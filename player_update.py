# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb, utility

sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie
# ---------------------------------------------------------------------------------------------------------------------

# Define function to generate HTML form.
def generate_form(Gamehandle, Email, Phone, Voip, 
                  Street_num, Street_num_suffix, 
                  Street_name, Street_type, Address_type, 
                  Minor, Major, District, Post, Country):
    

    form = cgi.FieldStorage()
    
    print """

    <form method=post action="do_player_update.py">
    

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
    

    
                <fieldset>
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Gamehandle*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Gamehandle" value=  "{0}"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Email*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="email" name="Email" value=         "{1}"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Phone</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Phone" value=         "{2}"  >
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-5 control-label">Voip*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Voip" value=         "{3}"  >
                    </div>
                  </div>
                
                </fieldset>
    
                <fieldset>
                </fieldset>
    
                <fieldset>

                 <div class="form-group">
                    <label for="Address_type" class="col-lg-5 control-label">Address Type*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Address_type" value=         "{4}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_num" class="col-lg-5 control-label">Street No.*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="number" name="Street_num" value=         "{5}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_num_suffix" class="col-lg-5 control-label">Street No.Suffix</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_num_suffix" value=         "{6}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Street_name" class="col-lg-5 control-label">Street Name*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_name" value=         "{7}"  >
                    </div>
                  </div>
    
    
                 <div class="form-group">
                    <label for="Street_type" class="col-lg-5 control-label">Street Type*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Street_type" value=         "{8}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Minor" class="col-lg-5 control-label">MinorMunicipality</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Minor" value=         "{9}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Major" class="col-lg-5 control-label">MajorMunicipality*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Major" value=         "{10}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="District" class="col-lg-5 control-label">GoverningDistrict*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="District" value=         "{11}"  >
                    </div>
                  </div>

                 <div class="form-group">
                    <label for="Post" class="col-lg-5 control-label">Postcode*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Post" value=         "{12}"  >
                    </div>
                  </div>
    
                 <div class="form-group">
                    <label for="Country" class="col-lg-5 control-label">Country*</label>
                    <div class="col-lg-5">
                      <input  class="form-control" type="text" name="Country" value=         "{13}"  >
                    </div>
                  </div>

    
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

""".format(Gamehandle, Email, Phone, Voip, 
           Address_type,
           Street_num, Street_num_suffix,
           Street_name, Street_type, Minor,
           Major, District, Post, Country)



# Define main function.
def main():
    
    user_type = utility.header("Update Profile","player")
    
    
    
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn or info.get("UserType") == 'V':    
        utility.redirect("home.py")
        
    else:

        
        db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
        latest_address_cursor = db.cursor()
        current_address_cursor= db.cursor()
        
    
        
        sql1 = "select PlayerID, AddressID, StartDate, EndDate \
                   from PlayerAddress \
                where PlayerID = %s and EndDate is null" \
                       % (sess.data["UserID"])
    
    
        latest_address_cursor.execute(sql1)
        latest_address_row = latest_address_cursor.fetchone()
    
    
        sql2 = "select * from PlayerAddress \
                    inner join Player On Player.PlayerID = PlayerAddress.PlayerID \
                    inner join Address on Address.AddressID = PlayerAddress.AddressID \
                        where PlayerAddress.PlayerID = %s \
                            and PlayerAddress.AddressID = %s " \
                                % (latest_address_row[0], latest_address_row[1] )
        
    
        current_address_cursor.execute(sql2)
        current_address_row = current_address_cursor.fetchone()
    
        
    
        Gamehandle = to_null(current_address_row[12])
        Email = to_null(current_address_row[11])
        Phone = to_null(current_address_row[13])
        Voip = to_null(current_address_row[14])          
    
        Street_num = to_null(current_address_row[16])    
        Street_num_suffix = to_null(current_address_row[17]) 
        Street_name = to_null(current_address_row[18]) 
        Street_type = to_null(current_address_row[19]) 
        Address_type = to_null(current_address_row[20]) 
        Minor = to_null(current_address_row[22])
        Major = to_null(current_address_row[23])
        District = to_null(current_address_row[24])
        Post = to_null(current_address_row[25]) 
        Country = to_null(current_address_row[26])
    

        # close after use
        db.close()

    
        generate_form(Gamehandle, Email, Phone, Voip, 
                  Street_num, Street_num_suffix, 
                  Street_name, Street_type, Address_type, 
                  Minor, Major, District, Post, Country)
        


        
def to_null(value):
    if value is None:
        return ''
    else:
        return value    
    
    
    
# Call main function.
main()