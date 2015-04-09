# Import the CGI moduleWork
import cgi, MySQLdb,utility,session,sys


sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

info=sess.data
loggedIn = info.get("loggedIn")

if not loggedIn or sess.data.get("UserType")!="A":    
    utility.redirect("login.py")
    sys.exit(0)
          
    
utility.header("Adding new Equipment","")
    
form = cgi.FieldStorage()
    
# connect to db
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)  

    
# get all attribute values
ModelAndMake = form.getvalue("ModelAndMake")
EquipmentReview = form.getvalue("EquipmentReview")
ProcessorSpeed = form.getvalue("ProcessorSpeed")

sql = "insert into Equipment(EquipmentID, ModelAndMake, EquipmentReview, ProcessorSpeed) values (DEFAULT,  '{0}',   '{1}',   '{2}')".format(ModelAndMake, EquipmentReview, ProcessorSpeed)

    
cursor = db.cursor()

try:
    cursor.execute(sql)
    db.commit()
    info['adminMSG']="new equipment has been added successfully!"
    
except:
    db.rollback()
    info['adminMSG']="Failed to add the new game, please fill in all compulsory fields."

# go back to admin home page
utility.redirect("admin_home.py")