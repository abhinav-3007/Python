import re

emails = '''
Abhinav-goyal@gmail.com
raghav.mehra@university.edu
python-321-pycharm@my-work.net
'''

urls = '''
https://www.google.com
http://facebook.com
https://youtube.com
https://www.data.gov
'''

pattern = re.compile(r"[\w.-]+@[a-z-]+\.[a-z]{2,3}")
pattern2 = re.compile(r"http[s]?://(w{3}\.)?[a-z]+\.[a-z]{2,3}")

matches = pattern.finditer(emails)
matches2 = pattern2.finditer(urls)

print("Emails:")
for match in matches:
    print(match)
print("URLs:")
for match in matches2:
    print(match)