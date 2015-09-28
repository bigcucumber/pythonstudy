__author__ = 'luowen'
'some glob demos'

import glob
glob.glob('./[0-9].*')

glob.glob('*.gif')

glob.glob('?.gif')

glob.glob('**/*.txt', recursive=True)

glob.glob('./**/', recursive=True)

