# n=int(input("Enter the num: "))
# i=1
# while i<=n:
#         c=0
#         n1=int(input("Enter the number for divide: "))
#         j=1
#         while j<=n1:
#                 if n1%j==0:
#                         c=c+1
#                 j=j+1
#         if c==1:
#                 print("Yes")
#         elif c%2==0:
#                 print("No")
#         else:
#                 print("Yes")
#         i=i+1
list1=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(list1):
    j=1
    c=0
    while j<=list1[i]:
        if list1[i]%j==0:
            c=c+1
        j=j+1
    if c==2:
        print(list1[i],"is prime")
    else:
        print(list1[i],"not prime")
    i=i+1