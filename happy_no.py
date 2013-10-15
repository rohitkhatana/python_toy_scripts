import sys

def run():
    num = int(sys.stdin.readline())
    l=[num]
    while True:
        sum=0
        while num!=0:
            d = num%10
            sum +=(d*d)
            num=num/10
        if(sum==1):
            print "happy number"
            return
        elif sum in l:
            print 'not a happy no:'
            return
        else:
            num=sum
            l.append(num)
            

if __name__=="__main__":
    for i in range(int(sys.stdin.readline())):
        run()
