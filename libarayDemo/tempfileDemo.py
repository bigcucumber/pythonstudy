__author__ = 'luowen'

" the tempfile libaray"
import tempfile

tempDir = tempfile.gettempdir()  # get the system temp directory path

tempfileHandle = tempfile.TemporaryFile()  # create a temp file

tempfileHandle.write("haah".encode())
tempfileHandle.seek(0)
content = tempfileHandle.read()
print(content)
tempfileHandle.close()


# content manager example
with tempfile.TemporaryDirectory() as directory:
    print(directory)


