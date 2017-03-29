#def myfunc():
#    print("1")
#    yield 11
#    print("2")
#    yield 22

#f=myfunc()
#res=next(f)
#print(res)

#res1=next(f)
#print(res)

#def myrange(begin,end):
#    step=begin
#    while(init<end):
#        yield init
#        init+=1

#for i in myrange(0,20):
#    print(i)


def g():
    print("1")
    k=yield 3
    print(k)
    l=yield 4
    plint(l)

f=g()
k=next(f)
print(k)
k1=f.send(10)
print(k1)
