# Import the CGI moduleWork
import cgi, MySQLdb,utility,session,sys


sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

info=sess.data
loggedIn = info.get("loggedIn")

# check user identity
if not loggedIn or sess.data.get("UserType")!="A":    
    utility.redirect("login.py")
    sys.exit(0)
          
    
utility.header("Adding new Players","")
    
form = cgi.FieldStorage()
    
# connect to db
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)  

    
# get all attribute values
name = form.getvalue("game_name")
genre = form.getvalue("genre")
review = form.getvalue("review")
star = form.getvalue("star")
classification = form.getvalue("classification")
platform = form.getvalue("platform")
link = form.getvalue("link")
cost = form.getvalue("cost")

    
sql = "insert into Game(GameID,GameName,Genre,Review,StarRating,ClassificationRating,PlatformNotes,PromotionLink,Cost) \
            values (DEFAULT,  '{0}',   '{1}',   '{2}', {3}, '{4}', '{5}', '{6}', {7})"    \
                .format(name,genre,review,star,classification,platform,link,cost)

    
cursor = db.cursor()

try:
    cursor.execute(sql)
    db.commit()
    info['adminMSG']="new game has been created successfully!"
    
except:
    db.rollback()
    info['adminMSG']="Failed to create the new game, please fill in all compulsory fields."

# go back to admin home page
utility.redirect("admin_home.py")


