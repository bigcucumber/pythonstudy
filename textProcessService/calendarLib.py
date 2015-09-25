__author__ = 'Administrator'

""" Canlendar Lib reference """

from calendar import HTMLCalendar, TextCalendar

htmlCanlendar = HTMLCalendar()

resultSet = htmlCanlendar.formatmonth(theyear=2014, themonth=12)
print(resultSet)

with open('canlendarHtml.html', 'w', encoding='utf-8') as f:
    f.writelines(resultSet)
    f.close()

textCanlendar = TextCalendar()

resultSet = textCanlendar.formatmonth(theyear=2015, themonth=9)
print(resultSet)

with open('canlendarText.txt', 'w', encoding="utf-8") as f:
    f.writelines(resultSet)
    f.close()



