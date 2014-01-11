import datetime

def get_todays_date():
    # get today's date
    now = datetime.datetime.now()
    # parse out the date
    month = now.month
    day = now.day
    year = now.day
    # put year, month, and day into a list to pass on
    todays_date = [year, month, day]
    return todays_date

def convert_to_julian(todays_date):
    todays_julian = 0
    todays_year = todays_date[0]
    todays_month = todays_date[1] - 1 # sets the month to match the list of days_in_months
    todays_day = todays_date[2]
    i = 0

    # list of number of days in each month in a leap year
    days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # if the year is a leap year
    if todays_year % 4 == 0:
        while i < todays_month:
            todays_julian += days_in_months[i]
            i += 1
    # if the year is not a leap year
    else:
        days_in_months[1] = 28
        while i < todays_month:
            todays_julian += days_in_months[i]
            i += 1

    # add in the days from the current month
    todays_julian += todays_day
    return todays_julian

def todays_julian_date():
    todays_date = get_todays_date()
    julian_date = convert_to_julian(todays_date)

    # turn into a three-digit number
    julian_date = str(julian_date)
    if len(julian_date)  == 1:
        julian_date = "00" + julian_date
    elif len(julian_date) == 2:
        julian_date = "0" + julian_date

    return julian_date

todays_julian_date()