from rspm.db.models import mdb, Target, WebInfo
from rspm.helper.parser import parser_host

from rspm.third_library.whatweb.wrapper import WhatWeb
from rspm.third_library.cmsscan.wrapper import cms_scan


def test_connect_db():
    print(mdb)


def test_insert_target_db():
    with open('data/hosts.txt', 'r') as f:
        for line in f.readlines():
            host, port = parser_host(line)
            if not host:
                continue
            target = Target()
            target.Host = host
            target.Port = str(port)
            target.save()
            print(target.id)

    assert Target.objects.count() == 5


def test_delete_target_db():

    for target in Target.objects:
        target.delete()


def test_insert_webinfo_db():
    whatweb = WhatWeb()
    for target in Target.objects:
        target_url = 'http://' + target.Host
        # call whatweb and cms_scan
        print(target_url)
        whatweb_result = whatweb.scan(target_url)
        cms_scan_result = cms_scan(target_url)
        print(whatweb_result)
        print(cms_scan_result)
        webInfo = WebInfo()
        webInfo.Target = target
        webInfo.Data = {"whatweb": whatweb_result, "cms_scan": cms_scan_result}
        webInfo.save()

    assert len(WebInfo.objects) == 5

    # delete all targets
    test_delete_target_db()

    assert len(WebInfo.objects) == 0


if __name__ == '__main__':
    test_connect_db()
    test_delete_target_db()
    test_insert_target_db()
    test_insert_webinfo_db()
