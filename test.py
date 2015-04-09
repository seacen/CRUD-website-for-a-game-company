import sys,MySQLdb

db = MySQLdb.connect("info20003db.eng.unimelb.edu.au", "info20003g15", "info20003g15_2014", "info20003g15", 3306)
cursor = db.cursor()

q = "insert into UserAccount \
        Values (default,'55','55','V')"


cursor.execute ("""select * from (Viewer natural left outer join PremiumViewer) natural left outer join CrowdFundingViewer
""")
rows=cursor.fetchall()
print rows
