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
            <form class="bs-example form-horizontal" method=post action="admin_add_Player2.py">  
            
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="White" > <b><i>Add new Players</i></b> </font> </p>
                    </div>
                  </div>
                </fieldset>
            

                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="4" color="red" > <b><u>Give the number of Players you want to add</u></b> </font> </p>
                    </div>
                  </div>

    
                  <div class="form-group">
                    <label class="col-lg-4 control-label">No. of new Players*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="num_of_new_players" min="01" max="32" >
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
    
    
    
    
    
# Define main function.
def main():
    # print web header
    utility.header("Add new Players","")
    # check user identity
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn or sess.data.get("UserType")!="A":    
        utility.redirect("login.py")
    else:
        generate_form()
        
        

# Call main function.
main()



    
