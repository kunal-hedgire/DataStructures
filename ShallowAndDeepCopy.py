#Shallow copy
'''
list1=[10,20,30,40,[100,200]]
list2=list1.copy()

print("original list",list1)
print("copied list ",list2)

list1[4][1]=150
#list1.append(500)

print("original list",list1)
print("copied list ",list2)
'''

import copy


list1=[10,20,30,40,[100,200]]
list2=copy.deepcopy(list1)


print("original list",list1)
print("copied list ",list2)

list2[4][1]=150
#list1.append(500)

print("original list",list1)
print("copied list ",list2)

