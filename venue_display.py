import session, MySQLdb, utility

utility.header("Venue", "venue")
 
# Connect to DB
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()
supervisor_cursor = db.cursor()


cursor.execute("SELECT * FROM Venue")

rows = cursor.fetchall()

print """
    
    
    <p>  <font size="8" color="White" > <center><b>Venue</b></center>  </font>  </p>
    
"""   

for row in rows:
    id =  row[0]
    name = row[1]
    discription = row[2]
    power = row[3]
    lighting = row[4]        
    supervisor_id = row[5]


    supervisor_sql = "select * from Player \
                        where PlayerID = %s" \
                            %( supervisor_id )
    
    supervisor_cursor.execute(supervisor_sql)
    supervisor_row = supervisor_cursor.fetchone()
    
    supervisor_name = supervisor_row[2] + " " + supervisor_row[3] 
    
    
    print """
        <hr>
        <div class="row featurette">
          
          <div class="col-md-5">
            <img class="featurette-image img-responsive" src="venue_pic_1.jpg" alt="Generic placeholder image">
          </div>

          <div class="col-md-7">
            <h2> <span class="text-muted"><b><u><center>{0}</center><u></b></span></h2>
            
            <hr>
    
            <p class="lead">Description:            <pre>{1}</pre></p>
            <p class="lead">Power Outlets:          <pre>{2}</pre></p>
            <p class="lead">LightingCondition:      <pre>{3}</pre></p>
            <p class="lead">Supervised by:          <pre>{4}</pre></p>
          </div>
          <div>
              <p><br></p>
          </div>

        </div>
    """.format(name, discription, power, lighting, supervisor_name )
    
    
     

utility.footer()

