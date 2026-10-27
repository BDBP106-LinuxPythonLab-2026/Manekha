sentence = "This is is the first first sentence."
words = sentence.lower().split()
repeated = [word for word in words if words.count(word) > 1]
print(list(set(repeated)))