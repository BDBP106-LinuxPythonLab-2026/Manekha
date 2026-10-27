#a:
a = [i for i in range(1, 51)]
even_numbers = a[1::2]
print(even_numbers)

#b:
a = [i for i in range(1, 51)]
new_list = a[:10] + a[35::2]
print(new_list)