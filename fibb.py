



def fib(num):
    l1,l2,l3=1,0,0
    for i in range(num)[2:]:
        l3=l1+l2
        print l3
        l2,l1=l1,l3
        

if __name__=="__main__":
    print 0
    print 1
    fib(5)
