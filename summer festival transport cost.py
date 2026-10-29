n=int(input("Enter no of people:"))
p=int(input("Enter fuel cost for bus:"))
q=int(input("Enter fuel cost for shuttle:"))
bc,sc=0,0
if n%80==0:
    bc=n//80
else:
    bc=n//80 
    remaining_people=n-(bc*80)
    sc=remaining_people//8
    if n-(bc*80+sc*8)>0 and n-(bc*80+sc*8)<=8:
        sc+=1
cost=bc*p*75+sc*q*75
print(cost)