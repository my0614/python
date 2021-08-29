a,b=input().split(' ')
a=int(a)
b=int(b)
c=0
if a>b:
    for c in range(b,a+1):
        print(c)
if a<b:
    for c in range(a,b+1):
        print(c)
if a ==b:
    print(a)
