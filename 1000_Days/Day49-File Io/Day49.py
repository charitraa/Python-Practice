# read file
f = open('100_Days/Day49-File Io/edit.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# write

f = open('100_Days/Day49-File Io/edit2.txt', 'w')
f.write("hello")
# w for writing, a for appending and r for reading only
f.close()

# another way it avoid to close the file
with open("100_Days/Day49-File Io/edit2.txt", 'w'):
    f.write("hello hello")
