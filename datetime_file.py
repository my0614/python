import time,datetime
f = open("time.txt","a")
cnt = 1
for i in range(10):
    t = datetime.datetime.now()
    f.write("%d line -> %s\n"%(cnt,t))
    time.sleep(1)
    cnt += 1
    print(t)
