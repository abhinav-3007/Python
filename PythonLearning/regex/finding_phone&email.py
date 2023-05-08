import re

with open("data_for_regex.txt",'r') as fo:
    data = fo.read()

emailpattern = re.compile(r"[\w.-]+@[a-z-]+\.[a-z]{2,3}")
phonepattern = re.compile(r"[\d]{3}-[\d]{3}-[\d]{4}")

emailmatches = re.findall(emailpattern,data)
phonematches = re.findall(phonepattern,data)

email = []
phone = []

for match in emailmatches:
    email.append(match)

for match in phonematches:
    phone.append(match)

print("Email addresses:")
print(email)
print("\nPhone Numbers:")
print(phone)
