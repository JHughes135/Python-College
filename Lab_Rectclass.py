


class Rectangle(object):
    def __init__(self):
        self.length = float(input("Please enter the height of the rectangle : "))
        self.width = float(input("Please enter the width of you rectangle : "))

    def area(self, width, length):
        area = (width * length)

        return area


rect1 = Rectangle()
rect2 = Rectangle()

print(rect1.length, "cm", rect1.width, "cm")
print(rect1.area(rect1.width, rect1.length), "cm^2")
