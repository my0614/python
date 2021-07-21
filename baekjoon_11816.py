a = input()

if a[0] == '0':
    if a[1] == 'x':
        print(int(a,16))
    else:
        print(int(a,8))
if a[0] != '0':
    print(int(a,10))

    
