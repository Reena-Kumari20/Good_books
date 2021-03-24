a=input("enter the num: ")
i=-1
s=len(a)
z=" "
j=-1
while i>-s:
    if a[i]=='0':
        i=i-1
    else:
        break
while i>=-s:
    z=z+a[i]
    i=i-1
k=len(z)
while j>=(-k):
    print(z[j],end="")
    j=j-1