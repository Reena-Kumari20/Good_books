# # from _future_ import print_function
# score_list = {}
# l=int(input("Enter the num: "))
# i=1
# while i<=l:
#     name = input("Enter the name: ")
#     score = float(input("Enter the float value: "))
#     if score in score_list:
#         score_list[score].append(name)
#     else:
#         score_list[score] = [name]
#     i=i+1
# print(score_list)
# new_list = []
# for i in score_list:
#     new_list.append([i, score_list[i]])
# new_list.sort()
# result = new_list[1][1]
# result.sort()
# print (*result, sep = "\n")

# x=int(input("num1: "))
# y=int(input("num2: "))
# items = list(range(1,x+1,2))
# items = items+items[::-1][1:]
# for i in items:
#     text= "WELCOME" if i == x else '.|.'*i
#     print (text.center(y,'-'))


# dictionary= {}
# num= int(input("Enter the num: "))
# i=1
# while i<=num:
#     keys= input("Enter the string: ")
#     if keys in dictionary.keys():
#         print(dictionary[keys],"@@@@@@")
#         dictionary[keys]+=1
#     else:
#         dictionary[keys] = 1
#     i=i+1
# print(dictionary)
# print(len(dictionary))

# for i in dictionary.values():
#     print(i, end=" ")
#     i=i+1

# n= 6                        #Pattern(1,121,12321,1234321,123454321)
# for i in range(1, n+ 1):
#     for j in range(1, i - 1):
#         print(j, end=" ")
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
#     print()

# n=int(input("enter the num: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i-1:
#         print(j,end=" ")
#         j=j+1
#     j=i-1
#     while j<-1:
#         print(j,end=" ")
#     i=i+1

# 1*1=1

# 11*11=121

# 111*111=12321
n=int(input("Enter the number; "))
st=""
i=1
while i<=n:
    j=i
    while j<=i:
        st=st+"1"
        a=int(st)
        print(a*a)
        j=j+1
    i=i+1