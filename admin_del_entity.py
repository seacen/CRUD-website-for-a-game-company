import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)
    
form = cgi.FieldStorage()
if not form.has_key("entity"):
    utility.redirect("admin_home.py")
    sys.exit(0)
    
    
cur_name=form["entity"].value
id_name="{0}ID".format(cur_name)
if not form.has_key(id_name):
    utility.redirect("admin_home.py")
    sys.exit(0)
    
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()
isSuccess=1
try:
    cursor.execute("""delete from {0} where {1}={2}""".format(cur_name,id_name,form[id_name].value))
    db.commit()
    sess.data["adminMSG"]="{0} has been deleted successfully!".format(cur_name+form[id_name].value)  
except:
    db.rollback()
    if cur_name == "Player" or cur_name == "UserAccount":
        sess.data["adminMSG"]="failed to delete {0} as it is a supervisor account!".format(cur_name+form[id_name].value) 
    else: 
        sess.data["adminMSG"]="failed to delete {0}.".format(cur_name+form[id_name].value)  

db.close()


utility.redirect("admin_home.py")