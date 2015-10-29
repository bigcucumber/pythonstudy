def main():
    import requests, re
    url = "http://1111.ip138.com/ic.asp"
    resultSet = requests.get(url).text
    matchObj = re.search(r"\d*\.\d*\.\d*\.\d*", resultSet)
    if matchObj is not None:
        print(matchObj.group())
    else:
        print("ip not fetch from internet.")
if __name__ == "__main__":
    main()
