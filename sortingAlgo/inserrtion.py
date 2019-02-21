'''
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:#x=67
        if x < minimum:# 23 < 67
            minimum = x#min=-23,-6,-5,0,5,23,23,67
    new_list.append(minimum)#-23,-6,-5,0,5,23,23,67
    data_list.remove(minimum)#-23,-6,-5,0,5,23,23,67

print(new_list)



def insertion(A):
    for i in range(1,len(A)):
        temp = A[i]
        k = i
        while k > 0 and temp < A[k-1]:
            A[k-1],A[k]=A[k],A[k-1]
            k -=1
    return A

a=[200,50,10,60,80]
insertion(a)
print(a)
'''

class Singleton:
    __instance=None
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception
        else:
            Singleton.__instance = self

    @staticmethod
    def getinstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance




def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1
    return lst

a=reverse('hello world')
print(a)

