hi = {"rabi:name", "caste:shrestha"}
local = {"rabi:name", "caste:sikh"}

# hi.update(local)

# hi.clear()
hi.pop()

print(hi)

# del local
# print(hi)

# creating a dictionary
country_capitals = {
    "United States": "Washington D.C.",
    "Italy": "Rome",
    "England": "London"
}

# printing the dictionary
print(country_capitals)

country_capitals = {
    "United States": "Washington D.C.",
    "Italy": "Rome",
    "England": "London"
}

# get dictionary's length
print(len(country_capitals))  # 3

country_capitals = {
    "United States": "Washington D.C.",
    "Italy": "Naples"
}

# delete item having "United States" key
del country_capitals["United States"]


print(country_capitals)
