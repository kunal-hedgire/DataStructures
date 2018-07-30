class P:
    limit1 = 18
    def __init__(self,age=0):
        self.__mage=age

    def set_age(self):
        return self.__mage

    def get_age(self):
        if self.__mage < 18:
            return self.limit1
        else:
           return self.__mage

    age=property(set_age,get_age)


    def __str__(self):
        return 'Age {}'.format(self.get_age())

my_p= P(22)
print(my_p)





