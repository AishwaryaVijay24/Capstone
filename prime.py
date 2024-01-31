import math
num=int(input())
for i in range (2,num//2+1):
    if num%i==0:
        print(0.00)
        break
else:
    print("%.2f"%math.sqrt(num))
