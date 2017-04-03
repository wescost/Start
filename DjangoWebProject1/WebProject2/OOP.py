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