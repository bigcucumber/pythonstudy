__author__ = 'luowen'

"This module provides various time-related functions"

import time

altzoneValue = time.altzone
print(altzoneValue)

asctimeValue = time.asctime()
print(asctimeValue)

clockValue = time.clock()
print(clockValue)

daylightValue = time.daylight
print(daylightValue)

localtimeValue =time.localtime()
print(localtimeValue)  # get local time stamp

mtimevalue = time.gmtime()
print(mtimevalue)  # get time europe time stamp

formatTimeValue = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatTimeValue)  # print  2015-10-05 20:31:52

# get unix timestamp
timeStampValue = time.time()
print(timeStampValue)  # get the unix timestamp

timezoneValue = time.tzname
print(timezoneValue)  # get time zone tuple
