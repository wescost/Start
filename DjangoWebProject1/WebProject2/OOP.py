class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def main():
    p=Point(3,4)
    print(p.x)
    print(p.__dict__["x"])
    print(p.y)
    print(p.__dict__)
    p1=Point(5,6);
    
main()

class Point1:
    def f(self):
        self.x=500

def super_main():
    d=Point1()
    d.x=100
    print(d.x)
    Point1.f(d)

super_main()

class Car:
    def __init__(self, make, petrol_consumption):
        self.make = make
        self.petrol_consumption = petrol_consumption

    def petrol_calculation(self, price = 22.5):
        return self.petrol_consumption * price


ford = Car("ford", 10)

money = ford.petrol_calculation()
print(money)

class Square:
    def __init__(self, x):
        self.x = x

    def find_square(self):
        return self.x ** 2

s = Square(5)
print(s.x)
square = s.find_square()
print(square)