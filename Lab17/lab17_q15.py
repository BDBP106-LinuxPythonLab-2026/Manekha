L = ["kite", "king", "apple", "kangaroo", "ball"]
k = input("Enter starting character: ")

result = []

for word in L:
    if word.startswith(k):
        result.append(word)

print(result)