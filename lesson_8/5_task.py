# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle

def func (dir)->None:
    json_files = [i for i in os.listdir(dir) if i.endswith('.json')]
    for json_file in json_files:
        with (open(os.path.join(dir, json_file), "r", encoding="UTF-8") as f,
              open(f'{os.path.join(dir, json_file)}.pickle', 'wb') as f1):
            json_dict = json.load(f)
            res = pickle.dumps(json_dict, protocol=pickle.DEFAULT_PROTOCOL)
            pickle.dump(json_dict, f1)


if __name__=='__main__':
    func(os.getcwd())