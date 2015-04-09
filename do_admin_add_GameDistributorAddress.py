import utility, cgi, MySQLdb, session

sess = session.Session(expires=20*60, cookie_path='/')

# check if it is administrator
usertype = utility.header("Add distributor address","")
if usertype != "A":
    utility.redirect("login.py")
    sys.exit(0)
    
form = cgi.FieldStorage()
   
# get form values
Distributor_id = form.getvalue("GameDistributorID")

Street_num = form.getvalue("Street_num")
Street_name = form.getvalue("Street_name")
Street_type = form.getvalue("Street_type")
Major = form.getvalue("Major")
District = form.getvalue("District")         
Post = form.getvalue("Post")
Country = form.getvalue("Country")

Street_num_suffix = form.getvalue("Street_num_suffix")
Address_type = form.getvalue("Address_type")
Address_type_identifier = form.getvalue("Address_type_identifier")
Minor = form.getvalue("Minor")

# connect to db
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)

cursor = db.cursor()
    
sql = "INSERT INTO Address(AddressID, StreetNumber, StreetNumberSuffix, StreetName, StreetType, AddressType, AddressTypeIdentifier, \
                        MinorMunicipality, MajorMunicipality, GoverningDistrict, PostalArea, Country) \
                               VALUES (%s,  %s,   '%s',  '%s', '%s',  '%s', '%s',  '%s', '%s',  '%s',  '%s', '%s')" \
                                % ("default", Street_num, Street_num_suffix, Street_name, Street_type, Address_type, 
                                   Address_type_identifier, Minor, Major, District, Post, Country)
                             
try:
    # insert into Address
    cursor.execute( sql )
    
    # get the AddressID of inserted row    
    address_cursor = db.cursor() 
    address_sql  = "SELECT * FROM Address ORDER BY AddressID DESC LIMIT 1 "
    address_cursor.execute( address_sql )
    new_address_row = address_cursor.fetchone() 
    Address_id = new_address_row[0]                               
             
    # set previous EndDate as current date
    cursor3 = db.cursor() 
    sql3 = "UPDATE GameDistributorAddress Set EndDate = curdate() \
               WHERE GameDistributorID=%s ORDER BY AddressID DESC LIMIT 1 " \
                    % (Distributor_id )  
    cursor3.execute(sql3)
    
    # insert into GameDistributorAddress    
    cursor2 = db.cursor()                           
    sql2 = "insert into GameDistributorAddress(AddressID, GameDistributorID, StartDate, EndDate)\
           values (%s, %s, CURDATE(), null)"%(Address_id, Distributor_id)
    cursor2.execute(sql2)  
                                

    # Commit
    db.commit()       
    sess.data["adminMSG"] = "New distributor address is added successfully !"                                 
except:
    # Rollback 
    db.rollback()
    sess.data["adminMSG"] = "Failed to create new distributor !"  

utility.redirect("admin_home.py")       




                               