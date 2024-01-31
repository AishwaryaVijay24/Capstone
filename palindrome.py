def rev(num):
    res=0
    while num>0:
        res=res*10+num%10
        num//=10
    return res

num=int(input())
if rev(num)==num:
    print("Palindrome")
else:
    print("Not")