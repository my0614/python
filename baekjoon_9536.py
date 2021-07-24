n = int(input())
sound = []
for i in range(n):
    txt = input()
    while(1):
        animal = input()
        if animal != "what does the fox say?":
            sound.append(animal.split(' ')[2])
        else:
            break


re = txt.split(' ')

for i in sound:

    if i in re:
        while i in re:    
	        re.remove(i) # 'Smith' 삭제
for i in re:
    print(i, end=' ')
