from math import floor


def miles_time(miles):
    hours = miles / 18
    return hours


def to_time(tmp_hours):
    start = 8
    hours = floor(tmp_hours)
    minutes = (tmp_hours - hours) * 60
    hours += start
    hour = str(hours)
    min = int(minutes)
    if min < 10:
        min = "0" +str(min)
    return hour + ":" + min

