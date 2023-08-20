try:
    l = [1, 5, 6, 7]
    i = int(input("enter the index: "))
    print(l[i])


except:
    print('please enter a valid number')

finally:
    print('this is always executed')


def fun():
    try:
        l = [1, 5, 6, 7]
        i = int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print('please enter a valid number')
        return 0
    finally:
        print("hi")


fun()
