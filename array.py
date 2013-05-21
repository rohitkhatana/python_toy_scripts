import pdb
def main():
    f = open('c:\python27\My_Program\input.txt','r')

    st = f.read()
    st1 = ""
    for i in xrange(len(st)):
        if st[i].isdigit():
            st1 = st1+st[i]

    m=[]
    st=[34,37,656,97]

    for i in xrange(39):
        if i ==0:
            m.append(st[0])
        else:
            m1=((st[1]*m[i-1]+st[2])%st[3])
            m.append(m1)

    
    ch = 0
    k = 39
    n=97
    start=0
    
    """while(k<n):
        for i in range(k,n):
            if ch == m[i]:
                ch += 1
                i=0
        if i == (n-1):
            m.append(ch)
            ch =0
            k = k+1
    print m"""
    while(k<n):
        for i in range(start,k):
            if ch==m[i]:
                #print "rahul"
                ch =ch+1
                i=start
                print i,ch
        
        if i == k-1:
            #print "append"
             m.append(ch)
             #pdb.set_trace()
             start = start+1
             k=k+1
             
             
    print m
    

"""def small(start,end,m):
    #print end
    for i in range(start,end):
        #print i
        if m[i] == 0:
            break
    
    if i==end-1:
        m.append(0)
        print 'sdasd'
   """         
    
if __name__ == "__main__":
   main()
