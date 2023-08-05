# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle
import csv

def print_pikle(file)->None:

    with (open(file, "r", encoding="UTF-8") as csv_f):
        csv_file = [*csv.reader(csv_f)]
        res = pickle.dumps(csv_file, protocol=pickle.DEFAULT_PROTOCOL)
        print(res)

if __name__=="__main__":

    print_pikle('itog.csv')