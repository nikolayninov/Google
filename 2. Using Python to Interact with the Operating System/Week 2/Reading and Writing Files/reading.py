#!/usr/bin/python3
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

print("-"*15)

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
# Here we can see \n after every but the last line
print(lines)
