# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb, utility, datetime
from datetime import date

sess = session.Session(expires=20*60, cookie_path='/')
# --------------------------------------------------------------------------------------------------------------------
# send session cookie
# --------------------------------------------------------------------------------------------------------------------

def generate_form():

    
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
    today = datetime.date.today()
    
    print """

    <div class="row featurette" >
        <div class="well">
            <form class="bs-example form-horizontal" method=post action="do_viewer_register.py">  
            
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="White" > <b><i>New Viewer Sign Up</i></b> </font> </p>
                    </div>
                  </div>
                </fieldset>
            
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="4" color="red" > <b><u>Please fill all fields with *</u></b> </font> </p>
                    </div>
                  </div>
                </fieldset>

                  <div class="form-group">
                    <label class="col-lg-5 control-label">ACCOUNT*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="account"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">PASSWORD*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="password" name="password"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label for="ddd" class="col-lg-5 control-label">Date of Birth</label>
                    <div class="col-lg-5">
                      <input type="date" name="date" id="ddd" min="1900-01-01"  max="%s" > 
                    </div>
                  </div>
    """ %(today)

    print """
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Email</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="email" name="email"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Type*</label>
                    <div class="col-lg-5">
                      <input type="radio" name="viewer_type" value="P"> Premium<br>
                      <input type="radio" name="viewer_type" value="C"> Crowd Funding
                    </div>
                  </div>
    
    
    """
    
#--------------------------------------------------------------------------------------------------------------------

    print """
                 <div class="form-group">
                    <label for="Street_num" class="col-lg-5 control-label">Street No.*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="Street_num"  min ="0">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_num_suffix" class="col-lg-5 control-label">Street No.Suffix</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_num_suffix" >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_name" class="col-lg-5 control-label">Street Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_name" >
                    </div>
                  </div>
    
    
                 <div class="form-group">
                    <label for="Street_type" class="col-lg-5 control-label">Street Type*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_type" >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Address_type" class="col-lg-5 control-label">Address Type</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Address_type" >
                    </div>
                  </div>    
    
                 <div class="form-group">
                    <label for="Address_type" class="col-lg-5 control-label">Address Type Identifier</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Address_type-identifier" >
                    </div>
                  </div>   

                 <div class="form-group">
                    <label for="Minor" class="col-lg-5 control-label">MinorMunicipality</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Minor"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Major" class="col-lg-5 control-label">MajorMunicipality*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Major" >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="District" class="col-lg-5 control-label">GoverningDistrict*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="District"  >
                    </div>
                  </div>

                 <div class="form-group">
                    <label for="Post" class="col-lg-5 control-label">Postcode*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="Post" min="0" max="9999">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Country" class="col-lg-5 control-label">Country*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Country" >
                    </div>
                  </div>
    
    
                  <div class="form-group">
                    <div class="col-lg-5 col-lg-offset-5">
                      <a href = "home.py" class="btn btn-default">Cancel</a> 
                      <button type="submit" class="btn btn-primary">Submit</button> 
                    </div>
                  </div>

    """
# ----------------------------------------------------------------------------------------------------------------------------------
# Addition details for crowd funding viewer
    print """
                <hr>
    
                  <div class="form-group">
                    <div class="col-lg-8">
                  <p> <font size="4" color="red" > <u>ENTER FIELDS ONLY IF YOU ARE CROWD FUNDING VIEWER ( OPTIONAL )<br></u> </font> </p>
                    </div>
                  </div>


                  <div class="form-group">
                    <label class="col-lg-5 control-label">Total Amount Donated +</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="donation" min="0"  >
                    </div>
                  </div>
    
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">First Name +</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="d_first_name"  >
                    </div>
                  </div>
    
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Last Name +</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="d_last_name"  >
                    </div>
                  </div>
    
                <hr>
    
    """

    
    
    
    
    
# Define main function.
def main():
    
    utility.header("Sign up","")
    

    generate_form()
    
    
    
main()