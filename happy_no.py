'''
    language: python

Description of problem
A happy number is defined by the following process: 

Given a number X, square each digit and sum the results. Repeat this procedure on the resulting sum until you either reach 1, or fall into a repeating cycle which does not include 1. When this process ends in 1, X is a happy number.

The first line of the input will be an integer N (1 <= N <= 100).

Each of the following N lines represents a single test case, containing an integer X (1 <= X <= 100000).

For each test case, print 'Y' if X is a happy number, and 'N' if not. No blank line between test cases.


Sample input         Sample output

4
1                       Y
7                       Y
635                     Y
699                     N   
                        
'''



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
