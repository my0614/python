num = int(input())
num2 = int(input())
a_1 = num2 // 100
a_2 = num2  % 100 // 10
a_3 = num2 % 100 % 10 
print(num * a_3)
print(num * a_2)
print(num * a_1)
print(num * num2)
