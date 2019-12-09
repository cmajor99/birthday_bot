#Ryan Steele - 4291461
from functools import reduce
import operator
import mysql.connector

db_in_use = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="04041963@Win",
  database="friendsBirthdays",
  auth_plugin='mysql_native_password'
)
mycursor = db_in_use.cursor()

def unpackTuple(tup):  
    return (reduce(operator.add, tup))

#creating a list out of tuple list returned from query
#might turn into function
def birthdayCheck():
    #creating dynamically sized variable for iteration of the DB
    mycursor.execute("SELECT friendFname,friendLname FROM newFriends" )
    db_size = int(len(mycursor.fetchall()))
    blank = []
    for x in range(1,(db_size+1)):
        mycursor.execute(f"SELECT friendFname,friendLname FROM newFriends WHERE idfriends={x}" )
        myresult = mycursor.fetchone()
        blank.append(myresult)
    return blank

def grabEmail(fname,lname):
    blank_holder = []
    mycursor.execute(f"SELECT friend_email FROM newFriends WHERE friendFname='{fname}' AND friendLname='{lname}'")
    email_grab = mycursor.fetchone()
    unpck_email = unpackTuple(email_grab)

    if unpck_email is not None:
        return email_grab[0]
    else:
        return blank_holder

def grabPhone(fname,lname):
    blank_holder = []
    mycursor.execute(f"SELECT friend_phone FROM newFriends WHERE friendFname='{fname}' AND friendLname='{lname}'")
    phone_grab = mycursor.fetchone()
    unpck_phone = unpackTuple(phone_grab)

    if unpck_phone is not None:
        return phone_grab[0]
    else:
        return blank_holder
