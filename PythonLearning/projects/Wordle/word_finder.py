import csv

# Getting list of all words
with open('Word_List.txt', 'r') as file:
    words = file.read().split('\n')
freq = {}
for word in words:
    word_li = {*word}
    for character in word_li:
        if character in freq.keys():
            freq[character] += 1
        else:
            freq[character] = 1

# Adding frequencies of letters to file
with open('Letter_Frequencies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted(freq.items(), key=lambda x: x[1], reverse=True))

letters_list = ['', '', '']
with open('Letter_Frequencies.csv', 'r') as file:
    reader = csv.reader(file)
    # Getting list of most frequent letters
    for row in enumerate(reader):
        if row[0] < 5:
            letters_list[0] += row[1][0]
        elif row[0] < 10:
            letters_list[1] += row[1][0]
        elif row[0] < 14:
            letters_list[2] += row[1][0]
        else:
            break

# Getting words that use most frequent letters
for letters in letters_list:
    words_list = []
    for word in words:
        check_list = [letter in word for letter in letters]
        if all(check_list):
            words_list.append(word)
    print(words_list)
