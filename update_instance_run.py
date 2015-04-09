# Import the CGI module
import cgi,utility,session, MySQLdb

sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie


# Define function to generate HTML form.
def generate_form():
    
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
    
    print """

    <div class="row featurette" >
        <div class="well">
            <form class="bs-example form-horizontal" method=post action="update_instance_run2.py">  
            
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="White" > <b><i>Update Instance Run</i></b> </font> </p>
                    </div>
                  </div>
                </fieldset>
            

                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="4" color="red" > <b><u>Which Instance Run you want to update</u></b> </font> </p>
                    </div>
                  </div>
    """
    
#---------------------------------------------------------------------------------------------------------------
    # Select name of player
    print""" 
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Instance Run Name*</label>
                    <div class="col-lg-5">
                        <select class="form-control" id="select" name="instance_run_name" >
                            
    """

    sql = """select * from InstanceRun WHERE SupervisorID=%s """  % (sess.data["UserID"])
    
    InstanceRun_cursor= db.cursor()
    InstanceRun_cursor.execute(sql)
    
    
    InstanceRun_row = InstanceRun_cursor.fetchone()
    
    
    # get dropdown box for player name
    while InstanceRun_row is not None:
        print """
                         <option>%s</option>
        """ % (InstanceRun_row[2])
        InstanceRun_row = InstanceRun_cursor.fetchone()
    
    print""" 
                        </select>
                    </div>
                  </div>
                  
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Do you want to edit detials of Instance Run?*</label>
                    <div class="col-lg-5">
                      <input type="radio" name="edit_instance_run" value="0"> No <br>
                      <input type="radio" name="edit_instance_run" value="1"> Yes<br>
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Do you want to add or delete Player?*</label>
                    <div class="col-lg-5">
                      <input type="radio" name="edit_player" value="0"> No <br>
                      <input type="radio" name="edit_player" value="1"> Add <br>
                      <input type="radio" name="edit_player" value="2"> Delete <br>
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Do you want to add or delete Video?*</label>
                    <div class="col-lg-5">
                      <input type="radio" name="edit_video" value="0"> No <br>
                      <input type="radio" name="edit_video" value="1"> Add <br>
                      <input type="radio" name="edit_video" value="2"> Delete <br>
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Do you want to add or delete Achievement?*</label>
                    <div class="col-lg-5">
                      <input type="radio" name="edit_achievement" value="0"> No <br>
                      <input type="radio" name="edit_achievement" value="1"> Add <br>
                      <input type="radio" name="edit_achievement" value="2"> Delete <br>
                    </div>
                  </div>
    
    

    
              <fieldset>
                <div class="form-group">
                  <div class="col-lg-5 col-lg-offset-4">
                    <a class="btn btn-default" href="player_read.py" >Cancel</a> 
                    <button type="submit" class="btn btn-primary">Next</button> 
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
