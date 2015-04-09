# Import the CGI module
import cgi, MySQLdb,utility,session,sys


sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

info=sess.data
loggedIn = info.get("loggedIn")

if not loggedIn or sess.data.get("UserType")!="A":    
    utility.redirect("login.py")
    sys.exit(0)

result=0




#----------------------------------------------------------------------------------------------------------------

def extract_results(num_of_players, sn, fn, ln, r, t, email, gh, v):
    
    for i in range(0,num_of_players):
        
        if sn[i] is None or fn[i] is None or ln[i] is None or r[i] is None or t[i] is None or email[i] is None or gh[i] is None or v[i] is None:
            result = False
        else:
            result = True 
    
    return result




#----------------------------------------------------------------------------------------------------------------

def display_success(result,num_of_players ):
    
    if result == True:
        s1 = "successful!"
        s2 = "href = admin_home.py"
        s3 = "Click here to return to ADMIN HOMEPAGE."
        
    else:
        s1 = "unsuccessful!\n Please fill all fileds with * "         
        s2 = ""
        s3 = "Press BACKSPACE to try again."
        
    
    
    print """
    <h2>Adding %s new Players was %s</h2>
    <a %s>%s</a>
</body>

</html>
""" %(num_of_players, s1, s2, s3  )




#----------------------------------------------------------------------------------------------------------------

def get_supervisor_id(db, supervisor_name):
    
    cursor = db.cursor()
    
    sql = "SELECT * FROM Player \
                WHERE PlayerFirstName = '%s'" \
                    % (supervisor_name)
    
    cursor.execute(sql)
    s_id= cursor.fetchone()[0]

    return s_id





# ---------------------------------------------------------------------------------------------------------------------
# creat new account for new player and return UserAccountID 
def insert_user(db, fn, ln):
    
    cursor = db.cursor()
    id_cursor = db.cursor()
    
    sql = "INSERT INTO UserAccount(UserAccountID,UserName,UserPassword,UserType )\
               VALUES (default,  '%s',   '%s',    '%s') " \
                  %(             fn,   ln,     'P')

    try:
        cursor.execute( sql )
        db.commit()        
        # Commit       
    except:
        # Rollback 
        db.rollback()
        print "iu rollback" 

    
    id_sql = "SELECT * FROM UserAccount ORDER BY UserAccountID DESC LIMIT 1 "

    try:
        id_cursor.execute( id_sql )
        db.commit()        
        # Commit       
    except:
        # Rollback 
        db.rollback()
        print "select id rollback"  
    
    id_row = id_cursor.fetchone()
    return id_row[0]
    
    
# ---------------------------------------------------------------------------------------------------------------------

def insert_player(db,
                  a_id,
                  s_id, 
                  fn, ln,
                  r, t, email,
                  gh, v,
                  tel, pd
                  ):
    
    cursor = db.cursor()
    
    
    sql = "INSERT INTO Player(PlayerID, SupervisorID, PlayerFirstName, PlayerLastName, \
           PlayerRole, PlayerType, ProfileDescription, PlayerEmail, GameHandle, Phone, VoiP) \
               VALUES (   {0},   {1},   '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}')"\
              .format(   a_id,   s_id,    fn,    ln,    r,     t,     pd,   email,  gh,    tel,    v )
    
    
    try:
        cursor.execute( sql )
        db.commit()        
        # Commit       
    except:
        # Rollback 
        db.rollback()
        print "ip rollback" 

        
        
          
# ---------------------------------------------------------------------------------------------------------------------
def main():
    
    
    utility.header("Adding new Players","")
    
    form = cgi.FieldStorage()
    
    # connect to db
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
    
    # get number of new players
    num_of_players = (int) (form.getvalue("num_of_players"))  

    
    # lists to hold details
    supervisor_ids = []
    
    player_first_names = []
    player_last_names = []
    player_roles = []
    player_types = []
    player_emails = []
    player_gamehandles = []
    player_voips = []
    
    player_phones = []
    profile_descriptions = []
    
    
    
    
    # get Player details into lists -------------------------
    for i in range(0,num_of_players):
        
        # supervisor name to find id
        sn = form.getvalue("supervisor_name%s"%(i+1))
        
        # get id
        sid = get_supervisor_id(db, sn)
        
        # insert into supervisor id list
        supervisor_ids.append(sid)



        # first name
        fn = form.getvalue("player_first_name%s"%(i+1))
        player_first_names.append(fn) 
        
        # last name
        ln = form.getvalue("player_last_name%s"%(i+1))
        player_last_names .append(ln) 

        # role
        r = form.getvalue("player_role%s"%(i+1))
        player_roles.append(r) 
        
        # type
        t = form.getvalue("player_type%s"%(i+1))
        player_types.append(t) 

        # email
        email = form.getvalue("player_email%s"%(i+1))
        player_emails .append(email) 
        
        # gamehandle
        gh = form.getvalue("player_gamehandle%s"%(i+1))
        player_gamehandles.append(gh) 
        
        # voip
        v = form.getvalue("player_voip%s"%(i+1))
        player_voips.append(v) 
        
        # phone        
        tel = form.getvalue("player_phone%s"%(i+1))
        if tel is None:
            tel = ''
        player_phones.append(tel)         
        
        # profile description
        pd = form.getvalue("profile_description%s"%(i+1))
        if pd is None:
            pd = ''
        profile_descriptions.append(pd)

    # end of for loop --------------------------------------------------
    
    
    
    result = extract_results(num_of_players, supervisor_ids, 
                             player_first_names, player_last_names,
                             player_roles , player_types, player_emails,
                             player_gamehandles, player_voips)
    
    
    # if all needed inputs are valid------------------------------------
    if result == True:
        
        for i in range(0, num_of_players):
            
            # insert new UserAccount first
            # first name as default username and last name as default password
            id = insert_user(db, player_first_names[i], player_last_names[i] )
            
            
            # insert Player
            insert_player(db, id, supervisor_ids[i],player_first_names[i], player_last_names[i], player_roles[i], player_types[i], player_emails[i], player_gamehandles[i], player_voips[i], player_phones[i], profile_descriptions[i])
        
        
    display_success(result,num_of_players )
    
# ---------------------------------------------------------------------------------------------------------------------       
            

    
main()


    
      
      
        
        
        
        
        
        
        
        


    