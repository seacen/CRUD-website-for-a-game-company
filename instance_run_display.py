import session, MySQLdb, utility


utility.header("Instance Run", "instance run")

# Connect to DB
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM InstanceRun")

# get all instance runs  
rows = cursor.fetchall()
 
# display one instance run at a time
for row in rows:
    InsId = row[0]
    SuperId = row[1]
    Name = row[2]
    Time = row[3]       
    Category = row[4]
    
    # get supervisor's name 
    cursor.execute("SELECT * FROM Player where PlayerID={0}".format(SuperId))
    superrow = cursor.fetchone()
    supername = superrow[2]+" "+superrow[3]
    print """
    <hr class="featurette-divider">
    <div class="row featurette">
    
    <div class="col-md-7">
    <h3 class="featurette-heading"> <span class="text-muted">{0}</span></h3>
        
        <ul class="lead">
            <li>Recorded on {1}</li>
            <li>Category: {2}</li>
            <li>Supervised by <a href="player_display_detail.py?id={3}">{4}</a></li>
            <li>Featured players:
    """.format(Name, Time, Category, SuperId, supername)
    
    # get featured players in this instance run
    cursor.execute("select * from InstanceRunPlayer where InstanceRunID={0}".format(InsId))
    insrows = cursor.fetchall()
    for insrow in insrows:
        playerid = insrow[0]
        cursor.execute("select * from Player where PlayerID={0}".format(playerid))
        playerrow = cursor.fetchone()
        playername = playerrow[2]+" "+playerrow[3]
        print """
                <a href="player_display_detail.py?id={0}">{1}, </a>
        """.format(playerid, playername)
        
    print """
            </li>
            <li>Achievement:
                <ul>
    """
    
    # get achievements in this instance run
    cursor.execute("select * from Achievement where InstanceRunID={0}".format(InsId))
    achrows = cursor.fetchall()
    for achrow in achrows:
        ach_id = achrow[0]
        ach_time = achrow[2]
        ach_name = achrow[3]
        ach_reward = achrow[4]
        print """
                <li>{0}:\t{1} on \t{2}</li>
        """.format(ach_name, ach_reward, ach_time)
        
    # print none if no achievement
    if len(achrows)==0:
        print "None"
         
    print """
                </ul>
            </li>   
        </ul>
    </div>
    </div>
    """

utility.footer()