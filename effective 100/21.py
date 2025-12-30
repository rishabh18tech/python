u=int(input("enter totol units used"))
ans=0

if u>100:
    u-=100
    ans+= 100*1
else:
    ans+=u*1
    u=0

if u>300:
    u-=300
    ans+=300*3
else:
    ans+=u*3
    u=0
    
if u>400:
    u-=400
    ans+=400*5
else:
    ans+=u*5
    u=0

if u>0:
    ans+=u*8

print(ans," is your bijjli bill")