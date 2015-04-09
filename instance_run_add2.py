# Import the CGI module
import cgi,utility,session,MySQLdb


sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------

# Define function to generate HTML form.
def generate_form(game_name, name, category, date, 
                  num_of_players, num_of_videos, num_of_achievements, notes):
    

    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)


    
    # get Game table
    game_cursor = db.cursor()
    player_cursor = db.cursor()
    count_player_cursor = db.cursor()
    
    
    game_cursor.execute("select * from Game ORDER BY GameID")
    player_cursor.execute("select * from Player")
    count_player_cursor.execute("SELECT COUNT(*) FROM Player")
    
    
    game_row = game_cursor.fetchone()
    player_row =  player_cursor.fetchone()
    max_player = count_player_cursor.fetchone()[0]

    
    print """
    
    <div class="row featurette" >
        <div class="well">
            <form class="bs-example form-horizontal" method=post action="do_instance_run_add.py">  
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="White" > <b><i>Details of Instance Run</i></b> </font> </p>
                    </div>
                  </div>
    """
    
#--------------------------------------------------------------------------------------------------------------------
# Numbers from last page
    
    print"""
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Number of Attended Players*</label>
                    <div class="col-lg-5">

                      <input  class="form-control"  id="disabledInput" type="number" name=""  value="{0}" disabled="" >
                      <input type = "hidden" name = "num_of_players"  value="{0}">
                    </div>
                  </div>
    """ .format(num_of_players, max_player )

    print"""
                  <div class="form-group">
                    <label class="col-lg-4 control-label">No. of Videos to Upload*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" id="disabledInput" type="number" name="" value="{0}" disabled="">
                      <input type = "hidden" name = "num_of_videos"  value="{0}"> 
                    </div>
                  </div>
    
    """ .format(num_of_videos)
    
    print"""
                  <div class="form-group">
                    <label class="col-lg-4 control-label">No. of Achievements*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" id="disabledInput" type="number" name="" value="{0}" disabled="">
                      <input type = "hidden" name = "num_of_achievements"  value="{0}"> 
                    </div>
                  </div>
    
                </fieldset>
    """ .format(num_of_achievements)
       
#--------------------------------------------------------------------------------------------------------------------    
    
    
    print"""
               <hr>


                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="4" color="red" > <b><u>Please fill all fields with *</u></b> </font> </p>
                    </div>
                  </div>
                </fieldset>
    


                <fieldset>
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Instance Run Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="name" >
                    </div>
                  </div>
                </fieldset>
    
                  <div class="form-group">
                    <label for="select" class="col-lg-4 control-label">Category*</label>
                    <div class="col-lg-5">
                        <select name="category" class="form-control" id="select">
                        <option value="casual" selected>Casual</option>
                        <option value="tournament">Tournament</option>
                        </select>
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label for="ddd" class="col-lg-4 control-label">Date Recorded*</label>
                    <div class="col-lg-5">
                      <input type="date" name="date" id="ddd" min="2014-01-01"  max="2100-01-01" > 
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Performance Notes</label>
                    <div class="col-lg-5">
                      <textarea name="notes" cols="40" rows="4" id="ddd"></textarea>
                    </div>
                  </div>
    
    """    
    
    
    

    
    

    
    
    
    
    
#---------------------------------------------------------------------------------------------------------------
    
  
    print"""
            <hr>
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-8">
                  <p> <font size="5" color="White" > <b><i>Enter first name of each Player</i></b> </font> </p>
                    </div>
                  </div>
                </fieldset>
    
    
    """
   
    
    # Select name of player
    for i in range(1, num_of_players+1):
        
        
        print""" 

                  <div class="form-group">
                    <label class="col-lg-3 control-label">Player {0} - First Name*</label>
                    <div class="col-lg-5">
                        <select class="form-control" id="select" name="player_name{0}">
                            
        """ .format(i)
        
        player_cursor.execute("select * from Player")
        player_row = player_cursor.fetchone()
        # get dropdown box for player name
        while player_row is not None:
            print """
                             <option>%s</option>
            """ % (player_row[2])
            player_row = player_cursor.fetchone()

        print """
                      </select>
                    </div>
                  </div>
        """


    
    
#---------------------------------------------------------------------------------------------------------------
    
    # Head for Video
    print """
            <hr>
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-8">
                  <p> <font size="5" color="White" > <b><i>Enter Details for each Video</i></b> </font> </p>
                    </div>
                  </div>
                </fieldset>    
    """
    
    
    # Enter details for each Video
    # and which Game is contained in the Video
    for i in range(1, num_of_videos+1):
        
        game_cursor.execute("select * from Game ORDER BY GameID")

        game_row = game_cursor.fetchone()

        print """
        
                  <div class="form-group">
                    <label class="col-lg-3 control-label">Game Name*</label>
                    <div class="col-lg-5">
    
                        <select class="form-control" id="select" name="game_name%s">
                            
        """ % (i)
    
        # get dropdown box for Game
        while game_row is not None:
            print """
                             <option>%s</option>
            """ % (game_row[1])
            game_row = game_cursor.fetchone()

        print """
                      </select>
                    </div>
                  </div>
        """
    
    
        print"""
                  <div class="form-group">
                    <label class="col-lg-3 control-label">Video {0} - URL*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="video_url{0}"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-3 control-label">Video {0} - Price</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="video_price{0}" min="0" max="999"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-3 control-label">Video {0} - Type</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="video_type{0}"  >
                    </div>
                  </div>
            <hr>
        """.format(i)

    
#---------------------------------------------------------------------------------------------------------------
    # Head for Achievement    
    print """
        
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-8">
                  <p> <font size="5" color="White" > <b><i>Enter Details for each Achievement</i></b> </font> </p>
                    </div>
                  </div>
                </fieldset>

    """
    
    # Enter for each Achievement
    for i in range(1, num_of_achievements+1):
        print """
                  <div class="form-group">
                    <label class="col-lg-3 control-label">Achievement {0} - Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="achievement_name{0}"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-3 control-label">Achievement {0} - Reward*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="achievement_reward{0}"  >
                    </div>
                  </div>
            <hr>
        """.format(i)
    
    

    print """
              <fieldset>
                <div class="form-group">
                  <div class="col-lg-3 col-lg-offset-3">

                    <a class="btn btn-default" href="upload_instance_run.py">Cancel</a> 
                    <button type="submit" class="btn btn-primary">Submit</button> 
                  </div>
                </div>
              </fieldset>
    
        </form>
    
      </div>
    </div>
</html>
    
"""
    db.close()


# Define main function.
def main():
    
    # get user type
    usertype = utility.header("Upload Instance Run","")
    
    
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn or sess.data.get("PlayerType")!="S":    
        utility.redirect("login.py")
        
    else:
        form = cgi.FieldStorage()
        game_name = form.getvalue("game_name")
        name = form.getvalue("name")    
        category = form.getvalue("category")
        
        date = form.getvalue("date")
        
        num_of_players = (int) (form.getvalue("num_of_players"))    
        num_of_videos = (int)(form.getvalue("num_of_videos"))
        num_of_achievements = (int)(form.getvalue("num_of_achievements"))
        
        notes = form.getvalue("notes")
        
        
        generate_form(game_name, name, category, date,
                  num_of_players, num_of_videos, num_of_achievements, notes)

# Call main function.
main()






