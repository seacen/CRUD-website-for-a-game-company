import sys,MySQLdb,utility,session,cgi,datetime

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn:
    utility.redirect("login.py")
    sys.exit(0)
elif info.get("UserType") != 'V':
    sess.data["LoginError"]=1     
    utility.redirect("video_display.py")
    sys.exit(0)

    
form = cgi.FieldStorage()

# no id then back
if not form.has_key("id"):
    utility.redirect("video_order.py")
    sys.exit(0)

    
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

if sess.data["ViewerType"]=="C":
    perk=1
#check premium subscription
else:
    perk=0
    cursor.execute("""select RenewalDate from PremiumViewer where ViewerID={0}""".format(sess.data["UserID"]))
    row=cursor.fetchone()
    if datetime.date.today()>row[0]:
        sess.data["Expired"]=1
        utility.redirect("video_order.py")
        sys.exit(0)
        
#create new order
cursor.execute ("""insert into ViewerOrder Values (default,CURDATE(),{0})""".format(sess.data["UserID"]))
cursor.execute("""set @EID=LAST_INSERT_ID()""")
db.commit()


ids=form.getlist("id")
#if greater than 1,handling in video_order
if len(ids)>1:
    for id in ids:
        cursor.execute ("""insert into ViewerOrderLine values ({0},@EID,{1},default)""".format(id,perk))
        db.commit()
    utility.redirect("video_order.py")

#only one video, handled at video_display_detail
else:
    id=ids[0]
    cursor.execute("""select * from ViewerOrderLine where VideoID={0} and ViewerOrderID=@EID""".format(id))
    if cursor.rowcount==1:
        cursor.execute("""DELETE FROM ViewerOrder WHERE ViewerOrderID=@EID""")
        db.commit()
        row=cursor.fetchone()
        sess.data["Show{0}".format(id)]=1
        utility.redirect("video_display_detail.py?id={0}".format(id))
        sys.exit(0)
        
    cursor.execute ("""insert into ViewerOrderLine values ({0},@EID,{1},'viewed')""".format(id,perk))
    db.commit()
                 
    sess.data["Show{0}".format(id)]=1
    utility.redirect("video_display_detail.py?id={0}".format(id))

