# The libraries we'll need
import sys, cgi, redirect, session,utility

# Get the session and check if logged in
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

# ---------------------------------------------------------------------------------------------------------------------

# debug - what's in the session
#print(sess.data)
#sys.exit()

if loggedIn:
    
    utility.redirect("home.py")

else:
    utility.header("Login","home")
    
    print"""
    <div class="container marketing">
    <div class="row featurette" >
            <div class="well">
              <form class="bs-example form-horizontal" method="post" action="do_login.py">
    
                <fieldset>
                  <div class="form-group">
                    <div class="col-lg-5" col-lg-offset-5">
                  <p> <font size="4" color="red" > <b><u>Login</u></b> </font> </p>
                  <p>{0}</p>
                    </div>
                  </div>
                </fieldset>
    

    
                <fieldset>
    
                  <div class="form-group">
                    <label class="col-lg-3 control-label">Username</label>
                    <div class="col-lg-3">
                      <input  class="form-control" type="text" name="username">
                    </div>
                  </div>
    
                  <div class="form-group">
                    <label class="col-lg-3 control-label">Password</label>
                    <div class="col-lg-3">
                      <input  class="form-control" type="password" name="password">
                    </div>
                  </div>
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
    </div>
    </form>
    </html>
    """.format("Your username or password was entered incorrectly" if sess.data.get('failedAtt') else '')
    
if sess.data.get('failedAtt'):
    sess.data['failedAtt']=0