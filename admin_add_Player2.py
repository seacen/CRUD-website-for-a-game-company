# Import the CGI module
import cgi, MySQLdb,utility,session,sys

sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

# Define function to generate HTML form.
def generate_form(num_of_players):
    
    # connect to database
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)

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
            <form class="bs-example form-horizontal" method=post action="do_admin_add_Player.py">  
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="White" > <b><i>Details of new Players</i></b> </font> </p>
                    </div>
                  </div>
    """
    
#--------------------------------------------------------------------------------------------------------------------
# Player Numbers from last page
    
    print"""
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Number of new Players*</label>
                    <div class="col-lg-5">

                      <input  class="form-control"  id="disabledInput" type="number" name=""  value="{0}" disabled="" >
                      <input type = "hidden" name = "num_of_players"  value="{0}">
                    </div>
                  </div>
    """ .format(num_of_players)



    
    
#---------------------------------------------------------------------------------------------------------------
# Details of new Players to enter

#---------------------------------------------------------------------------------------------------------------
    

    print"""
            <hr>
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-8">
                  <p> <font size="6" color="White" > <b><i>Enter detals for each Player</i></b> </font> </p>
                    </div>
                  </div>
                </fieldset>

    """
   

#---------------------------------------------------------------------------------------------------------------
    # Select name of player
    for i in range(1, num_of_players+1):
        
        
        print""" 

                  <div class="form-group">
                    <div class="col-lg-4">
                  <p> <font size="6" color="Red" > <center><b>Player{0}</b></center> </font> </p>
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Supervisor Name*</label>
                    <div class="col-lg-5">
                        <select class="form-control" id="select" name="supervisor_name{0}">
                            
        """ .format(i)
        
    
        player_cursor.execute("select * from Player WHERE PlayerType='S'")
        player_row = player_cursor.fetchone()
        # get dropdown box for player name
        while player_row is not None:
            print """
                             <option>%s</option>
            """ % (player_row[2])
            player_row = player_cursor.fetchone()

        
        print""" 
                      </select>
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Fisrt Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="player_first_name{0}"  >
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-lg-4 control-label">Last Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="player_last_name{0}"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Role*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="player_role{0}"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Type*</label>
                    <div class="col-lg-5">
        
                      <input type="radio" name="player_type{0}" value="N"> Normal Player<br>
                      <input type="radio" name="player_type{0}" value="S"> Normal Player & Supervisor </div>
                  </div>

                  <div class="form-group">
                    <label class="col-lg-4 control-label">Email*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="email" name="player_email{0}"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">GameHandle*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="player_gamehandle{0}"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">VoiP*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="player_voip{0}"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Phone</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="player_phone{0}"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Profile Description</label>
                    <div class="col-lg-5">
                      <textarea name="profile_description{0}" cols="40" rows="4" id="ddd"></textarea>
                    </div>
                  </div>
        
                <hr>

        """.format(i)

        
        
    print""" 
          <fieldset>
            <div class="form-group">
              <div class="col-lg-5 col-lg-offset-4">
                <a class="btn btn-default" href="admin_add_player.py" >Cancel</a> 
                <button type="submit" class="btn btn-primary">Next</button> 
              </div>
           </div>
          </fieldset>

    """



    db.close()


#----------------------------------------------------------------------------------------------------------------
def main():
    
    usertype = utility.header("New adding Players","")
    if usertype != "A":
        utility.redirect("login.py")
    else:
    
        # Define main function.
        form = cgi.FieldStorage()

        try:
             num_of_players = (int) (form.getvalue("num_of_new_players"))  
        except: 
             utility.redirect("admin_add_Player.py") 
             sys.exit(0)                  
                          
        generate_form(num_of_players )

        
# call main function        
main()    
    
