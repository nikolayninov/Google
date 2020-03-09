#!/usr/bin/python3
import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
f.close()
for row in csv_f:
    name, phone, role = row
    print(name, phone, role)
