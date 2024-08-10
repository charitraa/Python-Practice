# # Concept:
# # File handling in Python allows you to interact with files on your system. You can read from, write to, and manipulate files using built-in functions. This is particularly useful for working with data stored in text files, CSV files, or even more complex file formats.


# Opening a File:

# Use the open() function to open a file. This function returns a file object.
# The basic syntax is:
# python
# Copy code
# file = open('filename', 'mode')
# Modes:
# 'r': Read(default mode).
# 'w': Write(overwrites the file if it exists).
# 'a': Append(adds content to the end of the file).
# 'b': Binary mode(for non-text files like images).


# read(): Reads the entire file.

import shutil
import os
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()


# readline(): Reads one line at a time.

file = open('example.txt', 'r')
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
file.close()


# readlines(): Reads all lines into a list.

file = open('example.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line)
file.close()


# Writing to a File:

file = open('example.txt', 'w')

file.write('This is a new line.\n')

file.close()


# Appending to a File:

file = open('example.txt', 'a')

file.write('This is an additional line.\n')

file.close()

lines = ['Hello, world!\n', 'This is a file.\n']
file = open('example.txt', 'w')
file.writelines(lines)
file.close()

# Close the file:

# After you're done working with a file, it's important to close it using the close() method. This ensures that the file is properly saved and the system can free up resources.

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# The with statement automatically closes the file after the block of code is executed.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# File Position:

# The file object keeps track of the current position in the file using the tell() method. You can use the seek() method to move the position to a specific byte offset.

file = open('example.txt', 'r')
content = file.read(10)
print(content)
print(file.tell())  # 10

file.seek(0)  # Move the position back to the start

content = file.read(10)

print(content)

file.close()

# File Size:

# You can get the size of a file using the getsize() method.


file_size = os.path.getsize('example.txt')
print(file_size)  # 40

# Renaming a File:


os.rename('example.txt', 'new_example.txt')

# Deleting a File:


os.remove('new_example.txt')

# Creating a Directory:


os.mkdir('new_directory')

# Deleting a Directory:


os.rmdir('new_directory')

# Copying a File:


shutil.copy('example.txt', 'copied_example.txt')

# Moving a File:


shutil.move('example.txt', 'moved_example.txt')

# Listing Files in a Directory:


directory_contents = os.listdir('directory_name')
print(directory_contents)
