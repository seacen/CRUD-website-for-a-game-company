# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb, utility, time
from datetime import date

sess = session.Session(expires=20*60, cookie_path='/')
# --------------------------------------------------------------------------------------------------------------------
# send session cookie
# ---------------------------------------------------------------------------------------------------------------------


def main():
    # check user identity
    info=sess.data
    loggedIn = info.get("loggedIn")
    if not loggedIn or info.get("UserType") == 'V':    
        utility.redirect("login.py")
    
    else:
        utility.header("","player")

        form = cgi.FieldStorage()
        
        p_num = 0
        a_num = 0

        # 3 Compulsory fields of Player

        Gamehandle = form.getvalue("Gamehandle")

        if Gamehandle is not None:
            p_num += 1

        Email = form.getvalue("Email")
        if Email is not None:
            p_num += 1
        
        Voip = form.getvalue("Voip")
        if Voip is not None:
            p_num += 1
            
        # 1 Voluntary fields of Player
        Phone = to_null(form.getvalue("Phone"))

        
        
        # 7 Compulsory fields of Address
        Street_num = form.getvalue("Street_num")
        # if string is an int
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
        
        
        # 3 Voluntary fields of Address 
        Street_num_suffix = to_null(form.getvalue("Street_num_suffix"))  
        Address_type = to_null(form.getvalue("Address_type"))
        Minor = to_null(form.getvalue("Minor"))
    
        # connect to database 
        db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)

        player_cursor = db.cursor()
        adrress_cursor = db.cursor()
        player_address_cursor = db.cursor()
    

        # Check what has been changed
        #
        # 0 - nothing changed
        # 1 - player changed
        # 2 - address changed
        # 3 - both changed
        status = check_detail(db, Gamehandle, Email, Voip, Phone, Street_num, Street_num_suffix, Street_name, Street_type, Address_type, Minor, Major, District, Post, Country)
        
    
        if status == 1 and p_num == 3:
            
            update_player(db,Gamehandle, Email, Phone, Voip)
            
            print"""
            <h2> "Your personal detail has been updated \n"</h2>
            
            """
        elif status == 2 and a_num == 7:
            
            
            # insert address entered as a new row into Address table
            insert_address(db, Street_num, Street_num_suffix, Street_name, Street_type, Address_type, Minor, Major, District, Post, Country)
            # update EndDate of last address
            update_last_address_date(db)
            # get latest inserted AddressId
            current_address_id = new_address_id(db)
            # insert player_address
            insert_player_address(db, current_address_id )
            
            print"""
            <h2> "Your address detail has been updated! \n"</h2>
            
            """
        elif status == 3 and p_num == 3 and a_num == 7:
            
            update_player(db,Gamehandle, Email, Phone, Voip)
            
            # insert address entered as a new row into Address table
            insert_address(db, Street_num, Street_num_suffix, Street_name, Street_type, Address_type, Minor, Major, District, Post, Country)
            # update EndDate of last address
            update_last_address_date(db)
            # get latest inserted AddressId
            current_address_id = new_address_id(db)
            # insert player_address
            insert_player_address(db, current_address_id )
            
            print"""
            <h2> "Your personal detail has been updated! \n"</h2>
            <h2> "Your address &nbspdetail has been updated! \n"</h2>
            """
        
        else:
            if p_num < 3 or a_num <7:
                print"""
                <h2> "Compulsory fields cannot be blank \n"</h2>
                """
            
            else:
                print"""
                <h2> "Nothing has changed! \n"</h2>
            
                """
        
    db.close()
    
    # end of main()

# ---------------------------------------------------------------------------------------------------------------------





### Check if 
### Address or Player is changed 
### or both are changed 
### or none is changed
def check_detail(db, Gamehandle, Email, Voip, Phone, Street_num, Street_num_suffix, Street_name, Street_type, Address_type, Minor, Major, District, Post, Country):
    
        
    
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
        
    
        ### Boolean Variables
        player_detail_changed = 0
        address_changed = 0

        if ( Gamehandle != (current_address_row[12]) or Email != current_address_row[11] or Phone != to_null(current_address_row[13]) or Voip != current_address_row[14] ):
            player_detail_changed = 1;
        
        if ( Street_num != current_address_row[16] or \
            Street_num_suffix != to_null(current_address_row[17]) or \
            Street_name != current_address_row[18] or \
            Street_type != current_address_row[19] or \
            Address_type != to_null(current_address_row[20]) or \
            Minor != to_null(current_address_row[22]) or \
            Major != current_address_row[23] or \
            District != current_address_row[24] or \
            Post != current_address_row[25] or \
            Country != current_address_row[26] ):
            
            address_changed = 1;
    
        
        if      ( player_detail_changed == 0 and address_changed == 0 ):
            return 0;
        
        elif    ( player_detail_changed == 1 and address_changed == 0 ):
            return 1;
        
        elif    ( player_detail_changed == 0 and address_changed == 1 ):
            return 2;
        
        elif    ( player_detail_changed == 1 and address_changed == 1 ):
            return 3;

    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------        





### Update player's details 
def update_player(db, Gamehandle, Email, Phone, Voip):
    
    player_cursor = db.cursor()
    
    player_sql = "UPDATE Player \
                    SET GameHandle ='%s', PlayerEmail='%s', Phone='%s', Voip='%s' \
                        WHERE PlayerID = %s " \
                            % (Gamehandle, Email, Phone, Voip, sess.data["UserID"])
    
    try:
        # Execute the SQL command
        player_cursor.execute(player_sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        print "up rollback"
        
# ---------------------------------------------------------------------------------------------------------------------
         
    



### Insert new Address 
def insert_address(db, Street_num, Street_num_suffix, Street_name, Street_type, Address_type, Minor, Major, District, Post, Country):

    
    adrress_cursor = db.cursor()
    
    adrress_sql = "INSERT INTO Address(AddressID, StreetNumber, StreetNumberSuffix, StreetName, StreetType, AddressType, AddressTypeIdentifier, \
                        MinorMunicipality, MajorMunicipality, GoverningDistrict, PostalArea, Country) \
                               VALUES (%s, %d, '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s')" \
                                % ("default", Street_num, to_null(Street_num_suffix), Street_name, Street_type, Address_type, "default", Minor, Major, District, Post, Country)

    try:
        adrress_cursor.execute( adrress_sql )
        # Commit
        db.commit()
    except:
        # Rollback 
        db.rollback()
        print "ia rollback"
        
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------                     





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





### connect player and address which just entered
def insert_player_address(db, new_adrress_id):

    
    pa_cursor = db.cursor()
    
    pa_sql = "INSERT INTO PlayerAddress(PlayerID, AddressId, StartDate, EndDate)\
                           VALUES ( %s, %s, CURDATE(), null) "\
                                % (sess.data["UserID"], new_adrress_id)
                           
    try:
        pa_cursor.execute(pa_sql)
        db.commit()
    except:
        db.rollback()
        print "ipa rollback"
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- 





### connect player and address which just entered
def update_last_address_date(db):
    
    cursor = db.cursor()
    
    sql = "UPDATE PlayerAddress Set EndDate = curdate() \
               WHERE PlayerID=%s ORDER BY AddressId DESC LIMIT 1 " \
                    % (sess.data["UserID"])
    
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "ulad rollback"
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- 



def to_null(value):
    
    if value is None:
        return ""
    else:
        return value  
    
    
    
    
    
    
main()





