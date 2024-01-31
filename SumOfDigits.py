def SOD(num):
    res=0
    while num>=10:
        res=0
        while num>0:
            res+=num%10
            num//=10
        num=res
    return res

num=int(input())
print(SOD(num))