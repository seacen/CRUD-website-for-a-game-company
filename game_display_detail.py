import cgi, MySQLdb, utility


utility.header("Game detail","game")

form = cgi.FieldStorage()
Id = form.getvalue("id")

if Id == None:
    utility.redirect("game_display.py")
else:
    # Connect to DB
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Game WHERE GameID=%s"%Id)

    # Fetch one row at a time
    row = cursor.fetchone()
        
    Name = row[1]
    Genre = row[2]
    Review = row[3]
    Star = row[4]
    Classification =row[5]
    Platform = row[6]
    Promotion = row[7]
    Cost = row[8]
    
    print """
        <ul>
          <li>Name: %s</li>      
          <li>Genre: %s</li>   
          <li>Review: %s</li>   
          <li>Star: %s</li>   
          <li>Classification: %s</li>   
          <li>Platform: %s</li>   
          <li>Promotion: %s</li>   
          <li>Cost: %s</li>          
        </ul>
        <a href="game_display.py">Back</a>
    </body>
    </html>
    """%(Name, Genre, Review, Star, Classification, Platform, Promotion, Cost)
    