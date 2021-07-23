# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file html_spider
# @description html_spider
# @author WcJun
# @date 2021/07/22
# ---------------------------------------------


import requests
from bs4 import BeautifulSoup

from src.main.python.mysql.mysql import Mysql
from src.main.python.mysql.option import Options
from src.main.python.snowflake.snowflake import IdWorker


class Service(object):
    def __init__(self, machine: str, env: str, svc: str, pod: str, app: str, port: int):
        self.machine = machine
        self.evn = env
        self.svc = svc
        self.pod = pod
        self.app = app
        self.port = port


def do_spider_registry() -> []:
    # targets = []
    services = []
    registries = ['http://192.168.2.21:8761/', 'http://192.168.2.21:8762/', 'http://192.168.2.21:8763/']
    for registry in registries:
        response = requests.get(url=registry)
        registry_html = response.text
        if response.status_code == 200:
            soup = BeautifulSoup(registry_html, 'html.parser')
            pods = soup.findAll("a")
            # target_pods = [str]
            for pod_a_tag in pods:
                pod_txt = str(pod_a_tag.string)
                contents: list = pod_txt.split(':')
                if len(contents) > 2:
                    # target_pods.append(pod_txt)
                    svc: str = str(contents[0])
                    if svc.find('cluster.local') > 0:
                        machine: str = svc.split('-')[0]
                        evn: str = svc.split('.')[2]
                        pod: str = svc.split('.')[0]
                        service = Service(machine, evn, svc, pod, contents[1], int(contents[2]))
                        # target = json.dumps(obj=service, default=lambda x: x.__dict__, sort_keys=True, indent=4)
                        # targets.append(dict(service.__dict__))
                        services.append(service)

    # service_info = json.dumps(targets, sort_keys=True, indent=4)
    # print(service_info)
    # f = open("./service.json", mode="w", encoding="utf-8")
    # f.write(service_info)
    # f.close()

    return services


if __name__ == '__main__':
    options = Options('192.168.2.17', 'root', 'mysql', 'service_registry', 33004)
    mysql = Mysql(options)
    apps: [] = do_spider_registry()
    # app = json.dumps(obj=apps, default=lambda x: x.__dict__, sort_keys=True, indent=4)
    # print(app)
    parameters = []
    worker: IdWorker = IdWorker(0, 0)
    for spring_boot_service in apps:
        parameter = (
            worker.next_id(),
            spring_boot_service.machine,
            spring_boot_service.evn,
            spring_boot_service.svc,
            spring_boot_service.pod,
            spring_boot_service.app,
            spring_boot_service.port
        )
        parameters.append(parameter)

    sql = '''
    INSERT INTO `service_registry`(`id`, `machine`, `env`, `svc`, `pod`, `app`, `port`) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    mysql.insert(sql, parameters)

# def test_spider():
#     do_spider_registry()
