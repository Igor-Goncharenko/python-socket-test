import socket
from time import sleep

from _utils import *
from _user import User, Message


class Server(object):
    """"""
    def __init__(self):
        ip = 'localhost'
        port = 10000
        self.server_address = (ip, port)

        self.messages: list[Message] = []
        self.last_message_ids: dict[User: int] = {}
        self.server_user: User = User("server", ip, port)

    def run(self):
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socket_.bind(self.server_address)
        socket_.listen(1)
        print("[INFO] Server started. Waiting for users...")
        try:
            while True:
                connection, client_address = socket_.accept()
                print(f"[USER] Connected: {client_address}")
                self.user_connection(connection, client_address).start()
        except socket.error:
            print("[ERROR] Socket error")
        except Exception as e:
            print(f"[ERROR] {e.__class__.__name__}: \n{e} \n")
        finally:
            exit_message = Message(
                author=self.server_user,
                text=f"Server closes..."
            )
            self.messages.append(exit_message)
            sleep(2)

            socket_.close()

    @thread_decorator
    def user_connection(self, connection: socket.socket, client_address: tuple):
        user = None
        running = True
        try:
            while running:
                data = connection.recv(1024)

                if data is not None and data.decode() == SECRET_KEY:
                    running = False
                    break

                if data is not None and len(data.decode()) > 0:
                    if user is not None:
                        print(f"[MESSAGE] {user.name}: {data.decode()}")
                        message = Message(author=user, text=data.decode())
                        self.messages.append(message)
                        # connection.sendall(data)

                    else:
                        ip, port = client_address
                        user = User(name=data.decode(), ip=ip, port=port)
                        print(f"[USER] New user: {user.name}, ({user.ip}:{user.port})")
                        # old messages won't be sent
                        self.last_message_ids[str(user)] = len(self.messages)
                        # send other users messages
                        self._send_messages(connection, user).start()

        except socket.error:
            print("[ERROR] Socket error")
        except Exception as e:
            print(f"[ERROR] {e.__class__.__name__}: \n{e} \n")
        finally:
            connection.close()

            del self.last_message_ids[str(user)]

            exit_message = Message(
                author=self.server_user,
                text=f"User '{user.name}' logged out."
            )
            self.messages.append(exit_message)

            print(f"[USER] User: {user.name}, ({user.ip}:{user.port}) logged out.")

    @thread_decorator
    def _send_messages(self, connection: socket.socket, user: User):
        try:
            while str(user) in self.last_message_ids.keys():
                if user is not None:
                    max_message_id = len(self.messages)
                    for i in range(self.last_message_ids[str(user)], max_message_id):
                        message_text = self.messages[i].get_message(other_author=user)
                        connection.sendall(message_text.encode())
                        print(f"Message sent from {self.messages[i].author.name} to {user.name}. \n"
                              f"Text: {self.messages[i].text} \n {threading.current_thread()}")
                    self.last_message_ids[str(user)] = max_message_id
        except KeyError:
            ...
        except Exception as e:
            print(f"[ERROR] {e.__class__.__name__}: \n{e} \n")


if __name__ == '__main__':
    server = Server()
    server.run()
