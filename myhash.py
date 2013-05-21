import hashlib
import string
import random
def create_salt():
    s=""
    lis = random.sample(string.letters,5)
    for i in lis:
        s = s+i
    return s

def make_pw_hash(name, pw ,pass_salt):
    if pass_salt == None:           #this condition is only used at time of validating the password
        salt =create_salt()
    else:
        salt = pass_salt
    hashed = hashlib.sha256(name + pw + salt).hexdigest()   #we are hashing the password with username,pw,salt
    return '%s,%s' % (hashed,salt)                          #we are storing hashed password only and salt with it

def valid_pw(name,pw,hashed):
    salt = hashed.split(',')[1]
    if make_pw_hash(name,pw,salt) == hashed:
        return True

def create_salt2():
    return ''.join(random.choice(string.letters) for i in xrange(5))
def hash_str(s):
    return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split(',')[0]
    if h == make_secure_val(val):
        return val
    

if __name__== "__main__":
    #print check_secure_val(make_secure_val('rohit'))
    print make_pw_hash('rohit','1234','')
