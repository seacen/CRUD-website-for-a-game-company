import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)


form = cgi.FieldStorage()

# no id or distributor then back
if not form.has_key("id"):
    utility.redirect("admin_add_GameShipment2.py")
    sys.exit(0)
    
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

ids=form.getlist("id")

for id in ids:
    quantity=form[id+"Q"].value
    cursor.execute ("""insert into GameShipmentDetail values ({0},{1},{2})""".format(id,form["shipID"].value,quantity))
    db.commit()
    
utility.header("Shipment Logging Result","game")
print """<br><br><br><br><h3>Your shipment logging is successful!</h3>"""
print """<p><a href="admin_add_GameShipment.py">Back</a></p>"""
utility.footer()