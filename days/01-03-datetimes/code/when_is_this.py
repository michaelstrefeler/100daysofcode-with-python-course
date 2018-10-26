# when_is_this.py
# A python script that shows the difference between two dates

from datetime import date
import re

today = date.today()
user_date = input('Enter a valid date: ')
is_valid = False

# Makes sure user inputs a valid date
# For example 31.09.2018 will not work because September has 30 days
while is_valid is False:
    while not re.match(r'^\d{2}.\d{2}.\d{4}$', user_date):
        print('Invalid synthax. Enter a valid date (DD/MM/YYYY)')
        user_date = input('Enter a valid date: ')

    day, month, year = user_date.split()

    try:
        user_date = date(int(year), int(month), int(day))
        is_valid = True
    except ValueError:
        print('Invalid date. Try again')
        user_date = input('Enter a valid date: ')

difference = (user_date - today).days
user_date = user_date.strftime('%A, %B %d %Y')

# Adds the right suffix to the dates
if user_date[-7:-5].endswith('1'):
    user_date = user_date[:-5] + 'st' + user_date[-5:]
elif user_date[-7:-5].endswith('2'):
    user_date = user_date[:-5] + 'nd' + user_date[-5:]
elif user_date[-7:-5].endswith('3'):
    user_date = user_date[:-5] + 'rd' + user_date[-5:]
else:
    user_date = user_date[:-5] + 'th' + user_date[-5:]

# Checks if user_date is today, in the past or in the future
if difference == 0:
    print('Today is {user_date}')
elif difference < 0:
    print(f'{user_date} was {str(difference)[1:]} days ago')
else:
    print(f'There are {difference} days until {user_date}')
