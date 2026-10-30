s1=input().upper()
s2=input().upper()
d1={}
d2={}
s=''
cost=0
for i in s1:
    d1[i]=s1.count(i)
for j in s2:
    d2[j]=s2.count(j)
for k,v in d2.items():
    if k in d1.keys():
        if v>d1.get(k):
            s+=k*v
            cost+=1*(abs(v-d1.get(k)))
        else:
            s+=k
    else:
        s+=k*v
        cost+=1*v
print(cost)