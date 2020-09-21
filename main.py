#checks that num is not negative
num = -1
while num < 0:
    #ask the number to get the root of
    num = (int(input("Number?: ")))

res = -1
while res <= 0:
    #ask the resoloution of the approximation
    res = (float(input("Resoloution? (eg. 1, 0.1, 0.5): ")))

#calculate square root X
i = 0
x = 0
while (x <= num):
    i = i + res
    x = 1
    for j in range(2):
        x = x * i

if ((i + 1)**2 == num):
    square_X = i
elif ((i + 1)**2 - num) < (num - (i + 1)**2):
    square_X = i - res
elif ((i + 1)**2 - num) > (num - (i + 1)**2):
    square_X = i + res
else:
    square_X = 'ERROR'

#calculate cubed root X
i = 0
x = 0
while (x <= num):
    i = i + res
    x = 1
    for j in range(3):
        x = x * i

if ((i + 1)**3 == num):
    cube_X = i
elif ((i + 1)**3 - num) < (num - (i + 1)**3):
    cube_X = i + res
elif ((i + 1)**3 - num) > (num - (i + 1)**3):
    cube_X = i - res
else:
    cube_X = 'ERROR'

print('Square root approximation=', square_X)
print('Cube root approximation=', cube_X)
