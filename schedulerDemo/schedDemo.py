__author__ = 'Administrator'

"this is a scheduler demo"

from random import randint
import sched, time

schedObj = sched.scheduler()


def everyDayFetchWeather():
    weatherList = ['sun', 'rain', 'cloud', 'fog']
    print("today is {0}".format(weatherList[randint(0, len(weatherList) - 1)]), time.time())


def start():
    while True:
        print("start:", time.time())
        schedObj.enter(10, 1, everyDayFetchWeather)
        schedObj.enter(5, 1, everyDayFetchWeather)
        schedObj.enter(15, 3, everyDayFetchWeather)
        schedObj.run()
        print("end: ", time.time())

if __name__ == '__main__':
    start()
