
class ComplexNum(object):

    def __init__(self):
        self.complex_num = input("Please enter your complex number in the form a+bi : ")
        self.a = []
        self.b = []
        self.passed = 0

        for num in self.complex_num:
            if num != '+':
                self.a.append(num)
            else:
                break

        self.passed = 0

        for x in self.complex_num:
            if x == '+':
                self.passed = 1

            while x != 'i' and x != '+' and self.passed == 1:
                self.b.append(x)
                break

        self.a_str = ''.join(str(e) for e in self.a)
        self.b_str = ''.join(str(e) for e in self.b)
        self.a_str = int(self.a_str)
        self.b_str = int(self.b_str)


def add_complex_nums(num1, num2):
    added_first_part = num1.a_str + num2.a_str
    added_second_part = num1.b_str + num2.b_str
    added_first_part = str(added_first_part)
    added_second_part = str(added_second_part)

    result = (added_first_part + '+') + (added_second_part + "i")

    print(result)


def subtract_complex_nums(var1, var2):
    added_first_part = var1.a_str - var2.a_str
    added_second_part = var1.b_str - var2.b_str
    added_first_part = str(added_first_part)
    added_second_part = str(added_second_part)

    result = (added_first_part + '+') + (added_second_part + "i")

    print(result)


num1 = ComplexNum()
num2 = ComplexNum()

print(num1.complex_num)
add_complex_nums(num1, num2)
subtract_complex_nums(num1, num2)
