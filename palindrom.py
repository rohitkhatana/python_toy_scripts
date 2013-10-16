import sys

def palindrom(s,le):
    k=0
    for i,j in zip(range(0,len(s)-1), range(len(s)-2,-1,-1)):
        print s[i],s[j]
        if s[i]!=s[j]:
            print 'not a palindrom'
            break
        else:
            k+=1
            
    if i == le-2:
        print 'yup, a palindrom'
            







if __name__=="__main__":
    s = sys.stdin.readline()
    palindrom(s,len(s))
