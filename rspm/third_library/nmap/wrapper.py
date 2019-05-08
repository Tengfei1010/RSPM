import nmap


def port_scanner(ip, ports=None, top=200):
    """
    Scanning opened ports in ip
    :param ip: target ip
    :param ports: if none using top
    :return: ports opened
    """
    nmap_scanner = nmap.PortScanner()

    if ports:
        nmap_scanner.scan(ip, ports)
    else:
        nmap_scanner.scan(ip, arguments=['--top-ports ' + str(top)])

    scan_result = nmap_scanner[ip]
    return scan_result


def services_scanner():
    pass
