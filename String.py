str1=input()
str2=input()
print(len(str1)+len(str2))
if ascii(str1)>ascii(str2):
    print("YES")
else:
    print("NO")

print(str1.capitalize(),end=" ")
print(chr(ord(str2[0])-32),end="")
print(str2[1:])