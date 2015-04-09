import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)


form = cgi.FieldStorage()

# no id or distributor then back
if not (form.has_key("id") and form.has_key("dis")):
    utility.redirect("game_order.py")
    sys.exit(0)
    
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

#create new order
cursor.execute ("""insert into GameDistributorOrder Values (default,CURDATE(),{0})""".format(form["dis"].value))
cursor.execute("""set @EID=LAST_INSERT_ID()""")
db.commit()

ids=form.getlist("id")

for id in ids:
    if not form.has_key(id+"Q"):
        quantity=1
    else:
        quantity=form[id+"Q"].value
        
    cursor.execute("""select Cost from Game where GameID={0}""".format(id))
    row=cursor.fetchone()
    cursor.execute ("""insert into OrderDetail values (@EID,{0},{1},{2})""".format(id,quantity,row[0]))
    db.commit()
    
utility.header("Game Order Result","game")
print """<br><br><br><br><h3>Your order placement is successful!</h3>"""
print """<p><a href="game_order.py">Back</a></p>"""
utility.footer()