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
            <form class="bs-example form-horizontal" method=post action="do_admin_add_GameDistributor.py">  
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="red" > <b><i>Details of new Game Distributor</i></b> </font> </p>
                    </div>
                  </div>

                    <hr>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Company Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="CompanyName"  >
                    </div>
                  </div>

                  <div class="form-group">
                    <label class="col-lg-4 control-label">Contract First Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="ContactFirstName"  >
                    </div>
                  </div>
        
                  <div class="form-group">
                    <label class="col-lg-4 control-label">Contract Last Name</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="ContactLastName"  >
                    </div>
                  </div>
        

                  <div class="form-group">
                    <label class="col-lg-4 control-label">Phone*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="Phone"  >
                    </div>
                  </div>
                </fieldset>
    
             
                  


                 <fieldset>
    
                 <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="6" color="red" > <b><i>Address of new game distributor</i></b> </font> </p>
                    </div>
                  </div>

                   <hr>
    
                 <div class="form-group">
                    <label for="Address_type" class="col-lg-5 control-label">Address Type*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="AddressType">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_num" class="col-lg-5 control-label">Street No.*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="StreetNumber">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_num_suffix" class="col-lg-5 control-label">Street No.Suffix</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="StreetNumberSuffix">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_name" class="col-lg-5 control-label">Street Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="StreetName">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="AddressTypeIdentifier" class="col-lg-5 control-label">AddressTypeIdentifier*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="AddressTypeIdentifier">
                    </div>
                  </div>
    
    
                 <div class="form-group">
                    <label for="Street_type" class="col-lg-5 control-label">Street Type*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="StreetType">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Minor" class="col-lg-5 control-label">MinorMunicipality</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="MinorMunicipality">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Major" class="col-lg-5 control-label">MajorMunicipality*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="MajorMunicipality">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="District" class="col-lg-5 control-label">GoverningDistrict*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="GoverningDistrict">
                    </div>
                  </div>

                 <div class="form-group">
                    <label for="Post" class="col-lg-5 control-label">Postcode*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="PostalArea">
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Country" class="col-lg-5 control-label">Country*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Country">
                    </div>
                  </div>

    
                </fieldset>
             

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
    
    usertype = utility.header("new game distributor","")
    if usertype != "A":
        utility.redirect("login.py") 
    else:       
        generate_form()

        
        
main()  