
file = "pywhatkit_dbs.txt"

fileReal = open(file, 'r')
data = fileReal.read()
fileReal.truncate(3)
print(data)


# read
# write
# truncate delete the data
