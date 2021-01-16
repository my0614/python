a = input()

f = open("test.txt","w")
f.write(a.lower())
f.write(a.upper())
f.close()
