#!/usr/bin/python3
import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scare ghost appeared"))
