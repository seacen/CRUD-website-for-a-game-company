import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'V':
    utility.redirect("video_display.py")
    sys.exit(0)

# connect to DB    
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)

cursor=db.cursor()

cursor.execute("""select VideoID from ViewerOrder natural join ViewerOrderLine where ViewerID={0}""".format(sess.data["UserID"]))

rows=cursor.fetchall()

utility.header("My Videos","video")

print"""  
      <h1>My Videos</h1><br><br><br><ul>"""


if len(rows) == 0:
    # this user has not yet ordered any video
    print """
        <h3><p>Oops! It seems you don't have any premium video yet.</h3></p>
        <h4> <a href="video_order.py">click here to order!</a></h4>
    """
else:
    # display his videos
    for row in rows:
        cursor.execute("""select * from Video where VideoID={0}""".format(row[0]))
        info=cursor.fetchone()
        cursor.execute("""select InstanceName from InstanceRun where InstanceRunID={0}""".format(info[4]))
        instanceName=cursor.fetchone()[0]
        cursor.execute("""select GameName from Game where GameID={0}""".format(info[5]))
        gameName=cursor.fetchone()[0]
        print """<li><a href="video_display_detail.py?id={0}">Video{0}</a>&nbsp;&nbsp;Price:{1}&nbsp;&nbsp;VideoType:{2}&nbsp;&nbsp;InstanceRun:{3}&nbsp;&nbsp;Game:{4}</li><br><br>""".format(info[0],info[2],info[3],instanceName,gameName)
    
    print "</ul>"

utility.footer()
    