import MySQLdb, utility

utility.header("Equipment", "equipment")

# connect to database
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM Equipment")
    
# fetch first row
row = cursor.fetchone()

# display each equipment's information
while row is not None:    
    id = row[0]                   
    model = row[1]
    review = row[2]
    speed = row[3] 
    
    print """
        <hr class="featurette-divider">

        <div class="row featurette">

          <div class="col-md-7">
            <h2 class="featurette-heading"><span class="text-muted">{0}</span></h2>
            <p class="lead">Processor speed: {2}</p>
            <p class="lead">{2}</p>
          </div>


        </div>
    """.format(model, speed, review)

    # fetch another one
    row = cursor.fetchone()
         
# close after use
db.close()

utility.footer()


