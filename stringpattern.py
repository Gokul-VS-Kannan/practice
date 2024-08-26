a=input("Enter the string:")
b=""
c=""
for i in a:
    if i.isdigit():
        b=b+i
    else:
        b=b+" "
        c=c+i+" "
c=c.split()
b=b.split()
for i in range(len(c)):
    print(c[i]*int(b[i]),end="")