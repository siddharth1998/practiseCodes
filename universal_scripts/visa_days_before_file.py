# coding: utf-8
import datetime
import traceback

print(
    "Code to determine when I can begin visa-related tasks, considering if there is a restriction on starting a certain number of days before expiry."
)

if __name__ == "__main__":
    # Create the end date object
    try:

        year = int(input("Please input the year of expiry :: "))
        if year < datetime.datetime.now().year:
            raise ValueError("How can year be less than this year ???")
        month = int(input("Please input the month of expiry :: "))
        day = int(input("Please input the day of expiry :: "))

    except Exception as e:

        print(e)
        traceback.print_exc()
        exit(1)

    end = datetime.datetime(year, month, day)

    # Calculating the end date delta
    try:

        days_before = int(input("\n \n \n How many days before left :: "))

        can_start = end - datetime.timedelta(days=days_before)

        print("\n \n \nYou can start the process around :: ", can_start.strftime("%Y-%m-%d"),"\n \n \n")

    except Exception as e:

        print(e)
        exit(1)
