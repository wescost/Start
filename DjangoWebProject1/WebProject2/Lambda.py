s=lambda x,y:x+3*y
print(s(10,30))

def map(f,lis):
    return [f(elem) for elem in lis]

new_lis=map(lambda x:x+3,[10,20,30])