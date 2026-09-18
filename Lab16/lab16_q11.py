char=str(input("Enter a letter: "))
vowels=['a','e','i','o','u']
for i in vowels:
    if char==str(i):
        print("The letter is a vowel")
        break
else:
    print("The letter is a consonant.")