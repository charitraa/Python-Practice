a = [[2,2],[1,1]]
b = [[2,2],[3,3]]
c= [[],[]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j]+= a[i][k] * b[k][j]

for i in c:
    print(i)