import smtplib

choice = input('What is your email address?\n')

content = 'You have X friends who have birthdays today. They are InsertNameVariableHere'

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('pythongroupproject19@gmail.com', 'Python1234')

mail.sendmail('pythongroupproject@gmail.com', choice, content)

mail.close()