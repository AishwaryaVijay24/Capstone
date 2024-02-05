str1=input()
str1=str1.lower()
k=int(input())
li=[]
for i in range(len(str1)-(k-1)):
    li.append(str1[i:i+k])
li.sort()
print(li[0])
print(li[-1])