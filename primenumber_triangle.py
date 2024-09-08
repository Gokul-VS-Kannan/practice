# 2
# 3 11
# 5 13 19
# 7 17 23 29

n = int(input("Enter the value of n:"))
c = sum(list(range(1,n+1)))
a = []
d = 1
while len(a)<c:
    d = d+1
    z = 0 
    for i in range(1,d+1):
        if d%i==0:
            z=z+1
    if z == 2:
        a.append(d)
b=[]
c=n
d=0
m=n
for i in range(n):
    b.append(a[d:c])
    d=c
    m=m-1
    c=d+m
d=1
for i in b:
    c=d-1
    k=[]
    for j in range(d):
        k.append(b[j][c])
        c=c-1
    print(*k)
    d=d+1
    