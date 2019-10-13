"""
You prefer a good old 12-hour time format. 
But the modern world we live in would rather use the 24-hour format and you see it everywhere. 
Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format.
"""

import re

def time_converter(time):
    time = re.sub(':', '',time)
    am = True
    hours = time[0:2]
    hours = re.sub('^0', '',hours)
    minutes =  time[2:4]
    
    if int(hours) >= 12:
        am = False
        if int(minutes) > 0:
            if int(hours) > 12:
                hours = int(hours) - 12
    elif int(hours) == 0:
        hours = 12
            
    string = (
              "{}:{} p.m.".format(hours, minutes), 
              "{}:{} a.m.".format(hours, minutes)
              )[ am == True ]
    #replace this for solution
    return string

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("00:00")
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")



def time_converter(time):
    h, m = map(int, time.split(':'))
    if h < 12:
        ampm = 'a.m.'
    else:
        ampm = 'p.m.'
    if h > 12:
        h -= 12
    elif h == 0:
        h = 12
    return '%d:%02d %s' % (h, m, ampm)