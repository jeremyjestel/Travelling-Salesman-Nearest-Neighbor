from math import floor


def miles_time(miles):
    hours = miles / 18
    return hours

def to_minutes(time):
    time = list(time)
    if len(time) == 4:
        hours = int(time[0])
        min = int(time[2] + time[3])
    else:
        hours = int(time[0] + time[1])
        min = int(time[3] + time[4])
    minutes = (hours * 60 + min) - 480
    return minutes

def to_str(tmp_hours):
    start = 8
    hours = floor(tmp_hours)
    minutes = (tmp_hours - hours) * 60
    hours += start
    hour = str(hours)
    min = int(minutes)
    if min < 10:
        min = "0" +str(min)
    else:
        min = str(min)
    return hour + ":" + min

