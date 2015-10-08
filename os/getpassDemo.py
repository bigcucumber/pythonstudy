__author__ = 'luowen'
'Get Password Moduls'

import getpass

password = getpass.getpass(prompt="Please Input Your Password: ")
print("What you input password is [{0}]".format(password))


