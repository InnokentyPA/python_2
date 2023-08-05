# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла

import pickle
import csv
def to_csv(file_p)->None:
    with (open(file_p, 'rb') as f_pi,
          open("itog.csv", "w", newline='', encoding='utf-8', ) as f_csv,):
        picl_load = (pickle.load(f_pi))
        #print(picl_load)

        csv_write = csv.DictWriter(f_csv, fieldnames=['id','level','name','hash'])
        csv_write.writeheader()
        csv_write.writerows(picl_load)




if __name__=="__main__":
    to_csv('new_json.json.pickle')