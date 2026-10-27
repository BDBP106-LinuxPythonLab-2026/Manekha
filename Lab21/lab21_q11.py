from functools import reduce

words = ["Python", "is", "fun", "to", "learn"]
sentence = reduce(lambda a, b: a + " " + b, words)

print("Sentence:", sentence)