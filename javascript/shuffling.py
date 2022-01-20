# suffling.py
# import random
# name=['reena','sana','sara','anisha','anuradha','amrita','durga','deepti','rani']
# bed_room=['room_no.=>102,bed_no.=> 1','room_103,bed_3','room_201,bed_6']
# a=random.randint(0,len(name)-1)
# # print(a)
# b=name[a]
 
 
# x=random.randint(0,len(bed_room)-1)
# y=bed_room[x]
# print(b,"=>",y)
 
# name.remove(b)
# bed_room.remove(y)
# print(name)
# print(bed_room)
# suffling.py
import random
name=['reena','sana','sara','anisha']
bed_room=['room_no.=>102,bed_no.=> 1','room_no.=> 103,bed_no.=>3','room_no.=>104,bed_no.=> 1','room_no.=>102,bed_no.=> 1']
# a=random.randint(0,len(name)-1)
# print(a)
# b=name[a]
# print(b)
i=0
while i<len(name):
    a=random.randint(0,len(name))
    b=name[a]
    x=random.randint(0,len(bed_room))
    y=bed_room[x]
    print(b,"=>",y)
    name.remove(b)
    bed_room.remove(y)
    i=i+1
