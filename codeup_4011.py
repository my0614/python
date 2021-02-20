pin = input()
year= 0
month =0
gender = 0
if pin[7:8] == '1' or pin[7:8] == '2':
    year = 1900 + int(pin[0:2])
    month = pin[2:4]
    day = pin[4:6]
    if pin[7:8] == '1':
        gender = 'M'
    else:
        gender = 'F'
elif pin[7:8] == '3' or pin[7:8] == '4':
    year = 2000 + int(pin[0:2])
    month = pin[2:4]
    day = pin[4:6]
    if pin[7:8] == '3':
        gender = 'M'
    else:
        gender = 'F'

str = str(year)+"/"+str(month)+"/"+str(day)+" "+str(gender)
print(str)
