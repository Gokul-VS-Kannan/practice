def parenthesis(n):
    def brackets(s="",left=0,right=0):
        if len(s) == 2*n:
            result.append(s)
            return
        if left < n:
            brackets(s + "(",left + 1,right)
        if right < left:
            brackets(s + ")",left,right + 1)

    result=[]
    brackets()
    return result

n=int(input("Enter the number:"))
result = parenthesis(n)
print(result)
