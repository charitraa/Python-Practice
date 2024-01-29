a1 = (11, 72, 33, 77, 66, 55, 98, 37, 48, 36)
a = list(a1)
# After change u can change
b = a.sort()  # ascending order
# sort(reverse=true) descending order

print(a)
c = a.reverse()  # reversing the number

print(a)

e = a.insert(0, 11)  # add the position of index

print(a)
f = a.pop(1)  # remove the position of index
print(a)
g = a.remove(11)  # remove the elements
print(a)

# print(a.index(11))

# print("-----------------------------------")
print(a.count(11))
