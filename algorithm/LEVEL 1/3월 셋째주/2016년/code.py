import datetime
import time

def solution(a, b):
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return week[datetime.date(2016,a,b).weekday()]
