with open('100_Days/Day49-File Io/edit2.txt', 'r') as f:
    f.seek(10)  # to skip the char
    # to read after the char
    print(f.tell())
    data = f.read(4)
    # print data
    print(data)


with open("100_Days/Day49-File Io/edit3.txt", 'w') as f:
    f.write("hello ravi")
    # f.truncate(5) to write how many char you want to write
