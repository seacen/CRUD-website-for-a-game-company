import MySQLdb, utility

utility.header("Games", "game")

db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM Game")
    
# fetch first row
row = cursor.fetchone()
    
while row is not None:    
    Id = row[0]                   
    Game = row[1]
    Genre = row[2]
    Review = row[3] 
    Star_rating = row[4]
    Cost = row[8]
    
# fetch another one
    row = cursor.fetchone()
    
    print """
        <hr class="featurette-divider">

        <div class="row featurette">
          
          <div class="col-md-5">
            <img class="featurette-image img-responsive" src="game_pic_{1}.jpg" alt="Generic placeholder image">

          </div>

          <div class="col-md-7">
            <h2 class="featurette-heading"> {0} STARS <a href="game_display_detail.py?id={1}"><span class="text-muted">{2}</span></a></h2>
            <p class="lead">{3}</p>
          </div>


        </div>
    """.format(Star_rating, Id, Game, Review, Id)
         
# close after use
db.close()

utility.footer()





