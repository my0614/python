import re
n = int(input())
string = input()
numbers = re.findall(r'\d+', string)
numbers = list(map(int,numbers))
print(sum(numbers))
