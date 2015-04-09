# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb, utility, time
from datetime import date

sess = session.Session(expires=20*60, cookie_path='/')
# --------------------------------------------------------------------------------------------------------------------
# send session cookie
# ---------------------------------------------------------------------------------------------------------------------

def main():
    
    user_type = utility.header("Update Instance Run","player")
    
    
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn and user_type[1] != "S":    
        utility.redirect("login.py")
    
    else:

        form = cgi.FieldStorage()
        
        db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
        
        
        # 0 for no
        # 1 for yes
        edit_instance_run = form.getvalue("edit_instance_run")
        print edit_instance_run 

        instance_run_id = form.getvalue("instance_run_num ")
        print instance_run_id 
    
        # 0 for no
        # 1 for add into IR
        # 2 for delete from IR
        edit_player = form.getvalue("edit_player")
        edit_video = form.getvalue("edit_video")
        edit_achievement = form.getvalue("edit_achievement")
    
        print edit_player    
    
    

        # -----------------------------------------------------------------------------------------------------
        # update instance run detail
        if edit_instance_run == "1":
            # instance run detail for update
            new_instance_run_name = form.getvalue("new_instance_run_name")
            instance_run_date = form.getvalue("instance_run_date")
            instance_run_cate = form.getvalue("instance_run_cate")
        
            update_InstanceRun(db, instance_run_id, new_instance_run_name , instance_run_date, instance_run_cate)#
        
        
        
        
        # add one player into IR ------------------------------------------------------------------------------
        if edit_player == "1" :
            # new player detail
            
            player_chosed = form.getvalue("player_chosed_for_add")

            insert_InstanceRunPlayer(db, player_chosed, instance_run_id)#
        
        # delete player from IR
        if edit_player == "2":
            # player name for deletion
            player_chosed_for_del = form.getvalue("player_chosed_for_del")
            
            remove_InstanceRunPlayer(db, player_chosed_for_del, instance_run_id )#
        
        
        
        # add one Video related to IR -------------------------------------------------------------------------
        if edit_video == "1":
            # new Video detail
            new_video_url= form.getvalue("new_video_url")
            new_video_price= form.getvalue("new_video_price")
            new_video_type = form.getvalue("new_video_type")
            new_video_game = form.getvalue("game")
            
            insert_Video(db, instance_run_id, new_video_url, new_video_price, new_video_type, game)#
        
            # delelte Video related to IR
        if edit_video == "2":
            # Video URL for deletion
            video_url_for_delete = form.getvalue("video_url_for_delete")
    
            remove_Video(db, video_url_for_delete) #
    
    
    
    
        # add Achievement realted to IR -----------------------------------------------------------------------
        if edit_achievement == "1":
            # new achievement detail
            achievement_date= form.getvalue("achievement_date")
            achievement_name= form.getvalue("achievement_name")
            achievement_reward= form.getvalue("achievement_reward")
            
            insert_Achievement(db, instance_run_id, achievement_date, achievement_name, achievement_reward)#
    
    
        # delete Achievement realted to IR
        if edit_achievement == "2":
            # achievement name for deletion
            achievement_for_delete = form.getvalue("achievement_for_delete")
            
            remove_Achievement(db, achievement_for_delete )#

        
        
        db.close()
        
        
        
        
# end of main() -----------------------------------------------------------------------------------------------



        
def update_InstanceRun(db, instance_run_id, instance_run_name, instance_run_date, instance_run_cate):
    
    cursor = db.cursor()
    
    sql = """UPDATE InstanceRun SET InstanceName = '%s', RecordedTime ="%s", CategoryName = '%s' \
                WHERE InstanceRunID = %s """ \
                    % (instance_run_name, instance_run_date, instance_run_cate, instance_run_id)
    
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "uIR rollback"
# ---------------------------------------------------------------------------------------------------        
        
        
        
        
        
        
        
        
        
def insert_InstanceRunPlayer(db,player_chosed, instance_run_id):
    
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    
    
    
    sql = """SELECT * FROM Player  \
                WHERE PlayerFirstName = '%s' and SupervisorID = %s """\
                    % (player_chosed, sess.data["UserID"])
    

    cursor1.execute(sql)
    p_id = cursor1.fetchone()[0]
    

    sql = """INSERT INTO InstanceRunPlayer(PlayerID, InstanceRunID, PerformanceNotes) \
                VALUES(%s, %s, null) """ \
                    % (p_id , instance_run_id)
    
    try:
        cursor2.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "insert IRP rollback"
# ---------------------------------------------------------------------------------------------------

        
        
def remove_InstanceRunPlayer(db, player_chosed_for_del, instance_run_id ):
        
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    
    
    
    sql = """SELECT * FROM Player \
                WHERE PlayerFirstName = '%s' and SupervisorID = %s """ \
                    % (player_chosed_for_del, instance_run_id)
    

    cursor1.execute(sql)
    p_id = cursor1.fetchone()[0]
    

    sql = """ delete from InstanceRunPlayer \
                where PlayerID = %s and InstanceRunID = %s """ \
                    % (p_id , instance_run_id)
    
    try:
        cursor2.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "remove IRP rollback"
# ---------------------------------------------------------------------------------------------------
        
        
        
def insert_Video(db, instance_run_id, new_video_url, new_video_price, new_video_type, game):
            
    cursor1 = db.cursor()
    cursor2 = db.cursor()
        
    
    sql = """SELECT * FROM Game \
                WHERE GameName = '%s' """ \
                    % (game)
    

    cursor1.execute(sql)
    g_id = cursor1.fetchone()[0]
    
    
    

    sql = """INSERT INTO Video(VideoID, URL, Price, VideoType, InstanceRunID, GameID) \
                VALUES(        default, '%s', %s,      '%s',     %s,           %s) """ \
                    % ( new_video_url, new_video_price, new_video_type, instance_run_id, g_id )
    
    try:
        cursor2.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "insert Video rollback"
# ---------------------------------------------------------------------------------------------------






    
def remove_Video(db, video_url_for_delete):
        
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    
    
    
    sql = """SELECT * FROM Video \
                WHERE URL = '%s' """ \
                    % (video_url_for_delete)
    

    cursor1.execute(sql)
    v_id = cursor1.fetchone()[0]
    

    sql = """ delete from Video \
                where VideoID = %s """ \
                    % (v_id )
    
    try:
        cursor2.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "remove V rollback"
        
        
        
# ---------------------------------------------------------------------------------------------------
        
def insert_Achievement(db, instance_run_id, achievement_date, achievement_name, achievement_reward):
    
    
    cursor = db.cursor()
    
    

    sql = """INSERT INTO Achievement(AchievementID, InstanceRunID, WhenAchieved, AchievementName, RewardBody) \
                VALUES(default, %s, "%s", '%s', '%s') """ \
                    % (         instance_run_id, achievement_date, achievement_name, achievement_reward)
    
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "insert Achievement rollback"
        
# ---------------------------------------------------------------------------------------------------
        



def remove_Achievement(db, achievement_for_delete ):
    
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    
    
    
    sql = """SELECT * FROM Achievement \
                WHERE AchievementName = '%s' """ \
                    % (achievement_for_delete )
    

    cursor1.execute(sql)
    a_id = cursor1.fetchone()[0]
    print a_id 
    

    sql = """ delete from Achievement \
                where AchievementID = %s """ \
                    % (A_id )
    
    try:
        cursor2.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "remove Achievement rollback"
# ---------------------------------------------------------------------------------------------------
    
    
    
    
    

    
    
    
    
    
    
    
# Call main function.
main()
    
    
    
    
    
    
    
    
    
    
    
