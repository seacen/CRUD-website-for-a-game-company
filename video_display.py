import MySQLdb,utility,session

sess = session.Session(expires=20*60, cookie_path='/')

utility.header("Videos", "video")

# connect to database
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor=db.cursor()

# get all video instances
cursor.execute("""select * from Video""")
rows=cursor.fetchall()

# print entrance for ordering videos
print """<a class="btn btn-primary" href="video_order.py">Buy Videos</a>"""

if sess.data.get("LoginError")==1:
    print """<h7>You do not have access to premium videos, please sign up</h7>"""
    sess.data["LoginError"]=0
    
# get and display each video's information
for row in reversed(rows):
    Id = row[0]
    cursor.execute("""select GameName from Game where GameID={0}""".format(row[5]))
    Game = cursor.fetchone()[0]
    cursor.execute("""select InstanceName from InstanceRun where InstanceRunID={0}""".format(row[4]))
    Instance_run = cursor.fetchone()[0]
    Price = row[2]
        
    
    print """
    <ul>
        <li>
            <a href="video_display_detail.py?id=%s">Video %s</a>
        </li>
        <li>Instance Run Name: %s</li>
        <li>Game Name: %s</li>
        <li>Price: %s</li>
    </ul>
    <hr/>
    """%(Id, Id, Instance_run, Game, Price)
     
utility.footer()



