S1 = input("Enter first string: ")
S2 = input("Enter second string: ")

S1 = S1.lower().replace(" ", "")
S2 = S2.lower().replace(" ", "")

if sorted(S1) == sorted(S2):
    print("Anagrams")
else:
    print("Not anagrams")