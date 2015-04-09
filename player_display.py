import session, MySQLdb, utility


utility.header("Player", "player")

# Connect to DB
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM Player")

# get all player instances   
rows = cursor.fetchall()
    
for row in rows:
    Id = row[0]
    First_name = row[2]
    Last_name = row[3]       
    Gamehandle = row[8]
    Role = row[4]
    
    print """
        <ul>Player: %s           
            <li>Name: <a href="player_display_detail.py?id=%s">%s %s</a></li>
            <li>Role: %s</li>
            <li>Gamehandle: <a href="player_display_detail.py?id=%s">%s</a></li>
        </ul>
        <hr />
    """%(Id, Id, First_name, Last_name, Role, Id, Gamehandle)
     

utility.footer()

   

