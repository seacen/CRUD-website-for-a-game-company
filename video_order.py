import sys,MySQLdb,utility,session,cgi

sess = session.Session(expires=20*60, cookie_path='/')

info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or info.get("UserType") != 'V':
    sess.data["LoginError"]=1   
    utility.redirect("video_display.py")
    sys.exit(0)

db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)

cursor=db.cursor()

cursor.execute("""select VideoID from ViewerOrder natural join ViewerOrderLine where ViewerID={0}""".format(sess.data["UserID"]))

rows=cursor.fetchall()

ids=[]
for row in rows:
    ids.append(row[0])


utility.header("Order Videos","video")

print"""  
      <h1>Order Videos</h1>
      <h7>{0}</h7>
      <h3>Please select the videos you would like to order.</h3>
      <form method="post" action="do_video_order.py">""".format("Your membership has expired, please renew" if sess.data.get("Expired")==1 else "")
if sess.data.get("Expired")==1:
    sess.data["Expired"]=0

cursor.execute("""select VideoID,GameName,InstanceName from Video natural join Game natural join InstanceRun where VideoType='premium' or VideoType='behind the scene'""")

rows=cursor.fetchall()

for row in rows:

    if row[0] in ids:
        print """
        <ul><a href="video_display_detail.py?id={0}">Video {1}</a> has been purchased
        """.format(row[0],row[0])
        
    else:
        print """
        <ul>
            <div class="checkbox">
                <label>
                    <input type="checkbox" name="id" value="{0}"> Video{0}
                </label>
            </div>
        """.format(row[0])
        
    print """
            <li>GameName: {0}</li>
            <li>InstanceRun: {1}</li>
        </ul>""".format(row[1],row[2])


print """
    <p><input class= "btn btn-primary" type="submit" id="search-submit" value="Place order" ></p>
    </form>
"""

        
utility.footer()