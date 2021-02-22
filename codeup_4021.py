arr = input().split(' ')
#print(arr)
cnt = 0
for i in arr:
    if int(i) % 2 == 1: #홀수이면
        cnt += int(i)

if cnt == 0:
    print('-1')
else:
    print(cnt)
