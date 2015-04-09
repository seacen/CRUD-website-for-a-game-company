import MySQLdb

def delete(cur_name,key1,key2)

cur_name=form["entity"].value

try:           
    cursor.execute("""delete from {0} where {1}={2} and {3}={4}""".format(cur_name,key1[0],key1[1],key2[0],key2[1]))
    db.commit()
except:
    db.rollback()