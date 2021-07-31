n = int(input())
file = []
for i in range(n):
    file_name = input().split('.')
    file.append(file_name[1])
f =sorted(set(file))
for i in f:    
    print(i,file.count(i))
