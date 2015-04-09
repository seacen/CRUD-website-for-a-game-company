import session, MySQLdb, utility

sess = session.Session(expires=20*60, cookie_path='/')

# Required header that tells the browser how to render the HTML.

def display_profile():
    
    utility.header("My Profile", "")
    
    Id = sess.data["UserID"]
    
    #connect to database
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Viewer where ViewerID={0}".format(Id))
    
    # fetch viewer row
    viewer_row = cursor.fetchone()
    
    Type = viewer_row[1]
    Dob = viewer_row[2]
    Email = viewer_row[3]
                   
    print "<ul>\n"   


    
# ------------------------------------------------------------------------------------------------

    if sess.data["UserID"] == "V":
        print '<a class="btn btn-primary" href="instance_run_add.py">Upload instance run</a>'

    print """
    
    <p>
    <hr>
    <form action="viewer_update.py">
    <p><input class="btn btn-primary" type="submit" value="Update your Profile">&nbsp;&nbsp;&nbsp;<a href="viewer_videos.py" class="btn btn-primary">My Videos</a>
    """    

    
# ------------------------------------------------------------------------------------------------
# Show details for premium viewer or crowd funding viewer
    
    if Type == "C":
        cursor.execute("SELECT * FROM CrowdFundingViewer where ViewerID={0}".format(Id))
        C_viewer_row = cursor.fetchone()
        First_name = C_viewer_row[1]
        Last_name = C_viewer_row[2]
        Donation = C_viewer_row[3]
        print """
            <h3> Viewer Detail </h3>
            <li>First Name: %s</li>
            <li>Last Name:  %s</li>
            <li>Total Donation: %s</li>
        """%(First_name, Last_name, Donation)
            
                  
    elif Type == "P":
        cursor.execute("SELECT * FROM PremiumViewer where ViewerID={0}".format(Id))
        P_viewer_row = cursor.fetchone()   
        Renew_date = P_viewer_row[1]                   
        print """
            <li>Renew Date: %s</li>
        """%Renew_date

    
# ------------------------------------------------------------------------------------------------    
    print """   
            <li>Date of Birth: %s</li>
            <li>Email: %s</li>
            <h3> Address Details </h3>
    """%(Dob, Email)
        
    # get all address records for this viewer        
    sql = "select * from ViewerAddress \
            inner join    Address On Address.AddressID = ViewerAddress.AddressID \
                where ViewerAddress.ViewerID = %d;" \
                        %Id   
    cursor.execute(sql)
    
    address_rows = cursor.fetchall()
    for row in address_rows:
        add_info=[]
        for i in range(14):
            if row[i+2]==None:
                add_info.append('')
            else:
                add_info.append(row[i+2])
        
        
        print """
        <li>%s address: From %s to %s: %s%s, %s %s, %s %s %s, %s Postcode: %s</li>
        """%(add_info[7], add_info[0], add_info[1], add_info[3], add_info[4], add_info[5], 
             add_info[6], add_info[9], add_info[10], add_info[11], add_info[13], add_info[12])
                
    # close after use
    db.close()
    print """

</body>
</html>
"""

    #######################



# Define main function.
def main():
    info=sess.data
    loggedIn = info.get("loggedIn")
                         
    if not loggedIn or info.get("UserType") != 'V':    
        # redirect to login page
        utility.redirect("login.py")
    else:
        display_profile()

# Call main 
main()