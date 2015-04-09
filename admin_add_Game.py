# Import the CGI module
import cgi, MySQLdb,utility,session,sys

sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

# Define function to generate HTML form.
def generate_form():
    
    print """
    
    <div class="row featurette" >
        <div class="well">
            <form class="bs-example form-horizontal" method=post action="do_admin_add_Game.py">  
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="red" > <b><i>Details of new Game</i></b> </font> </p>
                    </div>
                  </div>

                    <hr>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Game Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="game_name"  >
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-lg-4 control-label">Genre*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="genre"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Review</label>
                    <div class="col-lg-5">
                      <textarea class="form-control" rows="3" name="review"></textarea>
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Star rating*</label>
                    <div class="col-lg-5">
                        <select class="form-control" id="select" name="star">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        </select>
                  </div>
                  </div>

                  <div class="form-group">
                    <label class="col-lg-4 control-label">Classification rating*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="classification"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Platform notes</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="platform"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Promotion link</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="link"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Cost*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" min=0 name="cost"  >
                    </div>
                  </div>
        
             

                <fieldset>
                    <div class="form-group">
                      <div class="col-lg-5 col-lg-offset-4">
                        <a class="btn btn-default" href="admin_home.py" >Cancel</a> 
                    <button type="submit" class="btn btn-primary">Submit</button> 
                  </div>
               </div>
              </fieldset>
    
    """



#----------------------------------------------------------------------------------------------------------------
def main():
    # check if it is administrator
    usertype = utility.header("new game","")
    if usertype != "A":
        utility.redirect("login.py") 
    else:       
        generate_form()

        
        
main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    