import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)
    
form = cgi.FieldStorage()

# no id or distributor then back
if not (form.has_key("VenueName") and form.has_key("EquipmentID")):
    utility.redirect("venue_create.py")
    sys.exit(0)
    
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

cursor.execute("""show columns from Venue""")

rows=cursor.fetchall()

adds=[]
for row in rows:
    if form.has_key(row[0]):
        adds.append(form[row[0]].value)
        
    
        
cursor.execute("""insert into Venue values (default,'{0}','{1}',{2},'{3}',{4})""".format(adds[0],adds[1],adds[2],adds[3],adds[4]))
cursor.execute("""set @EID=LAST_INSERT_ID()""")
db.commit()
    
    
ids=form.getlist("EquipmentID")


for id in ids:
    cursor.execute("""insert into VenueEquipment values (@EID,{0},CURDATE(),{1})""".format(id,form[id+"V"].value))
    db.commit()

utility.header("Venue Creating Result","venue")
print """<br><br><br><br><h3>Your venue creating is successful!</h3>"""
print """<p><a class= "btn btn-primary" href="admin_add_venue.py">Back</a></p>"""
utility.footer()
    