import socket


# Создаем  TCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10000)
print('Подключено к {} порт {}'.format(*server_address))
sock.connect(server_address)

try:
    # Отправка данных
    mess = input('>>>')
    print(f'Отправка: {mess}')
    message = mess.encode()
    sock.sendall(message)

    # Смотрим ответ
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f'Получено: {data.decode()}')

finally:
    print('Закрываем сокет')
    sock.close()