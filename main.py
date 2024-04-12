import time
import datetime
import os
import sys
# dfn: display file name in logger
def logger(text, logname, format, name):
	try:
			if format == 'txt':
				if os.path.exists(logname + '.txt')==True:
					f = open(logname + '.txt', 'a')
					f.write(name + time.strftime('>> %H:%M:%S - ') + str(text) + '\n')
					f.close()
				else:
					f = open(logname + '.txt', 'w')
					f.write(name + time.strftime('>> %H:%M:%S - ') + str(text) + '\n')
					f.close()
			elif format == 'log':
				if os.path.exists(logname + '.log')==True:
					f = open(logname + '.log', 'a')
					f.write(name + time.strftime('>> %H:%M:%S - ') + str(text) + '\n')
					f.close()
				else:
					f = open(logname + '.log', 'w')
					f.write(name + time.strftime('>> %H:%M:%S - ') + str(text) + '\n')
					f.close()
			else:
				print('Error1 in logger: file format has to be log or txt.')
				sys.exit(1)
	except Exception as e:
		print('Error0 in logger: Unknown Error>> ' + str(e))
		sys.exit(0)
				
					