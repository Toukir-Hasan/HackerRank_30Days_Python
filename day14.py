class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maximum_number = max(self._Difference__elements)
        minimum_number = min(self._Difference__elements)
        f= abs(maximum_number - minimum_number)
        self.maximumDifference=f




# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)