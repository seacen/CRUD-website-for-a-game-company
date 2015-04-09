# Import the CGI module
import cgi,utility,session, MySQLdb

sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

# Define function to generate HTMLorm.
def generate_form():
    
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    

    player_cursor = db.cursor()
    player_cursor.execute("SELECT COUNT(*) FROM Player")
    
    
    
    print """

    <div class="row featurette" >
        <div class="well">
            <form class="bs-example form-horizontal" method=post action="instance_run_add2.py">  
            
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="White" > <b><i>Upload New Instance Run</i></b> </font> </p>
                    </div>
                  </div>
                </fieldset>
            
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="4" color="red" > <b><u>Please fill all fields with numbers</u></b> </font> </p>
                    </div>
                  </div>
                </fieldset>

    """
    
    # total number of players
    max_player = player_cursor.fetchone()[0]
    
    
    print"""
                  <div class="form-group">
                    <label class="col-lg-4 control-label">No. of Attended Players*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="num_of_players" min="01" max="%s" >
                    </div>
                  </div>
    """ % (max_player)
    

    
    print"""
                  <div class="form-group">
                    <label class="col-lg-4 control-label">No. of new Videos to Upload*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="num_of_videos" min="01" max="32" >
                    </div>
                  </div>
    
                
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">No. of new Achievements*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="num_of_achievements" min="01" max="32" >
                    </div>
                  </div>

              </fieldset>
    
    
              <fieldset>
                <div class="form-group">
                  <div class="col-lg-5 col-lg-offset-4">
                    <a class="btn btn-default" href="player_read.py" >Cancel</a> 
                    <button type="submit" class="btn btn-primary">Next</button> 
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
    
    utility.header("Upload Instance Run","player")
    
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn or sess.data.get("PlayerType")!="S":    
        utility.redirect("login.py")
    else:
        generate_form()
        
        

# Call main function.
main()









