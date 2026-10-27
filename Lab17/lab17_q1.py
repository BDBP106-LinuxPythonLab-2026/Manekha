B = int(input("Enter a binary number: "))
decimal = 0
power = 0

while B > 0:
    digit = B % 10
    decimal = decimal + digit * (2 ** power)
    B = B // 10
    power = power + 1

print(decimal)