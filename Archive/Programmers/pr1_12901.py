from datetime import datetime
def solution(a, b):
    months = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    date = datetime.strptime('2016-'+str(a)+"-"+str(b),"%Y-%m-%d")
    return months[date.weekday()]