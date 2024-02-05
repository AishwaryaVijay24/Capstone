def longpal(s):
    if s==s[::-1]:
        return s 
    left=longpal(s[1:])
    right=longpal(s[:-1])
    if len(left)>len(right):
        return left
    else:
        return right
    
str1=input()
print(longpal(str1))