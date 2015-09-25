__author__ = 'Administrator'

""" The textwrap module provides some convenience functions, as well as TextWrapper """

# wrap method
import textwrap, re


# wrap method
resultSetList = []
with open('reLib.py', 'r', encoding='utf-8') as f:
    for line in f:
        if re.match('^$', line):
            continue
        resultSet = textwrap.wrap(line, 25)
        resultSetList.append("\r".join(resultSet))

""" # write format string to format.txt
with open('format.txt', 'w', encoding="utf-8") as f:
    for line in resultSetList:
        f.write(line)
    f.close()
"""

# fill method same as "\n".join(wrap(text, ...))

string = "luowen"
resultSet = textwrap.fill(string, 5)
print(resultSet)


# shorten

string = "luowen"
resultSet = textwrap.shorten(string, width=3, placeholder="...")
print(resultSet)

