from gcsa.google_calendar import GoogleCalendar

# https://github.com/jignesh13/googlecalendar
# https://github.com/kuzmoyev/beautiful-date
calendar = GoogleCalendar('kareemassad5@gmail.com')
for event in calendar:
    print(event)