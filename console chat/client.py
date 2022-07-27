import socket

from _utils import *


class Client(object):
    def __init__(self):
        server_address = ('localhost', 10000)
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_.connect(server_address)

        self.name = None

        self.exit = False

    def run(self):
        """"""
        try:
            if self.name is None:
                self._get_name()

            while not self.exit:
                self._get_input().start()

                data = self.socket_.recv(1024)
                print(data.decode(), end="\n\n")

        finally:
            message = SECRET_KEY.encode()
            self.socket_.sendall(message)
            self.socket_.close()

    def _get_name(self):
        print("Enter your name:")
        self.name = input(">>>")
        print()

        message = self.name.encode()
        self.socket_.sendall(message)

    @thread_decorator
    def _get_input(self):
        """"""
        message = input()
        if message == "exit()":
            self.exit = True
        else:
            self.socket_.sendall(message.encode())


if __name__ == '__main__':
    client = Client()
    client.run()
