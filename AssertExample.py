class Stud:
    def CalAvg(self,array):
        assert len(array) != 0 ,'cant find avg of empty list not a proper input'
        self.sum = 0
        for item in array:
            self.sum += item
        return self.sum/len(array)
s1=Stud()
avg=(s1.CalAvg([10,20]))
print(avg)