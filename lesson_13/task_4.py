'''
Задание №4
Из json файла берутся данные для создания класса пользователей, и из класса множества  пользователей
'''
import json


class User:
    def __init__(self, name: str, user_id: str,  level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __repr__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __hash__(self):                                    
        return hash(self.name) + hash(self.user_id)

    def __eq__(self, other):                                                       
        return self.name == other.name and self.user_id == other.user_id




work_group = set()

def load_users(path: str = 'users2.json'):
    with open (path, 'r', encoding='UTF-8') as f:
        user_dict = json.load(f)
    for level, user_list in user_dict.items():
        for id, name in user_list.items():
            work_group.add(User(name, id, level))        


load_users()
print(work_group)