s = input()
if ':-)' in s or ':-(' in s:
    num = s.count('(')
    num2 = s.count(')')
    if num == num2:
        print('unsure')
    elif num > num2:
        print('sad')
    else:
        print('happy')
else:
    print('none')
