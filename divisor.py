m = 12
n = 8
list1 = [i for i in range(1, m+1) if m % i == 0] # m의약 수구하기
list2 = [i for i in range(1, n+1) if n % i == 0] # n의 약수구하기
if list1 == 2 and list2 == 2:
    print(m + n - 1)
else:
    list = []   # 아무것도 들어있지 않은 빈 리스트
    for i in list1: # list1의 값 
        if i in list:
           pass   
    else:
        if i in list2:
            list.append(i)
        for i in list2:
            if i in list:
                pass
            else:
                if i in list1:
                    list.append(i)
print(list)
