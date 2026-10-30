s=input().lower()
l=s.split(' ')
d={}
ll=[]
for i in l:
    s1=i[0]+i[-1]
    ll.append(s1)
    d[s1]=ll.count(s1)
maximum=max(d.values())
for k,v in d.items():
    if maximum==v:
        print(k)
