f = open('100_Days/Day49-File Io/edit2.txt', 'r')
while True:
    # readline returns the next line from file, if it exists (returns an empty string at EOF)
    line = f.readline()
    if not line:
        break
    # end='' is used to avoid adding a newline character at the end of each string
    print(line, end='')

f = open('100_Days/Day49-File Io/edit.txt', 'r')
while True:
    # readline returns the next line from file, if it exists (returns an empty string at EOF)
    line = f.readline()
    if not line:
        break
    # end='' is used to avoid adding a newline character at the end of each string
    print(line, end='')
