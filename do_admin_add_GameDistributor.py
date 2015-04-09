# Import the CGI moduleWork
import cgi, MySQLdb,utility,session,sys


sess = session.Session(expires=20*60, cookie_path='/')
# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

info=sess.data
loggedIn = info.get("loggedIn")

if not loggedIn or sess.data.get("UserType")!="A":    
    utility.redirect("login.py")
    sys.exit(0)
          
    
form = cgi.FieldStorage()
    
# connect to db
db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)  

    
cursor=db.cursor()

cursor.execute("""show columns from GameDistributor""")

rows=cursor.fetchall()

cursor.execute("""insert into GameDistributor values (default,'{0}','{1}','{2}',{3})""".format(form.getvalue(rows[1][0]),form.getvalue(rows[2][0]),form.getvalue(rows[3][0]),form.getvalue(rows[4][0])))
cursor.execute("""set @EID=LAST_INSERT_ID()""")
cursor.execute("""select @EID""")

dis_id=cursor.fetchone()[0]

cursor.execute("""show columns from Address""")
    
rows=cursor.fetchall()
address=''
info=[]
for row in rows:
    if row[0]!="AddressID":
        print form.getvalue(row[0])
        if not form.getvalue(row[0]):
            address+="None"
        else:
            address+=form.getvalue(row[0])
        info.append(form.getvalue(row[0]))
            
cursor.execute("""select * from Address""")
rows=cursor.fetchall()
    
dbadds=[]
for row in rows:
    dbadd=''
    id=row[0]
    for attri in row[1:]:
        if type(attri)==int:
            dbadd+=str(attri)
        elif attri==None:
            dbadd+="None"
        else:
            dbadd+=attri
    dbadds.append((id,dbadd))
match=0
for add in dbadds:
    if add[1]==address:
        Add_id=add[0]
        match=1
        
        
        
if not match:
    cursor.execute("""insert into Address values (default,'{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')""".format(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],info[10]))
    cursor.execute("""set @EID=LAST_INSERT_ID()""")
    cursor.execute("""select @EID""")
    Add_id=cursor.fetchone()[0]
        
cursor.execute("""insert into GameDistributorAddress values ({0},{1},CURDATE(),default)""".format(Add_id,dis_id))
db.commit()

utility.redirect("admin_add_GameDistributor.py")