from small import bot


file = "pywhatkit_dbs.txt"

fileReal = open(file, 'r')
data = fileReal.read()
fileReal.truncate(3)
bot.Talk(data)


# read
# write
# truncate delete the data
