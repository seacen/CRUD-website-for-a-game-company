# The libraries we'll need
import sys, cgi, session, utility

# ---------------------------------------------------------------------------------------------------------------------
sess = session.Session(expires=20*60, cookie_path='/')
alreadyLoggedOut = not sess.data.get('loggedIn')

if not alreadyLoggedOut:
    sess.data['loggedIn'] = 0 # log them out
    sess.data['userName'] = "None"
    sess.set_expires('') # expire session
    sess.close()


# ---------------------------------------------------------------------------------------------------------------------
# redirect to home page
utility.redirect("home.py")

