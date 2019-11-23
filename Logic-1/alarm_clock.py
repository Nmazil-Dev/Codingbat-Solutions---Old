def alarm_clock(day, vacation):
    if day == 6 and vacation or day == 0 and vacation:
        return "off"
    elif day == 6 and not vacation or day == 0 and not vacation:
        return '10:00'
    elif day in range(1, 6) and vacation:
        return '10:00'
    else:
        return '7:00'