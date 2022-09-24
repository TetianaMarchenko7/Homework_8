from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(user_list):

    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    list=defaultdict(list)

    today = datetime.now()
    day_number=today.weekday()

    if day_number in [0, 1 , 2, 3, 4]:
        start_interval=datetime(today.year, today.month, today.day) + timedelta(days=(5-day_number))
    elif day_number in [5, 6]:
        start_interval=datetime(today.year, today.month, today.day) - timedelta(days=(day_number-5))

    end_interval=start_interval + timedelta(days=7)

    for person in user_list:

        new_date=datetime(today.year, person["birthday"].month, person["birthday"].day)  
    
        if new_date >= start_interval and new_date <= end_interval:
            if new_date.weekday() in [0, 5, 6]:
                list["Monday"].append(person["name"])
            elif new_date.weekday()==1:
                list["Tuesday"].append(person["name"])
            elif new_date.weekday()==2:
                list["Wednesday"].append(person["name"])
            elif new_date.weekday()==3:
                list["Thursday"].append(person["name"])
            elif new_date.weekday()==4:
                list["Friday"].append(person["name"])

    for i in days:
        if list[i] != []:
            print(f"{i}: {', '.join(list[i])}")


if __name__='__main__'

    user_list=[{"name":"Jane", "birthday":datetime(2009, 9, 24)}, {"name":"Dima", "birthday":datetime(2013, 9, 29)}, {"name":"Ira", "birthday":datetime(1978, 9, 29)}]
    
    get_birthdays_per_week(user_list)
