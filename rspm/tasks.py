from rspm.app import celery
from rspm.constants import TaskType


@celery.task()
def add_together(a, b):
    return a + b


@celery.task()
def call_whatweb(url):
    from rspm.third_library.whatweb.wrapper import WhatWeb

    scanner = WhatWeb()
    result = scanner.scan(url)
    return {TaskType.WHATWEB: result}


@celery.task()
def call_nmap():
    return "call nmap"


@celery.task()
def call_cmsscan(url):
    from rspm.third_library.cmsscan.wrapper import cms_scan
    result = cms_scan(url)
    return {TaskType.CMS: result}
