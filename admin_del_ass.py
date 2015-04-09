import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

# check user identity
info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)

# get the name of the entity in which deletion will be conducted
form = cgi.FieldStorage()
# quit if get nothing
if not form.has_key("entity"):
    utility.redirect("admin_home.py")
    sys.exit(0)      
cur_name=form["entity"].value

# connect to database
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

# get all attributes in this entity
cursor.execute ("""show columns from {0}""".format(cur_name))
rows=cursor.fetchall()

# get attribute and value pairs
keys=[]
for row in rows:
    if "ID" in row[0]:
        if form.has_key(row[0]):
            keys.append((row[0],form[row[0]].value))
        else:
            utility.redirect("admin_home.py")
            sys.exit(0)

# try delete the instance            
isSuccess=1            
try:           
    cursor.execute("""delete from {0} where {1}={2} and {3}={4}""".format(cur_name,keys[0][0],keys[0][1],keys[1][0],keys[1][1]))
    db.commit()
except:
    db.rollback()
    isSuccess=0
db.close()


if isSuccess:
    sess.data["adminMSG"]="Deleted successfully!"
else:
    sess.date["adminMSG"]="Deletion failed"
    
utility.redirect("admin_home.py")
    
