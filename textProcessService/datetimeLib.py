__author__ = 'Administrator'

"""
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
"""

from datetime import date, time, datetime, timedelta, tzinfo



# timedelta object
print("-------- date object ------")
tdl = timedelta(days=2, seconds=22, microseconds=2, milliseconds=3)
print(tdl.days)
print(tdl.seconds)
print(tdl.microseconds)



# date object
print("-------- date object ------")
dateValue = date(2015, 9, 25)

print(dateValue.isoformat())
print(dateValue.isocalendar())
print(dateValue.isoweekday())

print(dateValue.ctime())
print(dateValue.weekday())
print(dateValue.replace(year=2232))

# datetime object
print("-------- datetime object ------")

datetimeValue = datetime(2013, 9, 25, 16, 37, 45)

timeValue = datetimeValue.time()

print(timeValue.hour)
print('----------xxxxxxxxxxxxxx-----------')
print(datetimeValue)
print(datetimeValue.isoformat())
print(datetimeValue.isocalendar())
print(datetimeValue.isoweekday())

print(datetimeValue.timestamp())

print(datetime.now())
print(datetime.today())


class PRC(tzinfo):
    """ define PRC timeZone """

    def utcoffset(self, dt):
        return timedelta(hours=8) + self.dst(dt)
    def dst(self, dt):
        return timedelta(hours=0)
    def tzname(self, dt):
        return "Asia/Shanghai"


tzPrc = PRC()
datetimeValue = datetime(year=2015, month=9, day=25, hour=17, minute=0, second=0, tzinfo=tzPrc)
print(datetimeValue.tzname())
dateValue = datetimeValue.date()
print(datetimeValue.tzname())
timeValue = time(tzinfo=datetimeValue.tzinfo)
print(timeValue.tzname())