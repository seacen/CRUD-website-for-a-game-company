# The libraries we'll need
import sys, session, cgi, MySQLdb, utility

sess = session.Session(expires=20*60, cookie_path='/')

usertype = utility.header("Home", "home")

print """
    <!-- Carousel
    ================================================== -->
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="item active">
          <img src="home1.jpg" alt="First slide">
          <div class="container">
            <div class="carousel-caption">
              <h1>New to WWAG ?</h1>
              <p>'Wil Wheaton Appreciation Guild' is an interactive gaming community comprised of elite players around the world. Join us and enjoy tons of entertaining gameplay videos today !</p>
              <p><a class="btn btn-lg btn-primary" href="about_page.py" role="button">Learn more</a></p>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="home2.jpg" alt="Second slide">
          <div class="container">
            <div class="carousel-caption">
              <h1>Real hardcores</h1>
              <p>32 players, 32 Pros. Only at WWAG.</p>
              <p><a class="btn btn-lg btn-primary" href="player_display.py" role="button">Learn more</a></p>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="home3.jpg" alt="Third slide">
          <div class="container">
            <div class="carousel-caption">
              <h1>How's that game ?</h1>
              <p>Find the answer in our review for a wide range of game collections.</p>
              <p><a class="btn btn-lg btn-primary" href="game_display.py" role="button">Browse games</a></p>
            </div>
          </div>
        </div>
      </div>
      <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev"><span class="glyphicon glyphicon-chevron-left"></span></a>
      <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next"><span class="glyphicon glyphicon-chevron-right"></span></a>
    </div><!-- /.carousel -->
    """
utility.footer()



