import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')
# check user identity
info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)
    
    
utility.header("Log a Game Shipment","game")
 

print"""  
      <h1>Log a Game Shipment</h1>
      <h3>Please select a distributor order of the shippment.</h3>
      <form method="post" action="admin_add_GameShipment2.py">"""

print """                    <div class="col-lg-5">
                                 <select name="disOrder" class="form-control" id="select">"""

# connect to database
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor=db.cursor()

cursor.execute("""select * from GameDistributorOrder""")

rows=cursor.fetchall()

for row in rows:
    cursor.execute("""select CompanyName from GameDistributor where GameDistributorID={0}""".format(row[2]))
    coName=cursor.fetchone()[0]
    print """<option value={0}>OrderID {1} &nbsp;SupplyDate: {2} &nbsp; {3}</option>""".format(row[0],row[0],row[1],coName)
    
    
print """</select></div>"""
print "<br><br><br>"    
print """<p><input class= "btn btn-primary" type="submit" id="search-submit" value="Next" /></p>"""
print "</form>"
    

utility.footer()
