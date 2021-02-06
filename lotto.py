import random

lotto_value = []
count = 0
one = 0
for i in range(7):
    a = random.randrange(1,46)
    lotto_value.append(a)

print(lotto_value)
lotto_input = input('로또 번호를 적어주세요').split(' ')
print(lotto_input)
for i in range(0,6):
    if int(lotto_input[i]) == lotto_value[i]:
        count += 1

if int(lotto_input[6] == lotto_value[6]):
    b = 1
else:
    b = 0

print('count',count)
if count >= 6:
    print('1등')
elif count + b >= 6:
    print('2등')
elif count +b >= 5:
    print('3등')
elif count + b >= 4:
    print('4등')
elif count + b >= 3:
    print('5등')
