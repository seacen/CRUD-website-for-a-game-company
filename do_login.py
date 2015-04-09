# The libraries we'll need
import sys, cgi, session,utility, MySQLdb

# ---------------------------------------------------------------------------------------------------------------------
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# login logic
if loggedIn:
    utility.redirect("home.py")
    sys.exit(0)
else:
    form = cgi.FieldStorage()
    if not (form.has_key('username') and form.has_key('password')):
        sess.data['loggedIn'] = 0
    else:
        # Check user's username and password
        # Replace these values with your own login details
        db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
        #get check if we get a row from the database for this user and password
        cursor = db.cursor()
        cursor.execute ("""
            SELECT UserName,UserAccountID,UserType
            FROM UserAccount
            WHERE UserName = %s
              AND UserPassword = %s
        """, (form["username"].value, form["password"].value))
        if cursor.rowcount == 1:
            sess.data['loggedIn'] = 1
            row = cursor.fetchone()
            sess.data['UserName'] = row[0]
            sess.data['UserID']=row[1]
            sess.data['UserType']=row[2]
            if row[2]=="P":
                cursor.execute("""SELECT PlayerType from Player where PlayerID = {0}""".format(row[1]))
                row = cursor.fetchone()
                sess.data['PlayerType']=row[0]
            elif row[2]=="V":
                cursor.execute("""SELECT ViewerType from Viewer where ViewerID = {0}""".format(row[1]))
                row = cursor.fetchone()
                sess.data['ViewerType']=row[0]
                
        else:
            sess.data['loggedIn'] = 0
            sess.data['failedAtt']= 1

        
        
        # tidy up
        cursor.close()
        db.close()

    whereToNext = "home.py" if sess.data['loggedIn'] == 1 else "login.py"
    sess.close()
    
    # redirect to home page or back to the login page
    utility.redirect(whereToNext)

