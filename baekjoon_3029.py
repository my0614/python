now_time =  input().split(":")
domb_time = input().split(":")

now_time = list(map(int, now_time))
domb_time = list(map(int, domb_time))

now_t = now_time[0]*60*60 +60*now_time[1]+now_time[2]
domb_t = domb_time[0]*60*60+ domb_time[1]*60+domb_time[2]

if domb_t > now_t:
    re = domb_t - now_t
else:
    re = domb_t - now_t + (24*60*60)
    
h = re//60//60
m = re//60%60
s = re%60

print("%02d:%02d:%02d"%(h,m,s))

    
    
