s1 = {1, 2, 3, 4, 5}

s2 = {2, 3, 4, 1, 8, 4, 5, 7, 8, 9, 0, }
print(s1.union(s2))
# s1.update(s2)
# print(s1, s2)
print(s1.intersection(s2))

print(s1.symmetric_difference(s2))
print(s2.difference(s1))

print(s1.isdisjoint(s2))

print(s2.issuperset(s1))
print(s1.issubset(s2))

s1.add(10)
print(s1)
a = s1.pop()
print(a)

s1.clear()
print(s1)
