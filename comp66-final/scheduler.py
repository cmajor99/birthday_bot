from main import mainFunc
import schedule, time

def dailyexec():
    print('Checking for birthdays...')
    return

schedule.every().day.at("20:00").do(dailyexec)
schedule.every().day.at("20:00").do(mainFunc)

# if dailyexec gets a value
# store in variable

while True:
    schedule.run_pending()
    time.sleep(5)
    # Output variable "There are x birthdays today. Wish them happy birthday"