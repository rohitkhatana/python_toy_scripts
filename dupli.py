import webapp2
import re
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
form="""
    <html>
        <form method="post">
            <a href="http://rohit-cs253.appspot.com/rot13">ROT13</a>
            <br>
            <div><a href="http://localhost:8080/unit2/signup">SIGNUP</a></div>
            What is your birthday?
            <br>
            <label>Day<input type="text" name="day" value="%(day)s"></label>
            <label>Month<input type="text" name="month" value="%(month)s"></label>
            <label>Year<input type="text" name="year" value="%(year)s"></label>
            <div style="color: red">%(error)s</div>
            <br>
            <br>
            <input type="submit">
        </form>
    </html>
"""
signup="""
    <html>
            <form method="post">
            <label style="color:blue">USERNAME <input name="usname" type="text" value="%(usname)s"></label><br>
            <label style="color:yellow">PASSWORD<input name="password" type="password" value="%(password)s"></label><br>
            <label style="color:49A66C">VERIFY PASSWORD<input name="verify" type="password" value="%(verify)s"></label><br>
            <label style="color:green">E-MAIL <input name="email" type="text" value="%(email)s"></label><br>
            <br>
           
            <br>
            <input type="submit">

        </form>
    </html>


"""
ROT13="""
    <html>
        <form method="post">
            <h2 style="color: blue">Enter the text Below:<h2>
            <input type="text" name="text" style="width:500px;height:140;" value="%(rot)s">     
            <br>
            <input type="submit">
        </form>
    </html>
"""  #"%(rot)s is preserving user's input"


month_abbvs = dict((m[:3].lower(),m) for m in months)
def escape_html(st):
    for (i,o) in (("&","&amp;"),("<","&lt;"),(">","&gt;"),('"',"&quot;")):
        st=st.replace(i,o)
    return st
def valid_month(month):
    if month:
        #month=month.capitalize()
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
        if month in months:
            return month
def valid_day(day):
    if day and day.isdigit():
        day=int(day)
        if day <=31 and day >0:
            return day
def valid_year(year):
    if year and year.isdigit() and len(year) ==4:
        year=int(year)
        if year <= 2040 and year >= 1920:
            return year

def rot13(p):
    q=""
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
    return q

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{6,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)
    
class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="",month="",day="",year=""):
        self.response.out.write(form % {"error": error,
                                        "month": escape_html(month),
                                        "day": escape_html(day),
                                        "year": escape_html(year)
                                        })
    def get(self):
        self.write_form()
    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)
        if not(month and day and day):
            self.write_form("enter valid date ...plz",
                            user_month, user_day, user_year)
        else:
            self.redirect("/thanks")
            self.redirect("/rot13")
            
            
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day")

class Rot13Handler(webapp2.RequestHandler):
    def write_form(self,rot=""):
        self.response.out.write(ROT13%{"rot":escape_html(rot)})   #this will escape the html character in the form rot13
    
    def get(self):
         self.write_form()
        
    def post(self):
        user_rot=self.request.get('text')
        user_rot1=self.request.get('text')
        rot=rot13(user_rot)
        self.write_form(rot)
        self.redirect("/rot13")
        
                            
                                
class SignUp(webapp2.RequestHandler):
    def write_form(self,error="",usname="",password="",verify="",email=""):
        self.response.out.write(signup%{"error":error,               #substituting into the form
                                        "usname":usname,
                                        "password":password,
                                        "verify":verify,
                                        "email":email,
                                        })
    def get(self):
        self.write_form()
    def post(self):
        us_input=self.request.get('usname')
        pass_input=self.request.get('password')
        ver_input=self.request.get('verify')
        email_input=self.request.get('email')
        error_flag=False
        
        if not valid_username(us_input):
            error_flag=True
            
            
        if not valid_password(pass_input):
            error_flag=True
       
        elif ver_input!=pass_input:
            error_flag=True

        if not valid_email(email_input):
            error_flag=True
        if error_flag:
            self.write_form("enter valid data....",us_input,pass_input,ver_input,email_input)
        else:
            self.redirect("/unit2/welcome?username=" + us_input)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username=self.request.get('username')
        if valid_username(username):
            self.response.out.write("welcome ")
        else:
            self.redirect('unit2/signup')
            
app = webapp2.WSGIApplication([
    ('/',MainHandler),
    ('/thanks',ThanksHandler),
    ('/rot13',Rot13Handler),
    ('/unit2/signup',SignUp),
    ('/unit2/welcome',Welcome)]
                              ,debug=True)
