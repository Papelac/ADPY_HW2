from pprint import pprint
from fix_book import FIO, Phone, Equal_date
## Читаем адресную книгу в формате CSV в список contacts_list:
import os
import csv

current = os.getcwd()
file_name = 'phonebook_raw.csv'
full_path = os.path.join(current, file_name)

with open(full_path, 'rt', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

#pprint(contacts_list)

for line in contacts_list:
    FIO(line)
    Phone(line)

#pprint(contacts_list)

Equal_date(contacts_list)

#print(contacts_list)

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
new_file_name = 'fix_phonebook.csv'
new_full_path = os.path.join(current, new_file_name)
with open(new_full_path, "w", newline='', encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
  datawriter.writerows(contacts_list)