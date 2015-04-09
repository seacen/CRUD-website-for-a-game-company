# Import the CGI module
import cgi, MySQLdb,utility,session,sys


sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie


info=sess.data
loggedIn = info.get("loggedIn")
if not loggedIn or sess.data.get("PlayerType")!="S":    
    utility.redirect("login.py")
    sys.exit(0)

result=0





#----------------------------------------------------------------------------------------------------------------

def extract_results(game_name, name, date, category, notes,
                    player_names, video_urls, video_prices, video_types,
                    achievement_names, achievement_rewards, num_of_players,num_of_videos ,num_of_achievements):
        
    # check results 
    if (game_name == None or name == None or
        len(player_names) != num_of_players or
        
        len(video_urls) != num_of_videos or
        len(video_prices) != num_of_videos or
        len(video_types) != num_of_videos or
        
        len(achievement_names) != num_of_achievements or
        len(achievement_rewards) != num_of_achievements):
        
        result = False
    else:
        result = True  
        
    return result




#----------------------------------------------------------------------------------------------------------------

def display_success(result):
    
    if result == True:
        s1 = "successful!"
        s2 = "homepage.py"
        s3 = "Click here to return to HOMEPAGE."
        
    else:
        s1 = "unsuccessful!\nPlease fill in all blanks."         
        s2 = "instance_run_add.py"
        s3 = "Click here to try again."
        
    
    
    print """
    <h2>Your upload was %s</h2>
    <a href=%s>%s</a>
</body>

</html>
""" %(s1, s2, s3)




#----------------------------------------------------------------------------------------------------------------
def instance_run_insert(db, game_name, name, date, category):


    cursor = db.cursor()
    
    sql = """INSERT INTO InstanceRun(InstanceRunID, SupervisorID, InstanceName, RecordedTime, CategoryName) \
        VALUES (default, %s, '%s', "%s", '%s' )""" \
                        % (sess.data["UserID"], name, date, category)    
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        print "iri rollback"
        

        
        
        
#----------------------------------------------------------------------------------------------------------------
def latest_instance_run_id(db):
    
    latest_id_cursor = db.cursor()
    
    # select last row just entered #
    latest_id_sql  = "SELECT * FROM InstanceRun ORDER BY InstanceRunID DESC LIMIT 1 "
    latest_id_cursor.execute( latest_id_sql )
        
    # get id
    latest_id = latest_id_cursor.fetchone()[0]
    
    return latest_id


#----------------------------------------------------------------------------------------------------------------
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def instance_run_player_insert(db, player_id, performance_notes, latest_id):
    
    insert_cursor = db.cursor()
    

    insert_sql = "INSERT INTO InstanceRunPlayer (PlayerID, InstanceRunID, PerformanceNotes) \
                    VALUES (%s,%s,'%s') " \
                        % ( player_id, latest_id, performance_notes )
    try:
        insert_cursor .execute( insert_sql )
        db.commit()        
        # Commit       
    except:
        # Rollback 
        db.rollback()
        print "irpi rollback"  

        
#----------------------------------------------------------------------------------------------------------------
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def insert_achievement(db, latest_id, date, achievement_name, achievement_reward):
    
    
    cursor = db.cursor()
    
    sql = """INSERT INTO Achievement(AchievementID, InstanceRunID, WhenAchieved, AchievementName, RewardBody) \
               VALUES (%s, %s, "%s", '%s', '%s') """ \
                   % ("default", latest_id, date, achievement_name, achievement_reward)
    
    try:
        cursor.execute( sql )
        db.commit()        
        # Commit       
    except:
        # Rollback 
        db.rollback()
        print "ia rollback"  

        
#----------------------------------------------------------------------------------------------------------------
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def insert_video(db, url, price, t, instance_run_id, game_id):
    
    
    cursor = db.cursor()
    

    
    
    
    sql = "INSERT INTO Video(VideoID, URL, Price, VideoType, InstanceRunID, GameID) \
                     VALUES (%s,     '%s',  %s,   '%s',     %s,             %s) " \
                   % ("default",    url,  price,     t,     instance_run_id,   game_id)
    
    try:
        cursor.execute( sql )
        db.commit()        
        # Commit       
    except:
        # Rollback 
        db.rollback()
        print "iv rollback"        
    
    
#----------------------------------------------------------------------------------------------------------------
def get_player_id(db, player_name):
    
    cursor = db.cursor()
    
    sql = "SELECT * FROM Player \
                WHERE PlayerFirstName = '%s'" \
                    % (player_name)
    
    cursor.execute(sql)
    player_id = cursor.fetchone()[0]

    return player_id


#----------------------------------------------------------------------------------------------------------------
def get_game_id(db, game_name):
    
    cursor = db.cursor()
    
    sql = "SELECT * FROM Game \
                WHERE GameName = '%s'" \
                    % (game_name)
    
    cursor.execute(sql)
    game_id= cursor.fetchone()[0]

    return game_id







#----------------------------------------------------------------------------------------------------------------
def main():
    
    utility.header("User Registration","")
    
    
    # Define main function.
    form = cgi.FieldStorage()
    
    # connect to db
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
    
    supervisor_id = sess.data["UserID"]
    
    
    
    # Get data from fields
    game_name = form.getvalue("game_name")
    
    
    name = form.getvalue("name")
    category = form.getvalue("category")
    date = form.getvalue("date")


    # get length of each list
    num_of_players = (int) (form.getvalue("num_of_players"))    
    num_of_videos = (int)(form.getvalue("num_of_videos"))
    num_of_achievements = (int)(form.getvalue("num_of_achievements"))
    
    
    
    ### get PerformanceNotes for InstanceRunPlayer
    performance_notes = form.getvalue("notes")
    

    ### get Player names -----------------------------------
    player_names = []
    for i in range(0,num_of_players):
        n = form.getvalue("player_name%s"%(i+1))
        player_names.append(n) 

        
    ### Videos and Game names ------------------------------
    video_urls = []
    video_prices = []
    video_types = []
    game_names = []

    for i in range(0,num_of_videos):
        url = form.getvalue(   "video_url%s"   % (i+1) )
        price = form.getvalue( "video_price%s" % (i+1) )   
        Type = form.getvalue(  "video_type%s"  % (i+1) )
        
        game_name = form.getvalue(  "game_name%s"  % (i+1) )
        
        
        video_urls.append(url)
        video_prices.append(price)
        video_types.append(Type)
        game_names.append(game_name)
        
        
    # Achievements ------------------------------------------
    achievement_names = []
    achievement_rewards = []

    for i in range(0,num_of_achievements):
        name = form.getvalue("achievement_name%s"%(i+1))
        reward = form.getvalue("achievement_reward%s"%(i+1))
        achievement_names.append(name)
        achievement_rewards.append(reward)

        
    
    # check all needed inputs are valid ----------------------------------------
    result = extract_results(game_name, name, date, category, performance_notes ,
                            player_names, video_urls, video_prices, video_types,
                            achievement_names, achievement_rewards,num_of_players,num_of_videos ,num_of_achievements)
    
    
    
    
    
    
    
    
    # if all needed inputs are valid----------------------------------------------------
    if result == True:
        
        
        
        ### insert new row into InstanceRun
        instance_run_insert(db, game_name, name, date, category)
        
        ### get latest id of instance run
        latest_id = latest_instance_run_id(db)
        
        
        ### insert new rows into InstanceRunPlayer
        for i in range(0, num_of_players): 
            
            # get player id by search firstname
            player_id = get_player_id(db, player_names[i])
            # then insert
            instance_run_player_insert(db, player_id, performance_notes, latest_id)

            
        ### insert new rows for Achievement
        for i in range(0, num_of_achievements):
            
            insert_achievement(db, latest_id, date, achievement_names[i], achievement_rewards[i])
            
              
        ### insert new rows for Video
        for i in range(0, num_of_videos ):
            # get game id
            game_id = get_game_id(db, game_names[i])
            
            # then insert
            insert_video(db, url, price, video_types[i], latest_id , game_id)

    
    display_success(result)


    
    db.close()
    

        

#----------------------------------------------------------------------------------------------------------------

main()
    





        
        
        
        
        
        
        