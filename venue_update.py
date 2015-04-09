import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'P': 
    utility.redirect("login.py")
    sys.exit(0)
    
elif info.get("PlayerType")!="S":
    utility.redirect("login.py")
    sys.exit(0)
    
utility.header("Update Venue","venue")

print"""  
      <h1>Update Venue</h1>
      <h3>Please select the venue you would like to update.</h3>
      <form method="post" action="venue_update2.py">"""

db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)

cursor=db.cursor()

cursor.execute("""select VenueID,VenueName from Venue""")

rows=cursor.fetchall()

print """                    <div class="col-lg-5">
                                 <select name="VenueID" class="form-control" id="select">"""

for row in rows:
    print """<option value={0}>{1}</option>""".format(row[0],row[1])
    
    
print """</select></div>"""
print "<br><br><br>"    
print """<p><input class= "btn btn-primary" type="submit" id="search-submit" value="Next" /></p>"""
print "</form>"
    

utility.footer()
