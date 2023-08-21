f = open('100_Days/Day49-File Io/edit2.txt', 'r')
while True:
    # readline returns the next line from file, if it exists (returns an empty string at EOF)
    line = f.readline()
    if not line:
        break
    # end='' is used to avoid adding a newline character at the end of each string
    print(line, end='')

print("")
f = open('100_Days/Day49-File Io/edit.txt', 'r')
i = 0
while True:
    i = i+1
    # readline returns the next line from file, if it exists (returns an empty string at EOF)
    line = f.readline()
    if not line:
        break
    # end='' is used to avoid adding a newline character at the end of each string
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])

    print(m1)
    print(m2)
    print(m3)
    print(line, end='')
