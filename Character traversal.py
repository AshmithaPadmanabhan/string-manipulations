s=input("Enter the string:")
s1=''
for i in range(len(s)):
    if s[i] not in s1:
        s1=s1+s[i]*(i+1)
        if i!=len(s)-1:
            s1+='-'
    elif s[i] in s1:
        a=s.find(s[i])
        s1=s1+s[i]*(a+1)
        if i!=len(s)-1:
             s1+='-'
print(s1)