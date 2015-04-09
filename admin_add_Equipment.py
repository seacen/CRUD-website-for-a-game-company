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
            <form class="bs-example form-horizontal" method=post action="do_admin_add_Equipment.py">  
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="red" > <b><i>Details of new Equipment</i></b> </font> </p>
                    </div>
                  </div>

                    <hr>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Model and make</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="ModelAndMake"  >
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-lg-4 control-label">Review</label>
                    <div class="col-lg-5">
                      <textarea class="form-control" rows="3" name="EquipmentReview"></textarea>
                    </div>
                  </div>
        

                  <div class="form-group">
                    <label class="col-lg-4 control-label">Processor speed</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="ProcessorSpeed"  >
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
    usertype = utility.header("new equipment","")
    if usertype != "A":
        utility.redirect("login.py") 
    else:       
        generate_form()

        
        
main()    
    