from rspm.third_library.nmap.wrapper import port_scanner


def test_scan_ports():
    port_scanner('120.221.134.204')


if __name__ == '__main__':
    test_scan_ports()
