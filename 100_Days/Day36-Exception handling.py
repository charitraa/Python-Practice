from cmath import e


a = input("enter the number: ")
print(f"multiplication table of {a} is:")

try:

    for i in range(1, 11):
        print(f"{int(a)}x{i}={int(a)*i}")


except Exception as e:

    print('error:', e)


# except IndexError as a:
    # print("index out of bound ", {a})

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
