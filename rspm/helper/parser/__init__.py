def parser_host(host_port):
    host_port = host_port.strip('\n')
    if ':' in host_port:
        items = host_port.split(":")
        if len(items) != 2:
            return "", 0
        return items[0], items[1]

    return host_port, 80
