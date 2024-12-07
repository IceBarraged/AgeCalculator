from datetime import datetime, date


def DateDiff(date1,date2):
    return abs(date2-date1).days

def main():
    today = date.today()
    try:
            calcdate = input("Enter your date of birth (yyyy/mm/dd):\n")
            year, month, day = map(int, calcdate.split('/'))
            formatteddate = date(year, month, day)
            difference = DateDiff(formatteddate, today)
            print(difference)
            years = int(difference/365)
            months = int((difference%365)/30)
            days = int((difference%365)%30)
            print("You are ",years,"years, ",months,"months, and ",days,"days old.")

    except:
        print("Date not formatted correctly.")
main()
