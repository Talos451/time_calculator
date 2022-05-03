
def add_time(start_time, time_to_add,  day = None):    
    day_counter = 0
    days_of_week_counter = 0
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_time = start_time.split()
    am_or_pm = start_time[1]       
    start_time = start_time[0].split(':')
    start_time_hour = int(start_time[0])
    start_time_minute = int(start_time[1])

    time_to_add = time_to_add.split(':')
    time_to_add_hour = int(time_to_add[0])
    time_to_add_minute = int(time_to_add[1])
    
    half_day_counter = 0
    while (time_to_add_hour) >= 12:
        time_to_add_hour -= 12
        half_day_counter += 1
    

    added_time_hour = (int(start_time_hour) + int(time_to_add_hour))
    added_time_minute = (int(start_time_minute) + int(time_to_add_minute))

    if int(added_time_minute) > 60:
        added_time_minute = ((added_time_minute) - 60)
        added_time_hour += 1

    if (added_time_hour) > 11:
        if am_or_pm == 'PM':        #sets wheather its AM or PM
            am_or_pm = 'AM'
            day_counter += 1
        else:
            am_or_pm = 'PM'

    if added_time_hour > 12:                #subtract 12 to reset clock to the 12 hour system
        added_time_hour -= 12

    if half_day_counter % 2 != 0:
        if am_or_pm == 'PM':        #sets wheather its AM or PM bases on number of half day counters
            am_or_pm = 'AM'
            day_counter += (half_day_counter - 1) / 2 + 1
        else:
            am_or_pm = 'PM'
            day_counter += (half_day_counter - 1) / 2
    else:
            day_counter += (half_day_counter) / 2

    if day is not None:
        day_of_week = day.title()   
        days_of_week_counter = day_counter % 7 
        day_of_week_index = days_of_week.index(day_of_week)

    while days_of_week_counter > 0:
        if day_of_week == days_of_week[6]:
            day_of_week = days_of_week[0]
        else:
            day_of_week_index += 1
            day_of_week = days_of_week[day_of_week_index]
        days_of_week_counter -= 1
    if day_counter < 1:
        if day is not None:
            return (f"{str(added_time_hour).rjust(1, '0')}:{str(added_time_minute).rjust(2, '0')} {am_or_pm}, {day_of_week}")    
        return (f"{str(added_time_hour).rjust(1, '0')}:{str(added_time_minute).rjust(2, '0')} {am_or_pm}")
    elif day_counter == 1:
        if day is not None: 
            return (f"{str(added_time_hour)}:{str(added_time_minute).rjust(2, '0')} {am_or_pm}, {day_of_week} (next day)")
        return (f"{str(added_time_hour)}:{str(added_time_minute).rjust(2, '0')} {am_or_pm} (next day)")
    else:
        if day is not None:
            return (f"{str(added_time_hour)}:{str(added_time_minute).rjust(2, '0')} {am_or_pm}, {day_of_week} ({int(day_counter)} days later)")
        return (f"{str(added_time_hour)}:{str(added_time_minute).rjust(2, '0')} {am_or_pm} ({int(day_counter)} days later)")        



print(add_time("11:06 PM", "2:02", "Monday"))