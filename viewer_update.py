# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb, utility

sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie
# ---------------------------------------------------------------------------------------------------------------------

# Define function to generate HTML form.
def generate_form(viewer_type,
                  dob, Email,
                  first_name,  last_name, donation,
                  Street_num, Street_num_suffix,
                  Street_name, Street_type,
                  Address_type,Address_type_identifier,
                  Minor, Major, District, Post, Country):
    
    
    

    form = cgi.FieldStorage()
    
    if (viewer_type=="VC"):
        type_name = "Crowd Funding Viewer"
    if (viewer_type=="VP"):
        type_name = "Premium Viewer"
    
    print """

    <form method=post action="do_viewer_update.py">
    

    <div class="row featurette" >
            <div class="well">
              <form class="bs-example form-horizontal" >
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-6">
                  <p> <font size="8" color="White" > <b><i>Profile</i></b> </font> </p>
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
    
    """
    
    
    print """
    
    
                <fieldset>
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Viewer Account Type</label>
                    <div class="col-lg-5">

                      <input  class="form-control"  id="disabledInput" type="text" value="{0}" disabled="" >
                      <input type = "hidden" name = "viewer_type"  value="{1}">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Date of birth</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="date" name="dob" value="{2}" >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Email</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="email" value="{3}" >
                    </div>
                  </div>
                </fieldset>
    """.format(type_name, viewer_type, dob, Email)
    
    
    
    # -----------------------------------------------------------------------------------
    #  CrowdFundingViewer 
    if (viewer_type=="VC"):
        
        print """
                <fieldset>
                  <div class="form-group">
                    <label class="col-lg-5 control-label">First Name</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="first_name" value= "%s" >
                    </div>
                  </div>

    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Last Name</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="last_name" value= "%s" >
                    </div>
                  </div>
                </fieldset>
    """ %(first_name, last_name)
    


    
    # address details
    print """
                <fieldset>
                 <div class="form-group">
                    <label for="Address_type" class="col-lg-5 control-label">Address Type*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Address_type" value=         "{0}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_num" class="col-lg-5 control-label">Street No.*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="Street_num" min="0" value=         "{1}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_num_suffix" class="col-lg-5 control-label">Street No.Suffix</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_num_suffix" value=         "{2}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_name" class="col-lg-5 control-label">Street Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_name" value=         "{3}"  >
                    </div>
                  </div>
    
    
                 <div class="form-group">
                    <label for="Street_type" class="col-lg-5 control-label">Street Type*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_type" value=         "{4}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Minor" class="col-lg-5 control-label">Address Type Identifier</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Address_type_identifier" value=    "{5}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Minor" class="col-lg-5 control-label">MinorMunicipality</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Minor" value=         "{6}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Major" class="col-lg-5 control-label">MajorMunicipality*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Major" value=         "{7}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="District" class="col-lg-5 control-label">GoverningDistrict*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="District" value=         "{8}"  >
                    </div>
                  </div>

                 <div class="form-group">
                    <label for="Post" class="col-lg-5 control-label">Postcode*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Post" value=         "{9}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Country" class="col-lg-5 control-label">Country*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Country" value=         "{10}"  >
                    </div>
                  </div>
    """.format(Address_type,
               Street_num, Street_num_suffix,
               Street_name, Street_type,
               Address_type_identifier,
               Minor, Major, District, Post, Country)
    
    
    print """
    
                </fieldset>
                
                <fieldset>
                </fieldset>
                
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-5 col-lg-offset-5">
                      <button class="btn btn-default">Cancel</button> 
                      <button type="submit" class="btn btn-primary">Submit</button> 
                    </div>
                  </div>
                </fieldset>
    
              </form>
            </div>
    </div>
    </form>
    </html>

"""



# Define main function.
def main():
    
    viewer_type = utility.header("Update Profile","")
    
    
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn or info.get("UserType") != 'V':    
        utility.redirect("home.py")
    
    
    
    
    else:

        
        db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
        
        
        
        vc_cursor = db.cursor()
        vp_cursor = db.cursor()
        
        
        first_name = ""
        last_name = ""
        donation = ""
        renew_date = ""
        
        
        # get detail of CrowdFundingViewer 
        if ( viewer_type == "VC" ) :
            
            sql = "select * from CrowdFundingViewer \
                       where ViewerID = %s" \
                        % ( sess.data["UserID"])
            
            vc_cursor.execute(sql)
            detail_row = vc_cursor.fetchone()
            
            first_name = detail_row[1]
            last_name =  detail_row[2]
            donation =   detail_row[3]
        
        
        # get detail of PremiumViewer 
        if ( viewer_type == "VP" ) :
            
            sql = "select * from PremiumViewer \
                       where ViewerID = %s" \
                        % ( sess.data["UserID"])
            
            vp_cursor.execute(sql)
            detail_row = vp_cursor.fetchone()
            
            renew_date = detail_row[1]
            

        # get latest address id ---------------------------------
        sql1 = "select ViewerID, AddressID, StartDate, EndDate  \
                   from ViewerAddress \
                where ViewerID = %s and EndDate is null" \
                       % (sess.data["UserID"])
    
        latest_address_cursor = db.cursor()
        latest_address_cursor.execute(sql1)
        latest_address_row = latest_address_cursor.fetchone()
        # --------------------------------------------------------

        # get current address ----------------------------------------------------------
        sql2 = "select * from ViewerAddress \
                    inner join Viewer On Viewer.ViewerID = ViewerAddress.ViewerID \
                    inner join Address on Address.AddressID = ViewerAddress.AddressID \
                        where ViewerAddress.ViewerID = %s \
                            and ViewerAddress.AddressID = %s " \
                                % (latest_address_row[0], latest_address_row[1] )
        
        current_address_cursor= db.cursor()
        current_address_cursor.execute(sql2)
        current_address_row = current_address_cursor.fetchone()
        # ------------------------------------------------------------------------------


        dob = to_null(current_address_row[6])
        Email = to_null(current_address_row[7])
    
        Street_num = to_null(current_address_row[9])    
        Street_num_suffix = to_null(current_address_row[10]) 
            
        Street_name = current_address_row[11]
        Street_type = current_address_row[12]
        Address_type = current_address_row[13]
        Address_type_identifier = to_null(current_address_row[14])
            
        Minor = to_null(current_address_row[15])
        Major = current_address_row[16]
        District = current_address_row[17]
        Post = current_address_row[18]
        Country = current_address_row[19]
    

        # close after use
        db.close()

    
        generate_form(viewer_type,
                      dob, Email, 
                      first_name,  last_name, donation,
                      Street_num, Street_num_suffix,
                      Street_name, Street_type,
                      Address_type,Address_type_identifier,
                      Minor, Major, District, Post, Country)
        


# ----------------------------------------------------------------------------------------        
def to_null(value):
    if value is None:
        return ''
    else:
        return value    
    
    
    
# Call main function.
main()