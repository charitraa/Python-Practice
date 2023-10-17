# 1.
import random
a = ['apple', 'orange', 'mango', 'banana', 'blueberry']

for i in a:
    print(i)

# 2.
a = ('12', '13', '14')
b = 0
for i in a:
    c = int(i)
    b = b + c

print(f"the volume of box{b}")
# 3.
a = 0
b = 1

while a < 10:
    if b % 2 == 0:
        print(b)
        a += 1
    b += 1
# 4.
sum = 0
for i in range(1, 101):
    sum = sum + i

print(sum)

# 6.
a = 0
b = 1

while a < 10:
    if b % 2 != 0:
        print(b)
        a += 1
    b += 1

# 5.
a = ['jhumka', 'kathmandu', 'patan', 'pokhara']

for i in range(len(a)):
    if len(a[i]) > 8:
        print(a[i])

# 6.
while True:
    a = int(input('enter the amount of multiple of 20:'))
    if a % 20 == 0:
        break

# 8.


b = random.randint(1, 100)
print(b)
while True:

    if b <= 50:
        c = 'low'
    else:
        c = 'high'

    a = int(input(f'enter the nubmber you want to guess which is {c}='))
    if a == b:
        print('you choice correct number')
        break
    else:
        print('you choice wrong number')
