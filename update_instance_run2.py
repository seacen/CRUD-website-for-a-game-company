# Import the CGI module
import cgi, MySQLdb,utility,session,sys

sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

# Define function to generate HTML form.
def generate_form():
    

    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
    form = cgi.FieldStorage()
    
    
    
    # 0 for no
    # 1 for yes
    edit_instance_run = form.getvalue("edit_instance_run")

    instance_run_name = form.getvalue("instance_run_name")

    sql0 = """SELECT * FROM InstanceRun \
                WHERE InstanceName = '%s' """ \
                    %(instance_run_name )
    
    cursor0 = db.cursor()
    cursor0.execute(sql0)
    instance_run_num = cursor0.fetchone()[0]
    
    # 0 for no
    # 1 for add into IR
    # 2 for delete from IR
    edit_player = form.getvalue("edit_player")
    edit_video = form.getvalue("edit_video")
    edit_achievement = form.getvalue("edit_achievement")
    

    
    print """

    <div class="row featurette" >
        <div class="well">
            <form class="bs-example form-horizontal" method=post action="do_update_instance_run.py">  
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="White" > <b><i>Update infomation related to Instance Run</i></b> </font> </p>
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="col-lg-4">
                  <p> <font size="4" color="red" > <b><u>Please fill all fields with *</u></b> </font> </p>
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Instance Run Name</label>
                    <div class="col-lg-5">

                      <input  class="form-control"  id="disabledInput" type="text" name=""  value="{0}" disabled="" >
                      <input type = "hidden" name = "instance_run_num"  value="{5}">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label"></label>
                    <div class="col-lg-5">
                      <input  class="form-control" id="disabledInput" type="text" name="edit_instance_run" value="{1}" disabled="">
                      <input type = "hidden" name = "edit_instance_run"  value="{1}">
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-lg-4 control-label"></label>
                    <div class="col-lg-5">
                      <input  class="form-control" id="disabledInput" type="text" name="edit_player" value="{2}" disabled="">
                      <input type = "hidden" name = "edit_player"  value="{2}">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label"></label>
                    <div class="col-lg-5">
                      <input  class="form-control" id="disabledInput" type="text" name="edit_video" value="{3}" disabled="">
                      <input type = "hidden" name = "edit_video"  value="{3}">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label"></label>
                    <div class="col-lg-5">
                      <input  class="form-control" id="disabledInput" type="text" name="edit_achievement" value="{4}" disabled="">
                      <input type = "hidden" name = "edit_achievement"  value="{4}">
                    </div>
                  </div>

                </fieldset>
    """.format(instance_run_name, edit_instance_run, edit_player, edit_video, edit_achievement, instance_run_num  )
    
    


    # edit instance run detail
    if edit_instance_run == "1":
        
        
        sql1 = """Select * from InstanceRun \
                    WHERE InstanceRunID = '%s' and SupervisorID = %s""" \
                        % (instance_run_num , sess.data["UserID"])
    
        cursor1 = db.cursor()
        cursor1.execute(sql1)
        instance_run_row = cursor1.fetchone()
        
        ir_name = instance_run_row[2]
        ir_date = instance_run_row[3]
        ir_cate = instance_run_row[4]
        print """

    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Instance Run Name*</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "text" name = "instance_run_name"  value="{0}">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Date*</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "date" name = "instance_run_date"  value="{1}">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Category Name*</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "text" name = "instance_run_cate"  value="{2}">
                    </div>
                  </div>
    """.format( ir_name, ir_date, ir_cate )
    
    
    
#   -------------------------------------------------------------------------------------------------------------------------

    # add one player into IR ------------------------------------------------------------------------------
    if edit_player == "1" :
        print"""
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="3" color="red" > <b><u>Choose which player you want to add:</u></font> </p>
                    </div>
                  </div>
    """
        sql2 = """SELECT PlayerID FROM Player \
                    Where PlayerID not in (SELECT PlayerID from InstanceRunPlayer WHERE InstanceRunID = %s)\
                        AND SupervisorID = %s """ \
                        %( instance_run_num , sess.data["UserID"] )
        
        
    
    
        
    
        cursor2 = db.cursor()
        cursor2.execute(sql2)
        player_row = cursor2.fetchone()
        
        

        print """
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Player Name*</label>
                    <div class="col-lg-5">
                        <select class="form-control" id="select" name="player_chosed_for_add" >
        
    """
        while player_row is not None:
        
        
            player_id_sql = """SELECT PlayerFirstName FROM Player \
                                WHERE PlayerID = %s """ \
                                    %(player_row[0])
            player_id_cursor = db.cursor()
            player_id_cursor.execute(player_id_sql)
            fn = player_id_cursor.fetchone()[0]
            print """
                             <option>%s</option>
            """ % (fn)
        
        
            player_row = cursor2.fetchone()
        
        print""" 
                        </select>
                    </div>
                  </div>
    """
        
    # -----------------------------------------------------------------------------------------------------
    

    # delete player from IR -----------------------------------------------------------------------------------------
    if edit_player == "2":
        print"""
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="3" color="red" > <b><u>Choose which player you want to delete: </u></b> </font> </p>
                    </div>
                  </div>
    """
    
        sql2 = """select * from InstanceRunPlayer \
                    inner join Player On Player.PlayerID = InstanceRunPlayer.PlayerID \
                        where InstanceRunID = %s""" \
                            %(instance_run_num )

        cursor2 = db.cursor()
        cursor2.execute(sql2)
        player_row = cursor2.fetchone()

        print """
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Player Name*</label>
                    <div class="col-lg-5">
                        <select class="form-control" id="select" name="player_chosed_for_del" >
        
    """
        while player_row is not None:
            print """
                             <option>%s</option>
            """ % (player_row[5])
            player_row = cursor2.fetchone()
    
        print""" 
                        </select>
                    </div>
                  </div>
    """
    #-----------------------------------------------------------------------------------------------------------------
    
    
    
    
#   -------------------------------------------------------------------------------------------------------------------------

    # add one Video related to IR -------------------------------------------------------------------
    if edit_video == "1":
        print"""
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="3" color="red" > Enter detials of the new Video:</font> </p>
                    </div>
                  </div>
    """
        print"""
                  <div class="form-group">
                    <label class="col-lg-4 control-label">URL*</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "text" name = "new_video_url">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Price*</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "number" name = "new_video_price"  min="0">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Type*</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "text" name = "new_video_type"  >
                    </div>
                  </div>
    
    
    """
    # -----------------------------------------------------------------------------------------------    

    
     
    # delelte Video related to IR
    if edit_video == "2":
        print"""
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="3" color="red" > Delete a Video of InstanceRun:</font> </p>
                    </div>
                  </div>
    """
        
    
        sql3 = """SELECT * FROM Video \
                    WHERE InstanceRunID=%s""" \
                        % (instance_run_num)
    
        cursor3 = db.cursor()
        cursor3.execute(sql3)
        video_row = cursor3.fetchone()

        
        
        print """
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Video URL*</label>
                    <div class="col-lg-5">
                        <select class="form-control" id="select" name="video_url_for_delete" >
        
    """
        while video_row is not None:
            print """
                             <option>%s</option>
            """ % (video_row[1])
            video_row = cursor3.fetchone()
    
        print""" 
                        </select>
                    </div>
                  </div>
                
        """

    
#   -------------------------------------------------------------------------------------------------------------------------

    # add Achievement realted to IR
    if edit_achievement == "1":
    

        print"""
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="3" color="red" > <b><u>Enter detials of the new Achievement: </u></b> </font>  </p>
                    </div>
                  </div>
    """
        
        print"""
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Date of Achievement*</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "date" name = "achievement_date">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Achievement Name</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "text" name = "achievement_name"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Reward*</label>
                    <div class="col-lg-5">
                      <input class="form-control" type = "text" name = "achievement_reward"  >
                    </div>
                  </div>

    """


    # delete Achievement realted to IR
    if edit_achievement == "2":
        print"""
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="3" color="red" > <b><u>Delete an Achievement of InstanceRun :</font> </p>
                    </div>
                  </div>
    """

        sql4 = """SELECT * FROM Achievement \
                    WHERE InstanceRunID = %s """ \
                        % (instance_run_num)
    
        cursor4 = db.cursor()
        cursor4.execute(sql4)
        achievement_row = cursor4.fetchone()
    
        
        print """
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Achievement Name</label>
                    <div class="col-lg-5">
                        <select class="form-control" id="select" name="achievement_for_delete" >
        
    """
        while achievement_row is not None:
            print """
                             <option>%s</option>
            """ % (achievement_row[3])
            achievement_row = cursor4.fetchone()
    
        print""" 
                        </select>
                    </div>
                  </div>
                
        """
    
    
    # submit button
    print """
              <fieldset>
                <div class="form-group">
                  <div class="col-lg-5 col-lg-offset-4">
                    <a class="btn btn-default" href="player_read.py" >Cancel</a> 
                    <button type="submit" class="btn btn-primary">Submit</button> 
                  </div>
                </div>
              </fieldset>
    
    """
    
    
#---------------------------------------------------------------------------------------------------------------
# Define main function.
def main():
    
    user_type = utility.header("Update Instance Run","player")
    
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn and user_type[1] != "S":
        print " You don't have access"
        utility.redirect("home.py")
    else:
        generate_form()
        
        

# Call main function.
main()
