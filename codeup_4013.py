a = int(input())
value = a
result = ""
while 1:
    mok = a // 2
    na = a  % 2
    result += str(na)
    if mok == 0:
        break
    a = mok
result = result[::-1]          
print("2",result)
print("8 %o" % value)
print("16 %X" % value)
