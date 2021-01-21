class siam:
    def __init__(self,initialAge):
        self.age=initialAge
    def amIOld(self):
        if self.age<0:
            self.age=0
            print('Age is not valid, setting age to 0.')
            print('You are young.')
        elif self.age>0 and self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearpasses(self):
        self.age+=1

t = int(input())
for i in range(0,t):
    age = int(input())
    p = siam(age)
    p.amIOld()
    for j in range(0,3):
        p.yearpasses()
    p.amIOld()
    print("")






