import sys
result = []
n = int(input())
for i in range(n):
    a,b= map(int,sys.stdin.readline().split())
    result.append(a+b)

for i in result:
    print(i)
