sentence = "This is the first sentence."
words = sentence.split()
longest = max([word for word in words], key=len)
print(longest)