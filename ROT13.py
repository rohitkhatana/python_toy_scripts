q=""
p=input("enter the string->")


for i in range(0,len(p)):
    if 97 <= ord(p[i])and ord(p[i]) <= 122:
        if ord(p[i])+13 > 122:
            d=(ord(p[i])+13) - 122
            q=q+chr(97+d-1)
        else:
            q=q+chr(ord(p[i])+13)
    elif ord(p[i]) >=65 and ord(p[i]) <=90:
        if ord(p[i])+13 > 90:
                d=(ord(p[i])+13) - 90
                q=q+chr(65+d-1)
        else:
                q=q+chr(ord(p[i])+13)
    else:
        q=q+p[i]
                
                
                
print q
