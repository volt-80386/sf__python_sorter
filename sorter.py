#!/usr/bin/python
# -*- coding: utf8 -*- 

import argparse, csv, json, operator, datetime

# Настраиваем аргументы запуска (входной/выходной файл)
parser = argparse.ArgumentParser()
parser.add_argument("-i")
parser.add_argument("-o")
args = parser.parse_args()

# Открываем входной файл на чтение
if args.i:
    with open(args.i, 'r') as file1:
        data = file1.read()
else:
    sys.exit("Usage: sorter.py -i input_file -o output_file")

# Отрезаем лишние пробелы
cutdata = data.replace(' = ', '=')

# Импортируем как csv с разделителем =
mydata = csv.reader(cutdata.splitlines(), delimiter='=')

# Сортируем по возрастанию по второму столбцу
sort = sorted(mydata, key=operator.itemgetter(1), reverse=False)

# Берем самую последнюю строку из отсортированного списка и преобразуем второй столбец в дату
birth_date = datetime.datetime.strptime(sort[-1][1], '%Y-%m-%d')
# Вычисляем самый маленький возраст в годах (кол-во дней с даты рождения по сегодняшний день, разделенных на 365)
youngest = ((datetime.date.today() - birth_date.date()).days) // 365

# Объявляем массив
json_array = []
# Записываем данные в массив (Имя, возраст в днях, возраст на момент рождения самого молодого)
for line in sort:
    birth_date = datetime.datetime.strptime(line[1], '%Y-%m-%d')
    years_old = ((datetime.date.today() - birth_date.date()).days) // 365
    json_array.append(({'Name': line[0], 'DaysOld': (datetime.date.today() - birth_date.date()).days,'YearsOldWhenYoungestWasBorn': years_old - youngest}))

# Формируем json и записываем в выходной файл
if args.o:
    with open(args.o, 'w') as file2: 
        json_data = json.dumps(json_array, indent=4)
        file2.write(json_data)
else:
    sys.exit("Usage: sorter.py -i input_file -o output_file")
