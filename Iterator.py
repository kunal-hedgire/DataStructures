'''
#Simple Iterator Example
list=[1,2,3,4,5]

mylist=iter(list)

#for items in mylist:
   # print(items)
while True:
   try:
        print(mylist.__next__())
        print(mylist.__next__())
        print(mylist.__next__())
        print(mylist.__next__())
        print(mylist.__next__())
        print(mylist.__next__())
        print(mylist.__next__())

   except StopIteration:
        break
'''

'''
#For Loop Internally Work 
list=[1,2,3,4,5]

myitr=iter(list)

while True:
    try:
        ele=next(myitr)
        print(ele)
    except StopIteration:
        break
'''

'''
#Power of Numbers
class PowTwo:

    def __init__(self,max=0):
        self.num = max

    def __iter__(self):
        self.n=0
        return self


    def __next__(self):
        if self.n <= self.num:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration

print("Using For Loop")

my_itr = PowTwo(4)
for items in my_itr:
    print(items)
itr=iter(my_itr)
print("For Implementations")
while True:
    try:
        ele = itr.__next__()
        print(ele)

    except StopIteration:
        break
'''












