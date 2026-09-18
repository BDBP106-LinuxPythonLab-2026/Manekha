num=int(input("Enter a number : "))
number=num
rev=0
while num > 0:
    rev=(rev + num%10)*10
    num=num//10
rev=rev//10
print (rev)
if number==rev:
    print ("The number is a palindrome.")
else:
    print ("The number is not a palindrome.")




