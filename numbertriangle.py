n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        
        print(i, end=" ")
    print()

# out put
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

k=5
for i in range(1,k+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()   

# output"""""
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5  
a=10
for i in range(1,a+1):
    for j in range(1,i+1):
        print("$",end=" ")
    print()

#output
#$
#$ $
#$ $ $ 
#$ $ $ $

c=5
for i in range(1,c+1):
    for j in range(i,c+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

d=5
for i in range(1,d+1):
    print(" "*(d-i) + "* "*i)