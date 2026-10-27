text = input("Enter a string: ")
vowels = [char for char in text if char.lower() in "aeiou"]

print("Vowels:", vowels)