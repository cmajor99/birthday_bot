import MySQLdb

mydb = MySQLdb.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="pythonproject"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE (friends VARCHAR(255)")
mycursor.execute("ALTER TABLE friends ADD COLUMN friendsID INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("ALTER TABLE friends ADD COLUMN friendsName VARCHAR(255)")
mycursor.execute("ALTER TABLE friends ADD COLUMN friendsNumber INT")
mycursor.execute("ALTER TABLE friends ADD COLUMN friendsEmail VARCHAR(255)")
mycursor.execute("ALTER TABLE friends ADD COLUMN friendsFacebook VARCHAR(255)")

sql = "INSERT INTO friends (friendsName,friendsNumber,friendsFacebook ) VALUES (%s, %s, %s, %s)"
val = [
    ("Joseph", "6138705888","joseph.guindon@student.sl.on.ca","https://www.facebook.com/joey.guindon.9"),
    ("Cory", "6133629506","cory.major@student.sl.on.ca","https://www.facebook.com/CoryMajor72"),
    ("Ryan","ENTERNUMBERHERE","ryan.steele@student.sl.on.ca","https://www.facebook.com/profile.php?id=100009757061339"),
    ("Joel", "ENTERNUMBERHERE","joel.leger@student.sl.on.ca","https://www.facebook.com/TechyJ"),
    ("Robert", "ENTERNUMBERHERE","iothore.wheesk@student.sl.on.ca","https://www.facebook.com/profile.php?id=100009973901865")
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


sql_select_Query = "select of "