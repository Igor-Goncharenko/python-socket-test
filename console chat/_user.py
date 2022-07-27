from dataclasses import dataclass


@dataclass
class User:
    name: str
    ip: str
    port: int


class Message(object):
    id_count = 0

    def __init__(self, author: User, text: str):
        self.id = self.id_count
        self.id_count += 1
        self.author = author
        self.text = text

    def __repr__(self):
        return f'{self.author.name}: {self.text}'

    def get_message(self, other_author: User) -> str:
        if other_author == self.author:
            return f'You: {self.text}'
        else:
            return f'{self.author.name}: {self.text}'
