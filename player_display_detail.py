import cgi, MySQLdb, utility,sys


form = cgi.FieldStorage()
Id = form.getvalue("id")
if Id == None:
    utility.redirect("player_display.py")
    sys.exit(0)
else:
    # Connect to DB
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Player WHERE PlayerID=%s"%Id)

    # Fetch one row at a time
    row = cursor.fetchone()
        
    Id = row[0]
    Supervisor_id = row[1]
    First_name = row[2]
    Last_name = row[3]       
    Gamehandle = row[8]
    Role = row[4]
    Type = row[5]
    Description = row[6]
    
    cursor.execute("SELECT * FROM Player WHERE PlayerID=%s"%Supervisor_id)
    # Fetch one row at a time
    row = cursor.fetchone()
    Supervisor = row[2]+" "+row[3]
    
    utility.header((First_name+" "+Last_name+" detail"),"player")
    print """
        <ul>
          <li>First Name: %s</li>
          <li>Last Name: %s</li>
          <li>Supervised by: %s</li>
          <li>Gamehandle: %s</li>
          <li>Role: %s</li>
          <li>Type: %s</li>
          <li>Description: %s</li>
        </ul>
        <a href="player_display.py">Back</a>
    </body>
    </html>
    """%(First_name, Last_name, Supervisor, Gamehandle, Role, Type, Description)


