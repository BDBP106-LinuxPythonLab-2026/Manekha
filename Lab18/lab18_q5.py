S = input("Enter a sentence: ")

words = S.split()
seen = {}
result = []

for word in words:
    if word not in seen:
        seen[word] = 1
        result.append(word)

print(" ".join(result))