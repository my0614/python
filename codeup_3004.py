re = {}
result = []
def find_value(val):
    for key,value in re.items():
        if key == val:
            return value
        
cnt = int(input())
a = input().split(' ')
list_a = list(map(int, a))

list2_a = sorted(list_a)
for i in range(cnt):
    re[list2_a[i]] = i

for i in range(cnt):
    num = find_value(list_a[i])
    print(num,end=" ")
