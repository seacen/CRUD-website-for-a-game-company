# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb, utility, time
from datetime import date

sess = session.Session(expires=20*60, cookie_path='/')
# --------------------------------------------------------------------------------------------------------------------
# send session cookie
# ---------------------------------------------------------------------------------------------------------------------


def main():
    
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn or info.get("UserType") != 'V':    
        utility.redirect("login.py")
    
    else:
        utility.header("Update Viewer","player")

        form = cgi.FieldStorage()
        
        viewer_type = form.getvalue("viewer_type")
        
        
        # 2 fields of Viewer
        dob = form.getvalue("dob")       
        email = form.getvalue("email")
        
        
        # 2 CrowdFundingViewer fields
        first_name = form.getvalue("first_name")
        last_name = form.getvalue("last_name")

        
        a_num = 0
        # 7 Compulsory fields of Address
        Street_num = form.getvalue("Street_num")
        if Street_num is not None:
            a_num += 1 
            if Street_num.isdigit():
                Street_num = int(Street_num)
        Street_name = form.getvalue("Street_name")
        if Street_name is not None:
            a_num += 1

        Street_type = form.getvalue("Street_type")
        if Street_type is not None:
            a_num += 1
                
        Major = form.getvalue("Major")
        if Major is not None:
            a_num += 1   

        District = form.getvalue("District")
        if District is not None:
            a_num += 1 

        Post = form.getvalue("Post")
        if Post is not None:
            a_num += 1 

        Country = form.getvalue("Country")
        if Country is not None:
            a_num += 1   

        
        # 4 Voluntary fields of Address 
        Street_num_suffix = form.getvalue("Street_num_suffix")  
        Address_type = form.getvalue("Address_type")
        Address_type_identifier = form.getvalue("Address_type_identifier")
        Minor = form.getvalue("Minor")

        # connect to database 
        db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
        
        #81 None pviewer RD None None Parkvile Melbourne VIC 3000 Australia
        
        address_changed = check_detail(db,
                              Street_num, Street_num_suffix, 
                              Street_name, Street_type, 
                              Address_type, Address_type_identifier, 
                              Minor, Major, District, Post, Country)
         
        # address is not changed 
        if address_changed == 0 or address_changed  == 1:
            
            # update Viewer
            viewer_cursor = db.cursor()
            
            sql1 = """UPDATE Viewer SET DateOfBirth ="%s", Email = '%s' \
                        WHERE ViewerID = %s """ \
                            % (dob, email, sess.data["UserID"])
            
            
            
            
            viewer_detail_cursor = db.cursor()
            sql2 = None
            # update CrowdFundingViewer 
            if viewer_type == "C":
                
                sql2 = """UPDATE CrowdFundingViewer SET FirstName='%s', LastName='%s' \
                            WHERE ViewerID = %s """ \
                                % (first_name , last_name, sess.data["UserID"])
                

            try:
                viewer_cursor.execute(sql1)
                if (sql2 !=None):
                    viewer_detail_cursor.execute(sql2)
                db.commit()
                
                
            except:
                # Rollback in case there is any error
                db.rollback()
                print "up rollback"
            
            


        
        # address is changed ----------------------------------------------------------------------------------------------------------------------------
        if address_changed == 1 and a_num == 7:
            

            # update address 
            address_cursor = db.cursor()
    
            address_sql = "INSERT INTO Address(AddressID, StreetNumber, StreetNumberSuffix, StreetName, StreetType, AddressType, AddressTypeIdentifier, \
                                MinorMunicipality, MajorMunicipality, GoverningDistrict, PostalArea, Country) \
                                   VALUES (%s, %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                                % ("default", 
                                   Street_num, Street_num_suffix, 
                                   Street_name, Street_type, 
                                   Address_type, Address_type_identifier, 
                                   Minor, Major, District, Post, Country)
            
            # Commit if successs        
            try:
                address_cursor.execute(address_sql)
                db.commit()
                print "Address is updated"
            except:
                # Rollback in case there is any error
                db.rollback()
                print "insert address -> rollback"

            # ---------------------------------------------------------------------------
            
            
            # update EndDate of last address
            update_last_viewer_date(db)

            # get address id just inserted
            new_id = new_address_id(db)
            
            # insert viewer address
            insert_viewer_address(db, new_id)
            

    print """
    
    <a href="viewer_read.py"> Click here to return detail page</a>
</body>

</html>
"""
        
        
        
### Check if 
### Address is changed 
#   ---------------------------------------------------------------------------------------------------------
def check_detail(db,
                 Street_num, Street_num_suffix,
                 Street_name, Street_type,
                 Address_type, Address_type_identifier,
                 Minor, Major, District, Post, Country):
    

        sql1 = "select * from ViewerAddress \
                where ViewerID = %s and EndDate is null" \
                       % (sess.data["UserID"])

        latest_address_cursor = db.cursor()
        latest_address_cursor.execute(sql1)
        latest_address_row = latest_address_cursor.fetchone()
        

    
        sql2 = """select * from ViewerAddress \
                    inner join Viewer On Viewer.ViewerID = ViewerAddress.ViewerID \
                    inner join Address on Address.AddressID = ViewerAddress.AddressID \
                        where ViewerAddress.ViewerID = %s \
                            and ViewerAddress.AddressID = %s """ \
                                % (latest_address_row[0], latest_address_row[1] )
    

        current_address_cursor= db.cursor()
        current_address_cursor.execute(sql2)
        current_address_row = current_address_cursor.fetchone()
        
    
        ### Boolean Variable
        address_changed = 0

        if  Street_num != current_address_row[9]: address_changed = 1
        if  to_null(Street_num_suffix) != current_address_row[10]: address_changed = 1
        if  Street_name != current_address_row[11]: address_changed = 1
        if  Street_type != current_address_row[12]: address_changed = 1
        if  to_null(Address_type) != current_address_row[13]: address_changed = 1
        if  to_null(Address_type_identifier) != current_address_row[14]: address_changed = 1
        if  to_null(Minor) != current_address_row[15]: address_changed = 1
        if  Major != current_address_row[16]: address_changed = 1
        if  District != current_address_row[17]: address_changed = 1 
        if  Post != current_address_row[18]: address_changed = 1
        if  Country != current_address_row[19]: address_changed = 1
            


        
        return address_changed 
        


    
# ---------------------------------------------------------------------------------------------------------------------------------------------------
### find last entered row of address and return AddressID                           
def new_address_id(db):
    
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



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- 
### connect viewer and address which just entered
def insert_viewer_address(db, new_address_id):

    
    va_cursor = db.cursor()
    
    va_sql = "INSERT INTO ViewerAddress(ViewerID, AddressID, StartDate, EndDate)\
                           VALUES ( %s, %s, CURDATE(), null) "\
                                % (sess.data["UserID"], new_address_id)
                           
    try:
        va_cursor.execute(va_sql)
        db.commit()
    except:
        db.rollback()
        print "iva rollback" 
        


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- 
### update enddate of last address
def update_last_viewer_date(db):
    
    cursor = db.cursor()
    
    sql = "UPDATE ViewerAddress Set EndDate = curdate() \
               WHERE ViewerID=%s ORDER BY ViewerId DESC LIMIT 1 " \
                    % (sess.data["UserID"])
    
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "ulvd rollback"

        
#----------------------------------------------------------------------------------------------------------------
def display_success(result):
    
    if result == True:
        s1 = "successful!"
        s2 = "homepage.py"
        s3 = "Click here to return to HOMEPAGE."
        
    else:
        s1 = "unsuccessful!\nPlease fill in all blanks."         
        s2 = "upload_instance_run.py"
        s3 = "Click here to try again."
        
    
    
    print """
    <h2>Your upload was %s</h2>
    <a href=%s>%s</a>
</body>

</html>
""" %(s1, s2, s3)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- 
def to_null(value):
    
    if value is None:
        return ""
    else:
        return value  
       
        
main()
        