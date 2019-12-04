import MySQLdb
import requests,urllib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import timedelta
import datetime

import os


def fetch_birthdays(text_data):
	try:
		print(' ')
		print('-- Creating birthday list --')
		text = text_data.split('BEGIN:VEVENT')
		# Initializing value for id.
		id = 1000
		# This list element is a list of lists and will store all birthdays as individual lists
		birthday_list=[]
		# Looping through each birthday
		for i in range(1, len(text)):
			# Fetching each birthday as a element of list
			lines=text[i].split('\r\n')
			# Fetching DTSTART element of calendar file
			dtstart=(lines[1].split(':'))[1]
			# Splitting DTSTART into YYYY MM DD components
			bday_year = dtstart[0:4]
			bday_month = dtstart[4:6]
			bday_date = dtstart[6:8]
			# Fetching SUMMARY element of calendar file
			summary = lines[2].split(':')[1].split("'s birthday")[0]
			name = summary.split(' ')
			# Fetch first, middle, last names and their space(' ') adjustments
			if len(name) == 0:
				pass
			elif len(name) == 1:
				first_name = name[0]
				middle_name = ''
				last_name = ''
			elif len(name) == 2:
				first_name = name[0]
				middle_name = ' '
				last_name = name[1]
			elif len(name) == 3:
				first_name = name[0]
				middle_name = ' '+name[1]+' '
				last_name = name[2]
			else:
				first_name = name[0]
				middle_name = ' '+name[1]+' '
				last_name = ''
				for j in range(2, len(name)):
					last_name += name[j]+' '
				last_name = last_name[0:-1]
# Fetch uid element from calendar file
			uid = lines[5].split(':')[1].split('@facebook.com')[0]
			profile_id = uid[1:]
			
# Creating a list for this birthday
			line_data_list = [id+i, bday_year, bday_month, bday_date, first_name, middle_name, last_name, profile_id]
# Adding this list to parent birthday list
			birthday_list.append(line_data_list)
		print('-- Birthday List created successfully --')
		return birthday_list
	finally:
		pass

