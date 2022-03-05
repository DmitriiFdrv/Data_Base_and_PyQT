import subprocess

PROCESSES = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, '
                   'x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESSES.append(subprocess.Popen('python server.py',
                                          creationflags=subprocess.CREATE_NEW_CONSOLE))
        PROCESSES.append(subprocess.Popen('python client.py -n mes1',
                                          creationflags=subprocess.CREATE_NEW_CONSOLE))
        PROCESSES.append(subprocess.Popen('python client.py -n mes2',
                                          creationflags=subprocess.CREATE_NEW_CONSOLE))
        PROCESSES.append(subprocess.Popen('python client.py -n mes3',
                                          creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        while PROCESSES:
            VICTIM = PROCESSES.pop()
            VICTIM.kill()
