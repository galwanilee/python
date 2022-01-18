def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Rectangle:
    def __init__(self, a, b):
        self.length = 1
        self.width = 1
        self.num = a
        self.den = b

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def show(self):
         print(self.num,"/",self.den)
    def __add__(self, otherRectangle):
        newnum = self.num * otherRectangle.den + \
                 self.den * otherRectangle.num
        newden = self.den * otherRectangle.den
        common = gcd(newnum, newden)
        return Rectangle(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    def per(self):
        print(2 * (self.length + self.width))

    def sq(self):
        print(self.width * self.length)

    def set_length(self, length):
        if length < 20.0:
            self.length = length

    def set_width(self, width):
        if width < 20.0:
            self.width = width

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_ab(self):
        print(f'числитель = {self.num} знаминатель = {self.den}')
        print(f'{self.num / self.den}')


x = Rectangle(1,2)
y = Rectangle(2,3)
print(x+y)
print(x == y)
