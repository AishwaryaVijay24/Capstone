nofele=int(input())
li=[]
for i in range(nofele):
    li.append(int(input()))
    
nofq=int(input())
for i in range(nofq):
    key=int(input)
    if key in li:
     #if found[key,li]>0:
        print(li.count(key))
    else:
        print("Not present")