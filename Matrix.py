r=int(input())
c=int(input())
main=[]
for i in range(r):
    li=[]
    for i in range(c):
        li.append(int(input()))
    main.append(li)
print(main)
for i in range(c):
    print(main[0][i])
for i in range(1,r):
    print(main[i][c-1])
for i in range(c-2,-1):
    print(main[r-1][i])
for i in range(r-2,0,-1):
    print(main[i][0])