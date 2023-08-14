a = ''' dear name,
u r calling from the phone which has broken by u.
so , please continues your call at any time


            thank you name   
            
            
                                 your friend
                                 .........
                                 date: Date
'''
b = input('yourName = ')
c = input('today date =')
a = a.replace('name', b)
a = a.replace('Date', c)
print(a)
