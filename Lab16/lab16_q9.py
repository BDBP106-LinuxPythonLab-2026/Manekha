num=int(input("Enter a number: "))
rev=0
while num>0:
    rev=(rev+num%10)*10
    num=num//10
rev=rev//10
print(rev)