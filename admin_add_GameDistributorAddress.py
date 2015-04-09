import utility, sys

# check user identity
usertype = utility.header("Administration","") 
if usertype != 'A':
    utility.redirect("login.py")
    sys.exit(0)

print """
        <div class="row featurette" >
        <div class="well">
                      
             <fieldset>
                  <div class="form-group">
                    <div class="col-lg-8">
                  <p> <font size="6" color="White" > <b><i>Add new Game Distributor Address</i></b> </font> </p>
                    </div>
                  </div>
                      
                  <div class="form-group">
                    <div class="col-lg-6">
                        <p> <font size="4" color="red" > <b><u>Please fill all fields with *</u></b> </font> </p>
                    </div>
                  </div>
                      
                </fieldset>
                      
            <form class="bs-example form-horizontal" method=post action="do_admin_add_GameDistributorAddress.py">  
                      
                  <div class="form-group">
                    <label for="Street_num" class="col-lg-5 control-label">GameDistributor ID*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="GameDistributorID"  min ="1">
                    </div>
                  </div>

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
                     
            </div>
            </div>

    """