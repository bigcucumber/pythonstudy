__author__ = 'Administrator'

from urllib import request
import re

urlAddress = "http://1111.ip138.com/ic.asp"

ip = ""
fromWhere = ""
with request.urlopen(urlAddress) as urlHandle:
    for line in urlHandle:
        matchObj = re.search(u"\<center\>.*\<\/center\>", line.decode('gbk'))  # 需要过去页面的编码,不然编码出错获取不到
        if matchObj is not None:
            string = matchObj.group()
            ipCompileObj = re.compile(r"\d*\.\d*\.\d*\.\d", re.UNICODE)
            fromCompileObj = re.compile(r"来自(.*)\<", re.LOCALE)
            matchIp = ipCompileObj.search(string)
            matchFrom = fromCompileObj.search(string)
            if matchIp is not None:
                ip = matchIp.group()
            if matchFrom is not None:
                resultSet = matchFrom.group()
                fromWhere = resultSet[3: len(resultSet) - 1]
print(ip)
print(fromWhere)

