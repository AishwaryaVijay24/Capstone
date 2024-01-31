import math

n=int(input())
A=0
B=7
while n:
    fn=int(input())
    if math.fabs(A-fn)<=math.fabs(B-fn):
        print("A")
        A=math.fabs(A-fn)
    else:
        print("B")
        B=math.fabs(B-fn)
    n=n-1


