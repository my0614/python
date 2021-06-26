a = input().split(' ')
a = list(map(int, a))
for i in range(2,a[0]*a[1]*a[2]+1):

    if i%a[0] == 0 and i%a[1] == 0 and i%a[2] == 0:
        print(i)
        break
