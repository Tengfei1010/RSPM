from bs4 import BeautifulSoup
import requests
import re
import base64
import urllib.parse


def un_base(s):
    if s == '/library':
        s = s
    else:
        s = re.split('=', s)[1]
        s = urllib.parse.unquote(s)
        s = s.encode(encoding="utf-8")
        s = base64.b64decode(s).decode()
    return s


if __name__ == '__main__':

    url = 'https://fofa.so/library'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 UBrowser/6.0.1471.914 Safari/537.36'}
    response = requests.get(url=url, headers=headers)

    response = BeautifulSoup(response.text, "lxml")

    rules = response.findAll('div', {'class': 'panel panel-default'})
    rule = {}

    for i in rules:
        # print(i.find('label').get_text())
        rule_len = len(i.findAll('a'))
        if rule_len > 0:
            rule_list = i.findAll('a')
            temporary = {}
            for b in rule_list:
                s = un_base(b.attrs['href'])
                temporary[b.get_text()] = s
            rule[i.find('label').get_text()] = temporary

    with open('rule.txt', 'w', encoding='UTF-8', errors='ignore') as f:
        for i in rule:
            types = i
            for b in rule[i]:
                name = b
                rules = rule[i][b]
                if rules == '/library':
                    print(name + '未找到')
                else:
                    line = types + ' ' + name + ' ' + rules + '\n'
                    f.write(line)
