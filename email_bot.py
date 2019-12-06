import smtplib
import Scraper_File_Name

# Used for testing
# choice = input('What is your email address?\n')

email = Scraped_Email_Variable_Here

content = 'Happy birthday %s! I hope you  have a great day filled with lots of fun and laughter.'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('pythongroupproject19@gmail.com', 'Python1234')

mail.sendmail('pythongroupproject@gmail.com', email, content)

mail.close()