class Student(object):

    def __init__(self, line):

        self.results = [1, 2, 3, 4]

        for r0 in line.split():

            self.name = r0
            self.result1 = r1
            self.result2 = r2
            self.result3 = r3
            self.result4 = r4

    def average(self):
        average = (self.result1 + self.result2 + self.result3 + self.result4) / 4

        print(average)


file = open("results.txt", "r")
