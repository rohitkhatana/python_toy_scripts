import re
usname=input('enter ur usname:')
passw1=input('enter password->')
passw2=input('varify password->')
user_re=re.compile(r"^[a-zA-z0-9_-]{3,20}$")
def valid_username(usname):
    return user_re.match(usname)
user_pass=re.compile(r"^.{6,20}$")
def valid_pass(passw1):
    return user_pass.match(passw1)


    
ch1=valid_pass(passw1)
if not ch1:
    print 'eneter a valid password'
else:
    if passw1<>passw2:
        print 'password is not same'
    else:
        print 'thanks'
ch=valid_username(usname)
if not ch:
    print 'eneter a valid usname'
else:
    print 'thanks'

    
