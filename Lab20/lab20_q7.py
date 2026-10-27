paragraph = input("Enter a paragraph: ")
words = paragraph.lower().split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:")
    if word != "":
        frequency[word] = frequency.get(word, 0) + 1

for word in sorted(frequency):
    print(word, ":", frequency[word])

highest = 0

for word in frequency:
    if frequency[word] > highest:
        highest = frequency[word]

print("Most frequent word(s):")

for word in frequency:
    if frequency[word] == highest:
        print(word, ":", highest)