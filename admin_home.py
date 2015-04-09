import utility, MySQLdb,sys, session

usertype = utility.header("Administration", "home")
# check user identity
if usertype != "A":
    utility.redirect("login.py")
    sys.exit(0)
else:
    # display all entities
    # all entities support CRUD where necessary
    sess = session.Session(expires=20*60, cookie_path='/')
    db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
    cursor = db.cursor()
    
    print """  
<hr class="featurette-divider">
    """
    
    #UserAccount
    print """
<h3>{1}</h3>

<div class="panel-group" id="accordion">
    <form method="post" action="do_admin_update.py?entity={0}">
      <div class="panel panel-default">
        <div class="panel-heading">        
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
       
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
               <ul id="ddd">Notes
               <li id="ddd">User account is added automatically when a player or viewer is created.</li>
               <li id="ddd">Deletion of a user account leads to cascading deletions of the corresponding player or viewer.</li>
               </ul>
               <tr>
                <td>UserAccountID</td>
                <td>UserName</td>
                <td>UserPassword</td>
                <td>UserType</td>
               </tr>
    """.format("UserAccount",sess.data["adminMSG"] if sess.data.get("adminMSG") else "")
    if sess.data.get("adminMSG"):
        sess.data["adminMSG"]=""
    
    cursor.execute("SELECT * FROM UserAccount")   
    rows = cursor.fetchall()   
    for row in rows:
        Id = row[0]                   
        Name = row[1]
        Password = row[2]
        Type = row[3] 
        
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_entity.py?entity={4}&UserAccountID={0}">delete</a></p></td>
                   <td><input name="UserName{0}" type="text" placeholder='{1}'></td>
                   <td><input name="UserPassword{0}" type="text" placeholder={2}></td>
                   <td><input name="UserType{0}" type="text" placeholder={3}></td>
                 </tr>
        """.format(Id, Name, Password, Type, "UserAccount") 
        
    
               
    #Player
    print """
             </table>
           </div>
         </div>
       </div>
    </form>
    
    <form method="post" action="do_admin_update.py?entity={0}">    
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
            <ul id="ddd">Notes
             <li id="ddd">Deletion of a player leads to loss of relevant instance run and address records.</li>
            </ul>
               <tr>
                 <th>PlayerID</th>
                 <th>SupervisorID</th>
                 <th>FirstName</th> 
                 <th>LastName</th>
                 <th>Role</th>
                 <th>PlayerType</th>
                 <th>Description</th>
                 <th>Email</th>
                 <th>Handle</th>
                 <th>Phone</th>
                 <th>Voip</th>
               </tr>
    """.format("Player")
    cursor.execute("SELECT * FROM Player")   
    rows = cursor.fetchall()   
    for row in rows:
        Id = row[0]                   
        SuperID = row[1]
        FirstName = row[2]
        LastName= row[3] 
        Role= row[4]
        Playertype = row[5]
        Description = row[6] 
        Email = row[7]
        Handle = row[8]
        Phone = row[9]
        Voip = row[10]             
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_entity.py?entity={11}&PlayerID={0}">delete</a></p></td>
                   <td><input name="SupervisorID{0}" type="number" min=1 placeholder={1}></td>
                   <td><input name="PlayerFirstName{0}" type="text" placeholder={2}></td>
                   <td><input name="PlayerLastName{0}" type="text" placeholder="{3}"></td>
                   <td><input name="PlayerRole{0}" type="text" placeholder={4}></td>
                   <td><input name="PlayerType{0}" type="text" placeholder={5}></td>
                   <td><textarea placeholder="{6}" name="ProfileDescription{0}"></textarea></td>
                   <td><input name="PlayerEmail{0}" class="email" type="email" placeholder={7}></td>
                   <td><input name="GameHandle{0}" type="text" placeholder="{8}"></td>
                   <td><input name="Phone{0}" type="tel" placeholder={9}></td>
                   <td><input name="Voip{0}" type="text" placeholder={10}></td>        
                 </tr>
        """.format(Id, SuperID, FirstName, LastName, Role, Playertype, Description, Email, Handle, Phone, Voip, "Player")    
               
    #PlayerAddress
    print """
             </table>
           </div>
         </div>
       </div>
    </form> 
    
    <form method="post" action="do_admin_update.py?entity={0}">  
       <div class="panel panel-default">
        <div class="panel-heading">        
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">   
            <table border="2">
               <ul id="ddd">Notes
                <li id="ddd">PlayerAddress is added automatically when a new player is created.</li>
                 <li id="ddd">Deletion is strongly discouraged.</li>
               </ul>
               <p id="ddd">(order by PlayerID, StartDate)</p>
               <tr>
                 <th>PlayerID</th>
                 <th>AddressID</th>
                 <th>StartDate</th>
                 <th>EndDate</th> 
               </tr>
    """.format("PlayerAddress")
    cursor.execute("select * from PlayerAddress ORDER BY PlayerID, StartDate")  
    row = cursor.fetchone()   
    while row is not None:
        PlayerID = row[0]
        AddressID = row[1]                           
        StartDate = row[2]
        EndDate= row[3] 
                       
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={4}&PlayerID={0}&AddressID={1}">delete</a></p></td>
                   <td>{1}</td>
                   <td>{2}</td> 
                   <td>{3}</td> 
               </tr>
        """.format(PlayerID,AddressID,StartDate,EndDate, "PlayerAddress")  
        row = cursor.fetchone()
    

    #Viewer
    print """
             </table>
           </div>
         </div>
       </div>
    </form>
    
    <form method="post" action="do_admin_update.py?entity={0}">    
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
            <ul id="ddd">Notes
             <li id="ddd">Deletion of a viewer leads to loss of relevant video order records.</li>
            </ul>
               <tr>
                 <th>ViewerID</th>
                 <th>ViewerType</th>
                 <th>DateOfBirth</th> 
                 <th>Email</th>
                 <th>RenewalDate</th>
                 <th>FirstName</th>
                 <th>LastName</th>
                 <th>TotalAmountDonated</th>
               </tr>
    """.format("Viewer")
    cursor.execute("""select * from (Viewer natural left outer join PremiumViewer) natural left outer join CrowdFundingViewer""")   
    rows = cursor.fetchall()   
    for row in rows:
        ViewerID = row[0]                   
        ViewerType= row[1]
        DateOfBirth= row[2]
        Email= row[3] 
        RenewalDate= row[4]
        FirstName= row[5]
        LastName= row[6] 
        TotalAmountDonated= row[7]            
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_entity.py?entity={8}&ViewerID={0}">delete</a></p></td>
                   <td><input name="ViewerType{0}" type="text" placeholder={1}></td>
                   <td><input name="DateOfBirth{0}" class="date" placeholder={2} type="text" onfocus="(this.type='date')"></td>
                   <td><input name="Email{0}" class="email" type="email" placeholder="{3}"></td>
                   <td><input name="RenewalDate{0}" class="date" placeholder={4} type="text" onfocus="(this.type='date')"></td>
                   <td><input name="FirstName{0}" type="text" placeholder={5}></td>
                   <td><input name="LastName{0}" type="text" placeholder={6}></td>
                   <td><input name="TotalAmountDonated{0}" type="number" min=0 placeholder={7}></td>       
                 </tr>
        """.format(ViewerID, ViewerType, DateOfBirth, Email, RenewalDate, FirstName, LastName, TotalAmountDonated, "Viewer")   
        
        
    #ViewerAddress
    print """
             </table>
           </div>
         </div>
       </div>
    </form>           
     
    <form method="post" action="do_admin_update.py?entity={0}"> 
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">   
            <table border="2">
               <ul id="ddd">Notes
                <li id="ddd">ViewerAddress is added automatically when a new viewer is created.</li>
                 <li id="ddd">Deletion is strongly discouraged.</li>
               </ul>
              <p id="ddd">(order by ViewerID, StartDate)</p>
               <tr>
                 <th>ViewerID</th>
                 <th>AddressID</th>
                 <th>StartDate</th>
                 <th>EndDate</th> 
               </tr>
    """.format("ViewerAddress")
    cursor.execute("select * from ViewerAddress ORDER BY ViewerID, StartDate")  
    row = cursor.fetchone()   
    while row is not None:
        ViewerID = row[0]
        AddressID = row[1]                         
        StartDate = row[2]
        EndDate= row[3] 
                       
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={4}&ViewerID={0}&AddressID={1}">delete</a></p></td>
                   <td>{1}</td>
                   <td>{2}</td> 
                   <td>{3}</td>  
               </tr>
        """.format(ViewerID, AddressID, StartDate,EndDate,"ViewerAddress")  
        row = cursor.fetchone()
    
    
    #Distributor
    print """
             </table>
           </div>
         </div>
       </div>
    </form>
    
    <form method="post" action="do_admin_update.py?entity={0}">    
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">     
            <table border="2">              
               <tr>
                 <th>GameDistributorID</th>
                 <th>CompanyName</th>
                 <th>ContactFirstName</th> 
                 <th>ContactLastName</th>
                 <th>Phone</th>
               </tr>
    """.format("GameDistributor")
    cursor.execute("SELECT * FROM GameDistributor")   
    rows = cursor.fetchall()   
    for row in rows:
        DistributorId = row[0]                   
        CompanyName= row[1]
        ContactFirstName= row[2]
        ContactLastName= row[3] 
        Phone= row[4]            
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_entity.py?entity={5}&GameDistributorID={0}">delete</a></p></td>
                   <td><input name="DistributorID{0}" type="number" min=1 placeholder={1}></td>
                   <td><input name="CompanyName{0}" type="text" placeholder={2}></td> 
                   <td><input name="ContactFirstName{0}" type="text" placeholder={3}></td> 
                   <td><input name="ContactLastName{0}" type="text" placeholder={4}></td>
                 </tr>
        """.format(DistributorId, CompanyName, ContactFirstName, ContactLastName, Phone, "Distributor")  
               
               
    #DistributorAddress
    print """
             </table>
           </div>
         </div>
       </div>
    </form>
     
    <form method="post" action="do_admin_update.py?entity={0}">               
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body"> 
            <table border="2">
              <ul id="ddd">Notes
                 <li id="ddd">Deletion is strongly discouraged.</li>
               </ul>
              <p id="ddd">(order by DistributorID, StartDate)</p>
               <tr>
                 <th>AddressID</th>
                 <th>GameDistributorID</th>
                 <th>StartDate</th>
                 <th>EndDate</th>
               </tr>
    """.format("GameDistributorAddress")
    cursor.execute("select * from GameDistributorAddress ORDER BY GameDistributorID, StartDate")  
    row = cursor.fetchone()   
    while row is not None:
        AddressID = row[0]     
        GameDistributorID = row[1]        
        StartDate = row[2]
        EndDate= row[3] 
                       
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={4}&GameDistributorID={1}&AddressID={0}">delete</a></p></td>
                   <td>{1}</td>
                   <td>{2}</td> 
                   <td>{3}</td>   
               </tr>
        """.format(AddressID,GameDistributorID,StartDate,EndDate,"GameDistributorAddress")  
        row = cursor.fetchone()  
                          
    #Address
    print """
             </table>
           </div>
         </div>
       </div>
    </form> 
    
    <form method="post" action="do_admin_update.py?entity={0}">  
       <div class="panel panel-default">
        <div class="panel-heading">        
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">   
            <table border="2">
               <tr>
                 <th>AddressID</th> 
                 <th>StreetNumber</th>
                 <th>StreetNumberSuffix</th>
                 <th>StreetName</th>
                 <th>StreetType</th>
                 <th>AddressType</th>
                 <th>AddressTypeIdentifier</th>
                 <th>MinorMunicipality</th>
                 <th>MajorMunicipality</th>
                 <th>GoverningDistrict</th>
                 <th>PostalArea</th>
                 <th>Country</th>
               </tr>
    """.format("Address")
    cursor.execute("select * from Address ORDER BY StreetNumber,StreetNumberSuffix,StreetName,StreetType,AddressType,AddressTypeIdentifier,MinorMunicipality,MajorMunicipality,GoverningDistrict,PostalArea,Country")  
    row = cursor.fetchone()   
    while row is not None:
    
        AddressID = row[0]                   
        StreetNumber= row[1]
        StreetNumberSuffix = row[2]
        StreetName = row[3]
        StreetType = row[4]
        AddressType =row[5]
        AddressTypeIdentifier = row[6]
        MinorMunicipality = row[7]
        MajorMunicipality = row[8]
        GoverningDistrict = row[9]
        PostalArea = row[10]
        Country    = row[11]
                       
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_entity.py?entity={12}&AddressID={0}">delete</a></p></td>
                   <td><input name="StreetNumber{0}" type="number" placeholder={1}></td>
                   <td><input name="StreetNumberSuffix{0}" type="text" placeholder="{2}"</td>
                   <td><input name="StreetName{0}" type="text" placeholder={3}></td>
                   <td><input name="StreetType{0}" type="text" placeholder={4}></td>
                   <td><input name="AddressType{0}" type="text" placeholder={5}></td>
                   <td><input name="AddressTypeIdentifier{0}" type="text" placeholder={6}></td> 
                   <td><input name="MinorMunicipality{0}" type="text" placeholder={7}></td>
                   <td><input name="MajorMunicipality{0}" type="text" placeholder={8}></td>
                   <td><input name="GoverningDistrict{0}" type="text" placeholder={9}></td>
                   <td><input name="PostalArea{0}" type="text" placeholder={10}></td>
                   <td><input name="Country{0}" type="text" placeholder={11}></td>
               </tr>
        """.format(AddressID, StreetNumber,StreetNumberSuffix,StreetName,StreetType,
                   AddressType,AddressTypeIdentifier,MinorMunicipality,MajorMunicipality,GoverningDistrict,PostalArea,Country,"Address")  
        row = cursor.fetchone()
        
        
    #InstanceRun
    print """
             </table>
           </div>
         </div>      
       </div>
    </form>          
    
    <form method="post" action="do_admin_update.py?entity={0}">
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <ul id="ddd">Notes
            <li id="ddd">To add a new instance run, log in with a supervisor account.</li>
             <li id="ddd">Deletion of an instance run leads to loss of relevant players, videos, achievements.</li>
            </ul>    
            <table border="2">
               <tr>
                 <th>InstanceRunID</th>
                 <th>SupervisorID</th>
                 <th>InstanceName</th> 
                 <th>TimeRecorded</th>
                 <th>Category</th>                
               </tr>
    """.format("InstanceRun")
    cursor.execute("SELECT * FROM InstanceRun")   
    rows = cursor.fetchall()   
    for row in rows:
        Id = row[0]                   
        SuperID = row[1]
        InstanceName = row[2]
        Time = row[3]
        Category = row[4]               
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={5}&InstanceRunID={0}&SupervisorID={1}">delete</a></p></td>
                   <td>{1}</td>
                   <td><input name="InstanceName{0}" type="text" placeholder={2}></td>               
                   <td><input name="RecordedTime{0}" class="date" placeholder={3} type="text" onfocus="(this.type='date')"></td>
                   <td><input name="CategoryNamw{0}" type="text" min=1 placeholder={4}></td>
                 </tr>
        """.format(Id, SuperID, InstanceName, Time, Category, "InstanceRun")             
    
    #InstanceRunPlayer
    print """
             </table>
           </div>
         </div>      
       </div>
    </form>          
    
    <form method="post" action="do_admin_update.py?entity={0}">
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">    
            <table border="2">
             <ul id="ddd">Notes
                <li id="ddd">To manage InstanceRunPlayer, log in with a supervisor account.</li>
             </ul>
               <tr>
                 <th>InstanceRunID</th>
                 <th>PlayerID</th>
                 <th>PerformanceNotes</th>                
               </tr>
    """.format("InstanceRunPlayer")
    cursor.execute("SELECT InstanceRunID, PlayerID, PerformanceNotes FROM InstanceRunPlayer Order by InstanceRunID")   
    rows = cursor.fetchall()   
    for row in rows:
        InstanceRunID= row[0]
        PlayerID= row[1]                   
        PerformanceNotes= row[2]              
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={3}&InstanceRunID={0}&PlayerID={1}">delete</a></p></td>
                   <td>{1}</td>
                   <td><textarea placeholder="{2}" name="PerformanceNotes{0}"></textarea></td>            
                 </tr>
        """.format(InstanceRunID,PlayerID, PerformanceNotes, "InstanceRunPlayer") 
        
        
    #Video
    print """
             </table>           
           </div>
         </div>
       </div>
     </form>
            
    <form method="post" action="do_admin_update.py?entity={0}">   
       <div class="panel panel-default">
        
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">            
            <table border="2">
             <ul id="ddd">Notes
             <li id="ddd">To add new videos, log in with a supervisor account.</li>
             <li id="ddd">Deletion of a video leads to loss of relevant order records.</li>
             </ul>
               <tr>
                 <th>VideoID</th>
                 <th>URL</th>
                 <th>Price</th> 
                 <th>VideoType</th>
                 <th>InstanceRunID</th>
                 <th>GameID</th>
               </tr>
    """.format("Video")
    cursor.execute("SELECT * FROM Video")   
    rows = cursor.fetchall()   
    for row in rows:
        Id = row[0]                   
        URL = row[1]
        Price = row[2]
        VideoType= row[3] 
        InstanceRunID= row[4]
        GameID= row[5]       
        print """
                 <tr>       
                   <td>{0}<p><a href="admin_del_ass.py?entity={6}&VideoID={0}&GameID={5}&InstanceRunID={4}">delete</a></p></td>
                   <td><input name="URL{0}" class="url" type="text" placeholder={1}></td>
                   <td><input name="Price{0}" type="number" min=0 placeholder={2}></td>               
                   <td><input name="VideoType{0}" type="text" placeholder="{3}"></td>
                   <td>{4}</td>
                   <td>{5}</td>
                 </tr>
        """.format(Id, URL, Price, VideoType, InstanceRunID, GameID, "Video") 
        
    #ViewerOrder
    print """
             </table>
           </div>
         </div>
       </div>
    </form>
    
    <form method="post" action="do_admin_update.py?entity={0}">    
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
               <tr>
                 <th>ViewerOrderID</th>
                 <th>OrderDate</th>
                 <th>ViewerID</th>
               </tr>
    """.format("ViewerOrder") 
    cursor.execute("""select * from ViewerOrder""")   
    rows = cursor.fetchall()   
    for row in rows:
        ViewerOrderID = row[0]                   
        OrderDate= row[1]
        ViewerID= row[2]   
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={3}&ViewerOrderID={0}&ViewerID={1}">delete</a></p></td>
                   <td><input name="OrderDate{0}" class="date" placeholder={1} type="text" onfocus="(this.type='date')"></td>
                   <td>{2}</td>      
                 </tr>
        """.format(ViewerOrderID , OrderDate, ViewerID, "ViewerOrder")

        
    #ViewerOrderLine
    print """
             </table>
           </div>
         </div>
       </div>
    </form>
    
    <form method="post" action="do_admin_update.py?entity={0}">    
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
               <tr>
                 <th>VideoID</th>
                 <th>ViewerOrderID</th>
                 <th>FlagPerk</th> 
                 <th>ViewedStatus</th>
               </tr>
    """.format("ViewerOrderLine") 
    cursor.execute("""select * from ViewerOrderLine""")   
    rows = cursor.fetchall()   
    for row in rows:
        VideoID =row[0]
        ViewerOrderID = row[1]                   
        FlagPerk=row[2]  
        ViewedStatus = row[3]
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_entity.py?entity={4}&VideoID={0}">delete</a></p></td>
                   <td>{1}</td>
                   <td><input name="FlagPerk{0}" type="text" placeholder={2}></td>    
                   <td><input name="ViewedStatus{0}" type="text" placeholder={3}></td>
                 </tr>
        """.format(VideoID,ViewerOrderID,FlagPerk,ViewedStatus,"ViewerOrderLine") 
               
    
    #Achievement
    print """
             </table>            
           </div>
         </div>
       </div>
    </form>
         
    <form method="post" action="do_admin_update.py?entity={0}">
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">                
            <table border="2">
            <ul id="ddd">Notes
             <li id="ddd">To add new achievements, log in with a supervisor account.</li>
            </ul>
               <tr>
                 <th>PlayerID</th>
                 <th>InstanceRunID</th>
                 <th>TimeAchieved</th> 
                 <th>AchievementName</th>
                 <th>RewardBody</th>
               </tr>
    """.format("Achievement")
    cursor.execute("SELECT * FROM Achievement")   
    rows = cursor.fetchall()   
    for row in rows:
        Id = row[0]                   
        InstanceRunID= row[1]
        Time= row[2]
        Name= row[3] 
        Reward = row[4]       
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={5}&PlayerID={0}&InstanceRunID={1}">delete</a></p></td>
                   <td><input name="InstanceRunID{0}" type="number" min=1 placeholder={1}></td>
                   <td><input name="Time{0}" class="date" placeholder={2} type="text" onfocus="(this.type='date')"></td>               
                   <td><input name="Name{0}" type="text" placeholder="{3}"></td>
                   <td><input name="Reward{0}" type="text" placeholder={4}></td>
                 </tr>
        """.format(Id, InstanceRunID, Time, Name, Reward,"Achievement")          

         
    
    #Game
    print """
            </table>           
           </div>
         </div>
       </div>
     </form>
        
        
    <form method="post" action="do_admin_update.py?entity={0}">
      <div class="panel panel-default">
        <div class="panel-heading">
        
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
       
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
               <ul id="ddd">Notes
               <li id="ddd">Deletion of a game leads to cascading deletions of all relevant videos, orders etc.</li>
               </ul>
               <tr>
                 <th>GameID</th>
                 <th>GameName</th>
                 <th>Genre</th> 
                 <th>Review</th>
                 <th>StarRating</th>
                 <th>ClassificationRating</th>
                 <th>PlatformNotes</th>
                 <th>PromotionLink</th>
                 <th>Cost</th>
               </tr>
    """.format("Game")
    
    cursor.execute("SELECT * FROM Game")   
    rows = cursor.fetchall()   
    for row in rows:
        Id = row[0]                   
        Game = row[1]
        Genre = row[2]
        Review = row[3] 
        Star = row[4]
        Classification = row[5]
        Platform = row[6]
        Promotion = row[7]
        Cost = row[8]
        
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_entity.py?entity={9}&GameID={0}">delete</a></p></td>
                   <td><input name="GameName{0}" type="text" placeholder={1}></td>
                   <td><input name="Genre{0}" type="text" placeholder={2}></td>
                   <td><textarea placeholder="{3}" name="Review{0}"></textarea></td>
                   <td><input name="StarRating{0}" type="number" min=0 max=5 placeholder={4}></td>
                   <td><input name="ClassificationRating{0}" type="text" placeholder={5}></td>
                   <td><input name="PlatformNotes{0}" type="text" placeholder={6}></td>
                   <td><input name="PromotionLink{0}" type="text" placeholder={7}></td>
                   <td><input name="Cost{0}" type="number" min=0 placeholder={8}></td>
                 </tr>
        """.format(Id, Game, Genre, Review, Star, Classification, Platform, Promotion, Cost, "Game") 
    
    #GameDistributorOrder
    print """
            </table>           
           </div>
         </div>
       </div>
     </form>
        
        
    <form method="post" action="do_admin_update.py?entity={0}">
      <div class="panel panel-default">
        <div class="panel-heading">
        
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
       
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
               <ul id="ddd">Notes
               <li id="ddd">Deletion of a game order leads to cascading deletions of all relevant order details.</li>
               </ul>
               <tr>
                 <th>GameDistributorOrderID</th>
                 <th>SupplyDate</th>
                 <th>GameDistributorID</th> 
               </tr>
    """.format("GameDistributorOrder")

    cursor.execute("SELECT * FROM GameDistributorOrder")   
    rows = cursor.fetchall()   
    for row in rows:
        GameDistributorOrderID = row[0]                   
        SupplyDate = row[1]
        GameDistributorID  = row[2] 
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={3}&GameDistributorOrderID={0}&GameDistributorID={2}">delete</a></p></td>
                   <td><input name="SupplyDate{0}" class="date" placeholder={1} type="text" onfocus="(this.type='date')"></td>
                   <td>{2}</td>
                 </tr>
        """.format(GameDistributorOrderID, SupplyDate, GameDistributorID, "GameDistributorOrder")    
        
    
    #OrderDetail
    print """
            </table>           
           </div>
         </div>
       </div>
     </form>
        
        
    <form method="post" action="do_admin_update.py?entity={0}">
      <div class="panel panel-default">
        <div class="panel-heading">
        
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
       
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
               <ul id="ddd">Notes
               <li id="ddd">Order details are added automatically when a new GameDistributorOrder is created.</li>
               </ul>
               <tr>
                 <th>GameDistributorOrderID</th>
                 <th>GameID</th>
                 <th>QuantityOrdered</th> 
                 <th>ActualUnitPrice</th>
               </tr>
    """.format("OrderDetail")

    cursor.execute("SELECT * FROM OrderDetail")   
    rows = cursor.fetchall()   
    for row in rows:
        GameDistributorOrderID = row[0]                   
        GameID = row[1]
        QuantityOrdered = row[2]
        ActualUniPrice = row[3] 
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={4}&GamedistributorOrderID={0}&GameID={1}">delete</a></p></td>
                   <td>{1}</td>
                   <td><input name="QuantityOrdered{0}" type="number" min=1 placeholder={2}></td>
                   <td><input name="ActualUniPrice{0}" type="number" min=0 placeholder={3}></td>
                 </tr>
        """.format(GameDistributorOrderID, GameID, QuantityOrdered, ActualUniPrice,"OrderDetail") 
    
     
        
    #GameShipment
    print """
            </table>           
           </div>
         </div>
       </div>
     </form>
        
        
    <form method="post" action="do_admin_update.py?entity={0}">
      <div class="panel panel-default">
        <div class="panel-heading">
        
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
       
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
               <ul id="ddd">Notes
               <li id="ddd">Deletion of a game shipment leads to cascading deletions of all relevant shipment details.</li>
               </ul>
               <tr>
                 <th>GameShipmentID</th>
                 <th>DateReceived</th>
                 <th>GameDistributorOrderID</th> 
               </tr>
    """.format("GameShipment")

    cursor.execute("SELECT * FROM GameShipment")   
    rows = cursor.fetchall()   
    for row in rows:
        GameShipmentID = row[0]                   
        DateReceived = row[1]
        GameDistributorOrderID  = row[2] 
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={3}&GameShipmentID={0}&GameDistributorOrderID={2}">delete</a></p></td>
                   <td><input name="DateReceived{0}" class="date" placeholder={1} type="text" onfocus="(this.type='date')"></td>
                   <td>{2}</td>
                 </tr>
        """.format(GameShipmentID, DateReceived, GameDistributorOrderID, "GameShipment")
        
    #GameShipmentDetail
    print """
            </table>           
           </div>
         </div>
       </div>
     </form>
        
        
    <form method="post" action="do_admin_update.py?entity={0}">
      <div class="panel panel-default">
        <div class="panel-heading">
        
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
       
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">
            <table border="2">
               <ul id="ddd">Notes
               <li id="ddd">Shipment details are added automatically when a new GameShipment is created.</li>
               </ul>
               <tr>
                 <th>GameID </th>
                 <th>GameShipmentID </th>
                 <th>QuantityReceived </th> 
               </tr>
    """.format("GameShipmentDetail")

    cursor.execute("SELECT * FROM GameShipmentDetail")   
    rows = cursor.fetchall()   
    for row in rows:
        GameID = row[0]
        GameShipmentID = row[1]                   
        QuantityReceived = row[2]
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={3}&GameID={0}&GameShipmentID={1}">delete</a></p></td>
                   <td>{1}</td>
                   <td><input name="QuantityReceived{0}" type="number" min=0 placeholder={2}></td>
                 </tr>
        """.format(GameID, GameShipmentID, QuantityReceived, "GameShipmentDetail")    

        
    #Venue
    print """
             </table>
           </div>
         </div>
       </div>
    </form>

    <form method="post" action="do_admin_update.py?entity={0}">    
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">           
            <table border="2">
              <ul id="ddd">Notes
               <li id="ddd">Deletion of a venue leads to loss relevant VenueEquipment records.</li>
              </ul>
               <tr>
                 <th>VenueID</th>
                 <th>VenueName</th>
                 <th>Description</th>
                 <th>PowerOutlets</th>
                 <th>LightingNotes</th>
                 <th>SupervisorID</th>
               </tr>
    """.format("Venue")
    cursor.execute("SELECT * FROM Venue")   
    rows = cursor.fetchall()   
    for row in rows:
        Id = row[0]                   
        Name= row[1]
        Description= row[2]
        Power= row[3] 
        Lighting= row[4]
        SuperID= row[5]       
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={6}&VenueID={0}&SupervisorID={5}">delete</a></p></td>
                   <td><input name="VenueName{0}" type="text" placeholder={1}></td>
                   <td><textarea placeholder="{2}" name="Description{0}"></textarea></td>
                   <td><input name="PowerOutlets{0}" type="number" min=0 placeholder={3}></td>
                   <td><input name="LightingNotes{0}" type="text" placeholder={4}></td>
                   <td><input name="SupervisorID{0}" type="number" min=1 placeholder={5}></td>
                 </tr>
        """.format(Id, Name, Description, Power, Lighting, SuperID, "Venue")  

    #VenueEquipment
    print """
             </table>
           </div>
         </div>
       </div>
    </form>
    
    <form method="post" action="do_admin_update.py?entity={0}">   
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">            
            <table border="2">
              <p id="ddd">(order by VenueID, EquipmentID)</p>
               <tr>
                 <th>VenueID</th>
                 <th>EquipmentID</th>
                 <th>FinancialYearStartingDate </th>
                 <th>SoftwareVersion </th>         
               </tr>
    """.format("VenueEquipment")
    cursor.execute("select * from VenueEquipment order by VenueID, EquipmentID")   
    rows = cursor.fetchall()   
    for row in rows:
        VenueID = row[0]
        EquipmentID = row[1] 
        FinancialYearStartingDate = row[2]
        SoftwareVersion = row[3]            
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_ass.py?entity={4}&EquipmentID={0}&VenueID={1}">delete</a></p></td>
                   <td>{1}</td>
                   <td><input name="FinacialYearStartingDate{0}" class="date" placeholder={2} type="text" onfocus="(this.type='date')"></td>
                   <td><input name="SoftwareVersion{0}" type="text" placeholder={3}></td>       
                 </tr>
        """.format(VenueID, EquipmentID , FinancialYearStartingDate, SoftwareVersion,"VenueEquipment") 
    
    #Equipment
    print """
             </table>
           </div>
         </div>
       </div>
    </form>
    
    <form method="post" action="do_admin_update.py?entity={0}">   
       <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            <a data-toggle="collapse" data-parent="#accordion" href="#{0}" class="collapsed">
              {0}
            </a>
            <a class="btn btn-default" href="admin_add_{0}.py">
              add
            </a>
            <input class="btn btn-default" type="reset" value="reset">
            <input class="btn btn-default" type="submit" value="commit">
          </h4>
        </div>
        <div id="{0}" class="panel-collapse collapse" style="height: 0px;">
          <div class="panel-body">            
            <table border="2">
               <ul id="ddd">Notes
               <li id="ddd">Deletion of a equipment leads to cascading deletions of all relevant venue equipment records.</li>
               </ul>
               <tr>
                 <th>EquipmentID</th>
                 <th>ModelAndMake</th>
                 <th>EquipmentReview</th> 
                 <th>ProcessorSpeed</th>          
               </tr>
    """.format("Equipment")
    cursor.execute("select * from Equipment")   
    rows = cursor.fetchall()   
    for row in rows:
        EquipmentID = row[0]       
        ModelAndMake= row[1]
        EquipmentReview= row[2]
        ProcessorSpeed= row[3]         
        print """
                 <tr>
                   <td>{0}<p><a href="admin_del_entity.py?entity={4}&EquipmentID={0}">delete</a></p></td>
                   <td><input name="ModelAndMake{0}" type="text" placeholder={1}></td>
                   <td><textarea placeholder="{2}" name="EquipmentReview{0}"></textarea></td>
                   <td><input name="ProcessorSpeed{0}" type="number" min=0 placeholder={3}></td>       
                 </tr>
        """.format(EquipmentID,ModelAndMake,EquipmentReview,ProcessorSpeed,"Equipment")                
             
    print """
              </table>
            </div>
          </div>
        </div>
    </form>
    """

print """
    
</div>
"""
utility.footer()
       
                   
# close after use
db.close()
