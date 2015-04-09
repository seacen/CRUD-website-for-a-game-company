import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

# check user identity, only supervisor has access to this functionality
info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'P': 
    utility.redirect("login.py")
    sys.exit(0)
    
elif info.get("PlayerType")!="S":
    utility.redirect("login.py")
    sys.exit(0)
    
# try get venueID
form = cgi.FieldStorage()
if not form.has_key("VenueID"):
    utility.redirect("venue_update2.py")
    sys.exit(0)    
venueID=form["VenueID"].value

# connect to database   
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

# get all attribute names in Venue
cursor.execute("""show columns from Venue""")

rows=cursor.fetchall()

adds=[]
for row in rows:
    if form.has_key(row[0]):
        cursor.execute("""update Venue set {0}='{1}' where VenueID='{2}'""".format(row[0],form[row[0]].value,venueID))
        db.commit()

delIDs=form.getlist("delEquipmentID")

for delID in delIDs:
    try:
        cursor.execute("""Delete from VenueEquipment where VenueID={0} and EquipmentID={1}""".format(venueID,delID))
        db.commit()
    except:
        db.rollback()        
    
ids=form.getlist("EquipmentID")


for id in ids:
    cursor.execute("""insert into VenueEquipment values ({2},{0},CURDATE(),{1})""".format(id,form[id+"V"].value,venueID))
    db.commit()

    
    
utility.header("Venue Updating Result","venue")
print """<br><br><br><br><h3>Update successfully!</h3>"""
print """<p><a class= "btn btn-primary" href="venue_update.py">Back</a></p>"""
utility.footer()