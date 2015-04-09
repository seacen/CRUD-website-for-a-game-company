import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

# check user identity
info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)

# print web page header    
utility.header("Create Venue","venue")

# print form
print"""  
      <h1>Create a Venue</h1>
      <div class="row featurette" >
      <div class="well">
      <form class="bs-example form-horizontal" method="post" action="do_admin_add_Venue.py">
      <h3>Please fill the information below</h3><br>"""


# connect to database
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor=db.cursor()

# get all attributes in Venue
cursor.execute("""show columns from Venue""")
rows=cursor.fetchall()

for row in rows:
    if row[0]=="PowerOutlets":
        print """<p>{0}:&nbsp;&nbsp;&nbsp;<input type="number" min="1" name={0} id="ddd" value=1></p>""".format(row[0])
    elif row[0]=="SupervisorID":
        cursor.execute("""select PlayerID,PlayerFirstName,PlayerLastName from Player where PlayerType='S'""")
        sups=cursor.fetchall()
        print """<p>Supervisor Name:&nbsp;&nbsp;&nbsp;                    <div class="col-lg-5">
                                 <select name="SupervisorID" class="form-control" id="select">"""
        for sup in sups:
            print """<option value="{0}">{1}</option>""".format(sup[0],sup[1]+" "+sup[2])
        print "</select></div></p>"
    elif row[0]=="VenueName":
        print """<p>{0}:&nbsp;&nbsp;<input type="text" name="{0}" id="ddd"></p>""".format(row[0])
    elif "ID" not in row[0]:
        print """<p>{0}:&nbsp;&nbsp;<br><textarea name={0} rows="2" cols="50" id="ddd">None</textarea></p>""".format(row[0])
        
cursor.execute("""select EquipmentID,ModelAndMake from Equipment""")
rows=cursor.fetchall()
print """<br><br><br><h3>Please select the equipments and their versions that contained in the venue</h3>"""
for row in rows:
    print """<p><input type="checkbox" name="EquipmentID" value="{0}">{1}&nbsp;&nbsp;  <input type="number" min="1" step="0.1" name={0}V value=1 id="ddd"/><p>""".format(row[0],row[1])
print "<br><br><br>"    
print """<p><input class= "btn btn-primary" type="submit" id="search-submit" value="Creat Venue" /></p>"""
print "</form>"
