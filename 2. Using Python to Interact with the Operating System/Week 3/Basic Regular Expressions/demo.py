#!/usr/bin/python3
import re
result = re.search(r"p.ng", "Pangea", re.IGNORECASE)
print(re.search(r"[Pp]ython", 'Python'))
print(re.search(r"[a-z]way", 'The end of the highway'))
print(re.search(r"[a-z]way", 'What a way to go'))
print(re.search(r"[a-zA-Z0-9]", 'cloudy'))
print(re.search(r"[a-zA-Z0-9]", 'cloud9'))
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like cats and dogs."))
print(re.findall(r"cat|dog", "I like both cats and dogs."))
print("-"*50)

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))  # Huh??
print(re.search(r"Py[a-z]*n", "Python Programming"))  # Huh??
print(re.search(r"p?each", "To each their own"))
print("-"*50)

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"^A.*a$", "Azerbaijan"))
pattern = r"^[a-zA-z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
