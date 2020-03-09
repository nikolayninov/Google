#!/usr/bin/python3
import os
import datetime

# os.remove("novel.txt")
# os.rename("sample.txt", "new_sample.txt")
print(os.path.exists("new_sample.txt"))

print(os.path.getsize("new_sample.txt"))
print(os.path.getmtime("new_sample.txt"))
timestamp = os.path.getmtime("new_sample.txt")
print(datetime.datetime.fromtimestamp(timestamp))
print(os.path.abspath("new_sample.txt"))
