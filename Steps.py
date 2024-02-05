def fun(n):
    if n<=2:
        return n 
    else:
        return fun(n-2)+fun(n-1)
    
n=int(input())
print(fun(n))
