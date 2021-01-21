class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self,firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores=scores
    def calculat(self):
        total_subjects = len(self.scores)
        total_scores = 0
        for x in self.scores:
            total_scores += x
        average = total_scores / total_subjects

        if average>=90 and average<=100:
            return "O"
        elif average>=80 and average<90:
            return "E"
        elif average>=70 and average<80:
            return "A"
        elif average>=55 and average<70:
            return "P"
        elif average>=40 and average<55:
            return "D"
        else:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculat())
