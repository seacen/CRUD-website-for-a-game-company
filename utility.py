import session, cgi, MySQLdb


def header(title, actived):
    # ---------------------------------------------------------------------------------------------------------------------
    sess = session.Session(expires=20*60, cookie_path='/')
    loggedIn = sess.data.get('loggedIn')
    # send session cookie
    print "%s\nContent-Type: text/html\n" % (sess.cookie)
                
    
    if loggedIn:
        
        db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
        cursor = db.cursor()

        usertype = sess.data['UserType']
        if usertype == "P":
            profile_link = "player_read.py" 
                      
            cursor.execute("""SELECT PlayerType from Player where PlayerID = {0}""".format(sess.data['UserID']))
            row = cursor.fetchone()
            playertype = row[0]
            usertype = usertype + playertype 
            
        elif usertype == "V":
            profile_link = "viewer_read.py"            
            cursor.execute("""SELECT ViewerType from Viewer where ViewerID = {0}""".format(sess.data['UserID']))
            row = cursor.fetchone()
            viewertype = row[0]
            usertype = usertype + viewertype
            
        elif usertype == "A":
            profile_link = "admin_home.py"
        
        message = """<ul class="nav navbar-nav navbar-right">
                       <li><a href={0}>Hi! {1}</a></li>
                       <li><a href="do_logout.py">Logout</a>
                     </ul>
        """.format(profile_link, sess.data['UserName'])
        
    else:
        usertype = None
        message="""<ul class="nav navbar-nav navbar-right">
                       <li><a href="viewer_register.py">or...sign up now !</a></li>
                  </ul>
                    
                  <form class="navbar-form navbar-right" method="post" action="do_login.py">
                     <input type="text" class="form-control col-lg-3" placeholder="username" name="username" id="short">
                     <input type="password" class="form-control col-lg-3" placeholder="password" name="password" id="short">
                     <input type="submit" class="btn btn-primary" value="Login">
                   </form>
                """     
        
    # tidy up                 
    sess.close()  

    home = ""
    game = ""
    video = ""
    player = ""
    venue = ""
    instance_run = ""
    equipment = ""
    div = '<div class="container marketing">'
    if actived == "home":
        home = "active"
        div = ""
    elif actived == "game":
        game = "active"
    elif actived == "video":
        video = "active"
    elif actived == "player":
        player = "active"
    elif actived == "venue":
        venue = "active"
    elif actived == "instance run":
        instance_run = "active"
    elif actived == "equipment":
        equipment = "active"
    
    print """
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>{0}</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">


    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Custom styles for this template -->
    <link href="carousel.css" rel="stylesheet">
    
    </head>
<!-- NAVBAR
================================================== -->
  <body>
    <div class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-responsive-collapse">
             <span class="icon-bar"></span>
             <span class="icon-bar"></span>
             <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="about_page.py">WWAG</a>
        </div>
        
        <div class="navbar-collapse collapse navbar-responsive-collapse">
           <ul class="nav navbar-nav">
             <li class={1}><a href="home.py">Home</a></li>
             <li class="dropdown {2}">
             <a href="game_display.py" class="dropdown-toggle" data-toggle="dropdown">Game<b class="caret"></b></a>
               <ul class="dropdown-menu">
                 <li><a href="game_display.py">All</a></li>
                 <li class="divider"></li>
                 <li class="dropdown-header">--Hot--</li>
                 <li><a href="#">Dota II</a></li>
                 <li><a href="#">Call of Duty</a></li>
                 <li><a href="#">World of Warcraft</a></li>           
               </ul>
             </li>
             <li class="dropdown {3}">
             <a href="video_display.py" class="dropdown-toggle" data-toggle="dropdown">Video<b class="caret"></b></a>
               <ul class="dropdown-menu">
                 <li><a href="video_display.py">Browse all</a></li>
                 <li class="divider"></li>
                 <li><a href="video_order.py">Order premium</a></li>
               </ul>
             </li>
             <li class={4}><a href="player_display.py">Player</a></li>
             <li class={5}><a href="instance_run_display.py">Instance Run</a></li>
             <li class={6}><a href="venue_display.py">Venue</a></li>
             <li class={7}><a href="equipment_display.py">Equipment</a></li>
           </ul>          

        {8} 

       </div>
      </div>
    </div>
    {9}
    """.format(title, home, game, video, player, instance_run, venue, equipment, message, div)
    return usertype

def footer():
    print """
    <hr class="featurette-divider">

      <!-- /END THE FEATURETTES -->


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2014 Company, Inc. &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
      </footer>

    </div><!-- /.container -->
    
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="../../assets/js/docs.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
"""
    
    
def redirect(link):
    print "Content-Type: text/html\n"
    print """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="refresh" content="0;url=%s">
    </head>
    <body>
    </body>
    """%link