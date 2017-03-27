
def map(f,lis):
    #new_lis=[]
    #for elem in lis:
    #    new_lis.append(f(elem))

    #return new_lis
    return [f(elem) for elem in lis]

def func(x):
    return x+2

def func1(x):
    return x+3
n=[10,20,30]
print(map(func1,map(func,n)))

def reduce(g,init,lis):
    sum=init
    temp=lis[0]
    for i in lis:
        sum=g(sum,i)
    return sum

def plus(a,b):
    return a+b

n=[10,20,30]
new_n=map(func,n)
res=reduce(plus,0,new_n)

print(res)