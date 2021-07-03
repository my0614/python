
f = open("a.txt",'w')

for i in range(30):
    f.write('line %d\n' %(i+1))

f.close()
num = int(input())
f = open("a.txt",'r')
for i in range(num):
    print(f.readline(),end='')
f.close()
