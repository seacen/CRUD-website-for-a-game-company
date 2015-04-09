import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)
    
    
form = cgi.FieldStorage()

# no id or distributor then back
if not form.has_key("disOrder"):
    utility.redirect("admin_add_GameShipment.py")
    sys.exit(0)
    
    
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

cursor.execute ("""insert into GameShipment Values (default,CURDATE(),{0})""".format(form["disOrder"].value))
cursor.execute("""set @EID=LAST_INSERT_ID()""")
db.commit()

cursor.execute("select @EID")
shipmentID=cursor.fetchone()[0]

utility.header("Log a Game Shipment","game")

print"""  
      <h1>Log a Game Shipment</h1>
      <h3>Please select the games and quantities you have received.</h3>
      <form method="post" action="do_admin_add_GameShipment.py"><input type="hidden" name="shipID" value={0}>""".format(shipmentID)

cursor.execute("""select GameID,QuantityOrdered from OrderDetail where GameDistributorOrderID={0}""".format(form["disOrder"].value))

rows=cursor.fetchall()

for row in rows:
    cursor.execute("""select GameName from Game where GameID={0}""".format(row[0]))
    gameName=cursor.fetchone()[0]
    print """<p><input type="checkbox" name="id" value="{0}"/>{1} &nbsp;&nbsp;  <input type="number" name={2}Q min="1" max={3} value="1" id="ddd"\></p>""".format(row[0],gameName,row[0],row[1])
    
    
print "<br><br><br>"    
print """<p><input class= "btn btn-primary" type="submit" id="search-submit" value="Log Shipment" /></p>"""
print "</form>"
    

utility.footer()


