import session, MySQLdb, utility

sess = session.Session(expires=20*60, cookie_path='/')


def display_profile():
    usertype = utility.header("My Profile", "player")
    
    # connect to database
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
        
    cursor = db.cursor()
    sup_cursor=db.cursor()

    cursor.execute("SELECT * FROM Player where PlayerID={0}".format(sess.data["UserID"]))
    
    # fetch first player
    player_row = cursor.fetchone()
    
    sup_cursor.execute("SELECT PlayerFirstName,PlayerLastName from Player where PlayerID={0}".format(player_row[1]))
    sup_row=sup_cursor.fetchone()
    
    player_info=[]
    player_info.append(sup_row[0]+" "+sup_row[1])

    for i in range(9):
        if player_row[i+2]==None:
            player_info.append("None")
        else:
            player_info.append(player_row[i+2])    
    
    print """
    
    <p>
    <hr>
    <form action="player_update.py">
    <input class="btn btn-primary" type="submit" value="Update your Profile">
    """
    if usertype == "PS":
        print '<a class="btn btn-primary" href="instance_run_add.py">Upload instance run</a>'
        print '<a class="btn btn-primary" href="venue_update.py">Update Venues</a>'
        print '<a class="btn btn-primary" href="update_instance_run.py">Update Instance Run</a>'
        
    print """
    </p>

    %s
    <h3> Player Detail </h3>
    <ul>
      <li>First Name: %s</li>
      <li>Last Name: %s</li>
      <li>Supervisor: %s</li>
      <li>Gamehandle: %s</li>
      <li>Role: %s</li>
      <li>Type: %s</li>
      <li>Description: %s</li>
      <li>Email: %s</li>
      <li>Phone: %s</li>
      <li>Voip: %s</li>
    </ul>
    <h3> Address Details </h3>
    <ul>
    
"""%((sess.data.get("MSG") if sess.data.get("Success")==1 else ""),player_info[1], player_info[2], player_info[0], player_info[7], player_info[3], player_info[4], player_info[5], player_info[6], player_info[8], player_info[9])
    if sess.data.get("Success")==1:
        sess.data["Success"]=2
        
    # get all address records for current player     
    sql = "select * from PlayerAddress \
            inner join    Address On Address.AddressID = PlayerAddress.AddressID \
                where PlayerAddress.PlayerID = %d \
                ORDER BY PlayerAddress.StartDate DESC;" \
                        %(player_row[0])
    
    cursor.execute(sql)

    address_rows = cursor.fetchall()
    for row in address_rows:
        add_info=[]
        for i in range(14):
            if row[i+2]==None:
                add_info.append('')
            else:
                add_info.append(row[i+2])
        
        

        if add_info[1] == '':
            today = add_info[0]
        else:
            today = add_info[1]
        
        print """
        <li>%s address: From %s to %s     :   %s%s, %s %s, %s %s %s, %s Postcode: %s</li>
        
        """%(add_info[7], add_info[0], today, add_info[3], add_info[4], add_info[5], 
             add_info[6], add_info[9], add_info[10], add_info[11], add_info[13], add_info[12])
                
    # close after use
    db.close()
    print """
    </ul>
"""
    utility.footer()



# Define main function.
def main():
    info=sess.data
    loggedIn = info.get("loggedIn")
                         
    if not loggedIn or info.get("UserType") == 'V':    
        # redirect to login page
        utility.redirect("login.py")
    else:
        display_profile()

# Call main 
main()
    





