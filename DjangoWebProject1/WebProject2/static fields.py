class A:
    aaa=100
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def f(self):
        return self.x+self.y


p=A(10,20)
print(p.__dict__)
print(A.__dict__)