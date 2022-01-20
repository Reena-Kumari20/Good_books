# import json
 
# # {key:value mapping}
# # a ={"name":"John",
# #    "age":31,
# #     "Salary":25000}
# # print(type(a))
# # # conversion to JSON done by dumps() function
# # b = json.dumps(a)
 
# # # printing the output
# # print(b)
# # print(type(b))

# var = {
#       "Subjects": {
#                   "Maths":85,
#                   "Physics":90
#                    }
#       }
# with open("Sample.json", "w") as p:
#      json.dump(var, p)

# a=[3,4,[5,6],7]
# i=0
# while i<len(a):
#       if type(a[i])==list:
#             j=0
#             while j<len(a[i])
#                   print(a[i][j])
#                   j=j+1
#       else:
#             print(a[i])
#       i=i+1
def two_highest(arg1):
      l1=[]
      a=max(arg1)
      arg1.remove(a)
      if arg1==[]:
            return []
      else:
            i=0
            while i<len(arg1):
                  if a==arg1[i]:
                        arg1.remove(arg1[i])
                  i=i+1
            b=max(arg1)
            l1.append(a)
            l1.append(b)
            return l1


print(two_highest([15, 20, 20, 17]))