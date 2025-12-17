ls =  [1, 2, 3, 4, 5]
y = list(map(lambda x: x ** 2, ls))
print(y)

z = [z**2 for z in ls]
print(z)