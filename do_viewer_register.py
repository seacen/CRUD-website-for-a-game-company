# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb, utility, time
from datetime import date

sess = session.Session(expires=20*60, cookie_path='/')
# --------------------------------------------------------------------------------------------------------------------
# send session cookie
# --------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------
def check_data(account, pw, viewer_type,     Street_num, Street_name, Street_type, Major, District, Post, Country):
    

    if account is None or pw is None or viewer_type is None or Street_num is None or Street_name is None or Street_type is None or Major is None or District is None or Post is None or Country is None:
            result = False
    else:
            result = True 

    return result



#----------------------------------------------------------------------------------------------------------------

def display_success(result):
    
    if result == True:
        s1 = "successful!"
        s2 = "href = home.py"
        s3 = "Click here to HOMEPAGE."
        
    else:
        s1 = "unsuccessful!\n Please fill all fileds with * "         
        s2 = ""
        s3 = "Press BACKSPACE to try again."
        
    
    
    print """
    <h2>Sign up was %s</h2>
    <a %s>%s</a>
</body>

</html>
""" %( s1, s2, s3  )



# --------------------------------------------------------------------------------------------------------------------
def to_null(value):
    
    if value is None:
        return ""
    else:
        return value  
    
    


# --------------------------------------------------------------------------------------------------------------------  
def insert_viewer_address(db, viewer_id, adrress_id ):
    
    cursor = db.cursor()

    sql = "INSERT INTO ViewerAddress(ViewerID, AddressId, StartDate, EndDate)\
                           VALUES ( %s, %s, CURDATE(), null) "\
                                % (viewer_id , adrress_id)
                           
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "iva rollback"

        
        
        

# --------------------------------------------------------------------------------------------------------------------    
#   find last entered row of address and return AddressID                           
def get_address_id(db):
    
    address_cursor = db.cursor()
    
    
    # select last row just entered #
    address_sql  = "SELECT * FROM Address ORDER BY AddressID DESC LIMIT 1 "

    try:
        address_cursor.execute( address_sql )
        db.commit()        
        # Commit       
    except:
        # Rollback 
        db.rollback()
        print "nai rollback"  
    
    new_address_row = address_cursor.fetchone()
    return new_address_row [0]




# --------------------------------------------------------------------------------------------------------------------
def insert_address(db, Street_num, Street_name, Street_type, Major, District, Post, Country, Street_num_suffix, Address_type, Address_type_identifier, Minor):
    
    cursor = db.cursor()
    
    sql = "INSERT INTO Address(AddressID, StreetNumber, StreetNumberSuffix, StreetName, StreetType, AddressType, AddressTypeIdentifier, \
                        MinorMunicipality, MajorMunicipality, GoverningDistrict, PostalArea, Country) \
                               VALUES (%s,       %s,         '%s',              '%s',           '%s',       '%s',        '%s',                 '%s', '%s',   '%s',    '%s', '%s')" \
                                % ("default", Street_num, Street_num_suffix, Street_name, Street_type, Address_type, Address_type_identifier, Minor, Major, District, Post, Country)
    
    try:
        cursor.execute( sql )
        # Commit
        db.commit()
    except:
        # Rollback 
        db.rollback()
        print "ia rollback"
    
    
    

# --------------------------------------------------------------------------------------------------------------------
def insert_viewer(db, viewer_id , viewer_type, dob, email, d_first_name, d_last_name, donation):
    
    cursor = db.cursor()
    
    
    sql = """INSERT INTO Viewer(ViewerID, ViewerType, DateOfBirth, Email) \
               VALUES (%s,    '%s',  "%s",   '%s' )"""    \
                % (viewer_id,   viewer_type,   dob,  email)
    
    try:
        db.commit()        
        # Commit       
    except:
        # Rollback 
        db.rollback()
        print "iv rollback"
    
    # for premium viewr
    if viewer_type == "P":
        sql2 = """INSERT INTO PremiumViewer(ViewerID, RenewalDate) \
                   VALUES (%s,    DATE_ADD(CURDATE(), INTERVAL 1 MONTH)    )"""    \
                    % (viewer_id)
        
        try:
            cursor.execute( sql )
            cursor.execute( sql2 )
            db.commit()        
            # Commit       
        except:
            # Rollback 
            db.rollback()
            print "ipv   rollback"  
        
    # for crowd funding viewer    
    if viewer_type == "C":
        sql2 = """INSERT INTO CrowdFundingViewer(ViewerID, FirstName, LastName, TotalAmountDonated) \
                   VALUES (%s,    '%s', '%s', '%s' )"""    \
                    % (viewer_id, d_first_name, d_last_name, donation)
        
        try:
            cursor.execute( sql )
            cursor.execute( sql2 )
            db.commit()        
            # Commit       
        except:
            # Rollback 
            db.rollback()
            print "icv   rollback" 
        
        
               
# --------------------------------------------------------------------------------------------------------------------
def insert_user(db, account, pw):
    
    # default type of user
    t = "V"

    
    cursor = db.cursor()
    id_cursor = db.cursor()
    
    sql = """INSERT INTO UserAccount(UserAccountID,UserName,UserPassword,UserType )\
               VALUES (default,  '%s',   '%s',    '%s') """ \
                  %(             account,   pw,     t )

    
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
    

    
    
# --------------------------------------------------------------------------------------------------------------------
def main():

    utility.header("Sign up","")
    
    form = cgi.FieldStorage()
    
    # connect to db
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
    # 4 fields for UserAccount
    account = form.getvalue("account")
    pw = form.getvalue("password")
    viewer_type = form.getvalue("viewer_type")
    dob = to_null(form.getvalue("date"))
    email = to_null(form.getvalue("email"))
    
    # 7 Compulsory fields of Address 
    Street_num = form.getvalue("Street_num")
    Street_name = form.getvalue("Street_name")
    Street_type = form.getvalue("Street_type")
    Major = form.getvalue("Major")
    District = form.getvalue("District")         
    Post = form.getvalue("Post")
    Country = form.getvalue("Country")

    # 4 Voluntary fields of Address 
    Street_num_suffix = to_null(form.getvalue("Street_num_suffix"))  
    Address_type = to_null(form.getvalue("Address_type"))
    Address_type_identifier = to_null(form.getvalue("Address_type_identifier"))
    Minor = to_null(form.getvalue("Minor"))

    d_first_name = form.getvalue("d_first_name")
    d_last_name = form.getvalue("d_last_name")
    donation = form.getvalue("donation")
    
    
    
    good_data = check_data(account, pw, viewer_type,     Street_num, Street_name, Street_type, Major, District, Post, Country)
    
    
    
    # if all Compulsory fields are filled
    if good_data:
        
        ## insert an account for viewer and get account idv
        viewer_id = insert_user(db, account, pw, )
        
        ## insert Viewer
        insert_viewer(db, viewer_id ,viewer_type, dob, email, d_first_name, d_last_name, donation)
        
        # insert Address 
        insert_address(db, Street_num, Street_name, Street_type, Major, District, Post, Country, Street_num_suffix, Address_type, Address_type_identifier, Minor)
        
        # get latest Address id
        address_id = get_address_id(db)
        
        ## insert ViewerAddress
        insert_viewer_address(db, viewer_id, address_id )
    
    
    
    
    display_success(good_data)
    

    db.close()

    
main()

