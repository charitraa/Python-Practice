# number 1


a = ['1', '2', '3', '4', '5', '6']
b = ['5', '6', '7', '8', '9', '10']
u = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


set_a = set(a)
set_b = set(b)
set_u = set(u)

a = set()

for i in set_u:
    if i not in set_a:
        a.add(i)

print(a)
# A_Bar = set_u-set_a
# print(A_Bar)

# A_Union_B = set_a.union(set_b)
# print(A_Union_B)

# A_intersect_B = set_a.intersection(set_b)
# print(A_intersect_B)

# A_subtract_B = set_a-set_b
# print(A_subtract_B)

# A_Symmetry_B = set_a.symmetric_difference(set_b)
# print(A_Symmetry_B)

# # number 2
