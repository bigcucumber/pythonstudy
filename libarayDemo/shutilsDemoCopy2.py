__author__ = 'Administrator'

import shutil, pathlib, time

# copyfileobj method

srcFileObj = open('./shutilsDemo.py', mode='r', encoding='utf-8')
destFileObj = open('./shutilsDemoCopy.py', 'w', encoding='utf-8')

resultSet = shutil.copyfileobj(srcFileObj, destFileObj)
print(resultSet)

srcFilePath = './shutilsDemo.py'
destFilePath = './shutilsDemoCopy2.py'

resultSet = shutil.copyfile(srcFilePath, destFilePath)  # copy srcFilePath to destFilePath
print(resultSet)


# copy method can copy directory

srcFilePath = './shutilsDemo.py'
descFileDirectoryPath = './temp/'
descFileDirectoryPathObj = pathlib.Path(descFileDirectoryPath)

if not descFileDirectoryPathObj.is_dir():  # if the directory not exists create it
    descFileDirectoryPathObj.mkdir(parents=True)

shutil.copy(srcFilePath, descFileDirectoryPath)  # make directory and copy srcFilePath to directory


# copytree method

srcRootDir = "D:/ASF"
destRootDir = "./asf"

destRootDirObj = pathlib.Path(destRootDir)

if destRootDirObj.is_dir():  # when is exists remove it
    shutil.rmtree(destRootDir)

shutil.copytree(srcRootDir, destRootDir)

time.sleep(5)

shutil.rmtree(destRootDir)  # remove it


