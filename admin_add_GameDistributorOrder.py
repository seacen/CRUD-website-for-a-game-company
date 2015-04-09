import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')
# check user identity
info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)

# print html header   
utility.header("Order Games","game")

print"""  
      <h1>Order Games</h1>
      <h3>Please select the games you would like to purchase.</h3>
      <form method="post" action="do_game_order.py">"""

# connect to database
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor=db.cursor()

cursor.execute("""select GameID,GameName from Game""")
rows=cursor.fetchall()

for row in rows:
    print """<p><input type="checkbox" name="id" value="{0}"/>{1} &nbsp;&nbsp;  <input type="number" min="1" name={2}Q placeholder="quantity" id="ddd"\></p>""".format(row[0],row[1],row[0])


print """<h3>Please select the distributor that you wish to purchase games from</h3>
            <div class="col-lg-5">
            <select name="dis" class="form-control" id="select">
"""

cursor.execute("""select GameDistributorID,CompanyName from GameDistributor""")
rows=cursor.fetchall()

for row in rows:
    print """<option value={0}>{1}</option>""".format(row[0],row[1])
    

print """</select></div>"""
print "<br><br><br>"    
print """<p><input class= "btn btn-primary" type="submit" id="search-submit" value="Place Order" /></p>"""
print "</form>"
    

utility.footer()
