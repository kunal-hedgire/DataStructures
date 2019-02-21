class A:
    @classmethod
    def isAlphabet(cls,x):
        return x.isalpha()

    def toList(self,string):
        List = []
        for i in string:
            List.append(i)
        return List

    def toString(self,List):
        return ''.join(List)

    def reverse(self,string):
        LIST = self.toList(string)
        # Initialize left and right pointers
        r = len(LIST) - 1
        l = 0
        # Traverse LIST from both ends until
        # 'l' and 'r'
        while l < r:
            # Ignore special characters
            if not self.isAlphabet(LIST[l]):
                l += 1
            elif not self.isAlphabet(LIST[r]):
                r -= 1
            # Both LIST[l] and LIST[r] are not special
            else:
                LIST[l], LIST[r] = swap(LIST[l],LIST[r])
                l += 1
                r -= 1
        return self.toString(LIST)

def swap(a, b):
    return b, a
# Driver code
string = "a,b$c"
print('input is '+string)
a=A()
string = a.reverse(string)
print('output is '+string)



'''
class B:
    @classmethod
    def countTriplets(cls,arr, n):
        # Initialize result
        ans = 0
        sum = 12

        # Fix the first element as A[i]
        for i in range(0, n - 2):

            # Fix the second element as A[j]
            for j in range(i + 1, n - 1):

                # Now look for the third number
                for k in range(j + 1, n):
                    if (arr[i] + arr[j] + arr[k] < sum):
                        ans += 1
        return ans
# Driver program
b=B()
arr = [5, 1, 3, 4, 7]
n = len(arr)
sum=12

print(b.countTriplets(arr, n))
'''
'''

'''
# import copy
# old_list=[1,2,3,[4,5,6]]
# new_list=copy.copy(old_list)
# print("old list",old_list,"new list",new_list)
# old_list.append([4,4,2,4])
# print("change old list",old_list," change new list",new_list)
# old_list[3][2]=10
# old_list[1]=20
# print("change old list",old_list," change new list",new_list)
#
#

class A:
    pass
class B:
    pass
class C(B):
    pass
class D(C,A):
    pass

d=D()
print(())





