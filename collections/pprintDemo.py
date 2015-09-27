__author__ = 'luowen'

""" pprint demos """

from urllib.request import  urlopen

# get baidu content
with urlopen('http://www.baidu.com') as url:
    urlinfo = url.info()
    encode = urlinfo.get_content_charset()
    rawData = url.read().decode(encode)
