in_list = input().split(' ')
result = []
cnt = 0
for i in in_list:
    for j in i:
        cnt += int(j)
    result.append(cnt)
    cnt = 0

if len(in_list) == 11:
    result.remove(0)
print(max(result),min(result))
