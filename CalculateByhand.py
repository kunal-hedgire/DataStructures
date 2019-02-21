class Main_Code:
    def __init__(self,num):
        self.num = num

    def whichFinger(self):
        r = self.num % 8
        if r == 1:
            return r
        if r == 5:
            return r
        if r == 0 or r == 2:
            return 2
        if r == 3 or r == 7:
            return 3
        if r == 4 or r== 6:
            return 4
n=17
a=Main_Code(n)
b=a.whichFinger()
print(b)