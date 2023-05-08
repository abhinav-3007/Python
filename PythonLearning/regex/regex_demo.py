import re

sentence = "Start the day with an apple to keep the doctor away"

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
cricinfo.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Modi
Mr Tendulkar
Ms Nehwal
Mrs. Banerjee
Mr. T
'''

pattern = re.compile(r"")