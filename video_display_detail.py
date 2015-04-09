import cgi, MySQLdb, utility,sys,session

sess = session.Session(expires=20*60, cookie_path='/')

form = cgi.FieldStorage()
Id = form.getvalue("id")

if Id == None:
    utility.redirect("video_display.py")
    sys.exit(0)
else:
    # Connect to DB
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM Video WHERE VideoID=%s"%Id)
    row = cursor.fetchone()
        
    Url = row[1]
    Price = row[2]
    Type = row[3]
    Instance_run_id = row[4]
    Game_id = row[5]
    
    cursor.execute("SELECT * FROM InstanceRun WHERE InstanceRunID=%s"%Instance_run_id)
    row = cursor.fetchone()
    Instance_run_name = row[2]
    
    cursor.execute("SELECT * FROM Game WHERE GameID=%s"%Game_id)
    row = cursor.fetchone()
    Game_name = row[1]
    
    utility.header("Video of {0}".format(Instance_run_name),"video")
    
    
    print """
        <h3> Video %s from %s </h3>
        <ul>
          <li>Game: %s</li> 
          <li>Type: %s</li> 
          <li>Price: %s</li>
           %s
        </ul>"""%(Id, Instance_run_name, Game_name, Type, Price,("<li><a href=\"do_video_order.py?id={0}\">Watch This Video</a></li>".format(Id)) if Type!="free" else """<div class="embed-responsive embed-responsive-16by9">
                                                                                                                                                          <iframe class="embed-responsive-item" src={0}></iframe>
                                                                                                                                                            </div>""".format(Url))
    
    #API for video embedding
    key='Show{0}'.format(Id)
    isShow=sess.data.get(key)
    if isShow:
        print """
        <div class="embed-responsive embed-responsive-16by9">
          <iframe class="embed-responsive-item" src={0}></iframe>
        </div>
        """.format(Url)
        
        sess.data[key]=0

    print """<a href="video_display.py">Back</a>
    </body>
    </html>
    """
    
    utility.footer()
