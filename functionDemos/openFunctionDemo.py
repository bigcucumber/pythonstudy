__author__ = 'luowen'
"""
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	open for exclusive creation, failing if the file already exists
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newlines mode (deprecated)
"""
# open file and return a corresponding file object.

f = open('minFunctionDemo.py', 'r')

content = f.readlines()  # read file content and print
print(content)
f.close()  # close file handle

# anther method to read file
with open("minFunctionDemo.py") as f:
    print(f.read())
    f.close()
