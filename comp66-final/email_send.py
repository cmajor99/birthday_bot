import smtplib
#import Scraper_File_Name

# Used for testing
# choice = input('What is your email address?\n')
def emailSequence(fname,lname,email):
    receiver = email

    content = 'Happy birthday %s %s! I hope you  have a great day filled with lots of fun and laughter.'%(fname,lname)

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('pythongroupproject19@gmail.com', 'Python1234')

    mail.sendmail('pythongroupproject@gmail.com', receiver, content)

    mail.close()