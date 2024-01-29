a = input('enter a number: ')
try:
    b=int(a)
except:
    b = -1
if b > 0:
    print('i got your number ', a)
else:
    print('u dont have a eye')