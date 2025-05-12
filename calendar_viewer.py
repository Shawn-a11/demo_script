import calendar

def calendar_viewer():
    year = int(input("Enter the year (example:'2025'):"))
    month = int(input("Enter the month (1-12):"))

    print(calendar.month(year,month))
        

calendar_viewer() 