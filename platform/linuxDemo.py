__author__ = 'luowen'
'this is for linux platform demonstrates'

import platform


machine = platform.machine()
print(machine)  # print platform machine type

node = platform.node()
print(node)  # print compute's network name

platformInfo = platform.platform()
print(platformInfo)  # print much useful information

processorName = platform.processor()
print(processorName)  # print cpu information

release = platform.release()
print(release)  # print system release information

systemName = platform.system()
print(systemName)  # print system name

systemVersion = platform.version()
print(systemVersion)  # print version of system

systemNameAlais = platform.system_alias(systemName, release, systemVersion)
print(systemNameAlais)  # print linux alias information

uname = platform.uname()
print(uname)  # print linux uname information

