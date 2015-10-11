__author__ = 'luowen'

from html.parser import HTMLParser

class MYHTMLParser(HTMLParser):
    "customer html parser class"

    def handle_starttag(self, tag, attrs):
        print("start tag:", tag, attrs)

    def handle_endtag(self, tag):
        print("end tag:", tag)

    def handle_data(self, data):
        print("data: ", data)

    def handle_comment(self, data):
        print("comment:", data)

htmlParser = MYHTMLParser()
htmlString = """
<!doctype html>
<html
    <head>
        <title> haha </title>
        <meta charset="utf-8">
    </head>
    <body>
    <h1> haha </h1>
    <div>
        <img src="http://www.google.com/static/img1/logo.jpg">
        <ul>
            <li> menu1 </li>
            <li> menu2 </li>
            <li> menu3 </li>
            <li> menu4 </li>
        </ul>
    </div>
    </body>
</html>
"""

resultSet = htmlParser.feed(htmlString)

#resultSet = htmlParser.get_starttag_text()
#print(resultSet)


