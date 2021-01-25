#!/usr/bin/python

import argparse, csv, json, operator, datetime

parser = argparse.ArgumentParser()
parser.add_argument("-i")
parser.add_argument("-o")

args = parser.parse_args()

if args.i:
    file1 = open(args.i,'r')
    
mydata = csv.reader(file1, delimiter=';')

sort = sorted(mydata, key=operator.itemgetter(1), reverse=False)

for line in sort:
    birth_date = datetime.datetime.strptime(line[1], '%Y-%m-%d')
    youngest = ((datetime.date.today() - birth_date.date()).days) // 365

json_array = []

for line in sort:
    birth_date = datetime.datetime.strptime(line[1], '%Y-%m-%d')
    years_old = ((datetime.date.today() - birth_date.date()).days) // 365
    json_array.append(({'Name': line[0], 'Days old': (datetime.date.today() - birth_date.date()).days,'Years old when youngest was born': years_old - youngest}))

with open(args.o, 'w') as file2: 
    json_data = json.dumps(json_array, indent=4)
    file2.write(json_data)