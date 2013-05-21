f = open('c:\python27\st.txt', 'r')
r = 1
st=""
for line in f:
    if r <= 5:
        st = st + line
        r+=1
st ="Sometimes test cases are hard to makeup."
st =st.lower()
d = {}
for i in range(0,len(st)):
    #if st[i] != '.' and st[i] != ' ' and st[i] != ':)' and st[i] != ';' st[i] != ')' and st[i] != '(' and st['i'] = ':':
    ord1 = ord(st[i])
    if 97 <= ord1 and ord1 <=122:
        if d.has_key(st[i]):            #if :
            s = d[st[i]]
            s = s+1
            d[st[i]] = s
        else:
            d[st[i]] = 1
#printd[]


ll = []
for l,v in d.iteritems():
     ll.append(v) 

ll.sort()

ll.reverse()
sm =0 
p=26
print ll
for l in ll:
    sm += l*p
    p=p-1
print sm
print d
