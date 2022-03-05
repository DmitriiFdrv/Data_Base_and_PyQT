import os
import platform
import subprocess
import time
from ipaddress import ip_address
from pprint import pprint

result = {'Доступные узлы': "",
          "Недоступные узлы": ""
          }


def check_is_ipaddress(value):
    try:
        ipv4 = ip_address(value)
    except ValueError:
        raise Exception('Некорректный ip адрес')
    return ipv4


def host_ping(hosts_list, get_list=False):

    print("Проверка доступности узлов...")
    for host in hosts_list:
        try:
            ipv4 = check_is_ipaddress(host)
        except Exception as e:
            print(f'{host} - {e} воспринимаю как доменное имя')
            ipv4 = host

        param = '-n' if platform.system().lower() == 'windows' else '-c'
        response = subprocess.Popen(["ping", param, '1', str(ipv4)], stdout=subprocess.PIPE)
        if response.wait() == 0:
            result["Доступные узлы"] += f"{str(ipv4)} "
            res_string = f"{str(ipv4)} - Узел доступен"
        else:
            result["Недоступные узлы"] += f"{ipv4} "
            res_string = f"{str(ipv4)} - Узел недоступен"
        if not get_list:
            print(res_string)
    if get_list:
        return result


if __name__ == '__main__':

    hosts_list = ['192.168.8.1', '8.8.8.8', 'yandex.ru', 'google.com',
                  '0.0.0.1', '0.0.0.2', '0.0.0.3', '0.0.0.4', '0.0.0.5',
                  '0.0.0.6', '0.0.0.7', '0.0.0.8', '0.0.0.9', '0.0.1.0']
    start = time.time()
    host_ping(hosts_list)
    end = time.time()
    print(f'total time: {int(end - start)}')
    pprint(result, width=30)
