class A:
    @classmethod
    def isAlphabet(cls, string):
        List = []
        for i in string:
            List.append(i)
        LIST = List
        # Initialize left and right pointers
        r = len(LIST) - 1
        l = 0
        # Traverse LIST from both ends until
        # 'l' and 'r'
        while l < r:
            # Ignore special characters
            if not LIST[l].isalpha():
                l += 1
            elif not LIST[r].isalpha():
                r -= 1
            # Both LIST[l] and LIST[r] are not special
            else:
                LIST[l], LIST[r] =LIST[r],LIST[l]
                l += 1
                r -= 1
        return ''.join(List)

string = "abc$dhf%"
print('input is ' + string)
a = A()
string = a.isAlphabet(string)
print('output is ' + string)