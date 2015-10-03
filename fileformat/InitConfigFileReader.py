__author__ = 'luowen'
'this is ini configure file reader'
import configparser

config = configparser.ConfigParser({"haha": 'luwoen', 'xix': 'maomao', 'age': '23'})

config.read("config.ini")

sections = config.sections()

print(config.has_section("default"))  # judge the config has default sections
print(config.has_option("DEFAULT", 'haha'))  # judge the config object has haha attribute in DEFAULT section


age = config.get('DEFAULT', 'age')
print(type(age))  # get age of string dataType
age = config.getint('DEFAULT', 'age')
print(type(age))  # get age of integer dataType


# customer add config dynamic

config.add_section("extra")
config.set('extra', 'extension', 'php5lib')
config.set('extra', 'suffix', '.php')

with open('copyBYConfig.ini', 'w') as f:
    config.write(f)
