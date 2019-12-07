import schedule, time

def dailyexec():
    print('Checking for birthdays...')
    return

schedule.every().day.at("09:00").do(dailyexec)

# if dailyexec gets a value
# store in variable

while True:
    schedule.run_pending()
    time.sleep(5)
    # Output variable "There are x birthdays today. Wish them happy birthday"