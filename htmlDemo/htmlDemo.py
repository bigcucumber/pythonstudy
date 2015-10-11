__author__ = 'luowen'
"this is a html modules demo"
import html

htmlString = """
<!doctype html>
<html>
    <head>
        <title> this is a demo </title>
        <meta charset="utf-8">
    </head>
    <body>
    <h1> Html Demo </h1>
    </body>
</html>
"""

escapeHtmlString = html.escape(htmlString)
print(escapeHtmlString)  # escape html string

unescapeHtmlString = html.unescape(escapeHtmlString)
print(unescapeHtmlString)  # undo escape html string