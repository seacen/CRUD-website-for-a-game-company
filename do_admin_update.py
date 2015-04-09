import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'A': 
    utility.redirect("login.py")
    sys.exit(0)

form = cgi.FieldStorage()
if not form.has_key("entity"):
    utility.redirect("admin_home.py")
    sys.exit(0)
    
cur_name=form["entity"].value
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

cursor.execute ("""show columns from {0}""".format(cur_name))
rows=cursor.fetchall()
attris=[]
for row in rows:
    attris.append(row[0])

cursor.execute("""select {0}ID from {0}""".format(cur_name))

rows=cursor.fetchall()

upd_list=[]
has=0
for row in rows:
    row_list=[]
    for attri in attris:
        if form.has_key(attri+str(row[0])):
            has=1
            row_list.append((attri,form[attri+str(row[0])].value))
        else:
            row_list.append(())
    upd_list.append((row[0],row_list))

            

if not has:
    utility.redirect("admin_home.py")
    sys.exit(0)

success="Update successfully"
smallSuccess="  successfully updated "
error="Error has occured in "
isWrong=0
hasSuccess=0
    
for row in upd_list:
    for attri in row[1]:
        if attri!=():
            smallWrong=0
            try:
                cursor.execute("""update {3} set {0}='{1}' where {3}ID={2}""".format(attri[0],attri[1],row[0],cur_name))
                db.commit()
            except:
                db.rollback()
                isWrong=1
                smallWrong=1
                error+="{2}{0} {1}, ".format(row[0],attri[0],cur_name)
            if not smallWrong:
                hasSuccess=1
                smallSuccess+="{2}{0} {1}, ".format(row[0],attri[0],cur_name)
                
                
if isWrong:
    if hasSuccess:
        sess.data["adminMSG"]=error+smallSuccess
    else:
        sess.data["adminMSG"]=error
else:
    sess.data["adminMSG"]=success
    
db.close()
utility.redirect("admin_home.py")
