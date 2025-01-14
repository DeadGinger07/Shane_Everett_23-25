from tkinter import Tk, Canvas
#Date and time used in application
from datetime import date, datetime

#Gets events
def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
        return list_events

# Determines days between dates
def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

#Used to display something on screen
root = Tk()
c = Canvas(root, width = 800, height = 800, bg = 'black')
c.pack()
c.create_text(100, 50, anchor = 'w', fill = '#33FF33', \
              font = 'Arial 20 bold underline', text = 'My 23-24 Countdown Calendar')

#gets events from computer
events = get_events()
today = date.today()

vertical_space = 100
events.sort(key=lambda x: x[1])

for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = 'It is %s days until %s' % (days_until, event_name)
    c.create_text(100, vertical_space, anchor = 'w', fill = '#33FF33', \
              font = 'Arial 14 bold', text = display)
    vertical_space = vertical_space + 20
