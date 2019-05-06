# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package


if __name__ == '__main__':
    from rspm.third_library.whatweb.wrapper import WhatWeb

    scanner = WhatWeb()
    result = scanner.scan("http://www.lanrentuku.com/")
    print(result)
