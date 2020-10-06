#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
G = '\033[0;32m'
C = '\033[0;36m'
W = '\033[0;37m'
R = '\033[0;31m'
import requests,os,sys
from bs4 import BeautifulSoup as bs
reload(sys)
sys.setdefaultencoding('utf8')
try:
	os.system('clear')
	print '''%s╔═╗╔╦╗  ╔╗ ╦ ╦╔═╗╔═╗╔═╗╔═╗  ╦  ╦╔╦╗╦╔╦╗
║ ╦ ║║  ╠╩╗╚╦╝╠═╝╠═╣╚═╗╚═╗  ║  ║║║║║ ║ 
╚═╝═╩╝  ╚═╝ ╩ ╩  ╩ ╩╚═╝╚═╝  ╩═╝╩╩ ╩╩ ╩ 
'''%(C)
	sys.argv[1]
	print '%s[%s*%s] Waiting ...'%(W,G,W)
	try:
		api=requests.post('https://gdbypass.host/action.php',headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'},data={'link':sys.argv[1]}).text
		parse=bs(api,'html.parser').find('a')
		print '\n%s[%s✓%s] Url : %s'%(W,G,W,parse['href'])
		print '\n%s[%s✓%s] Title : %s'%(W,G,W,parse.text)
	except TypeError:exit('%s[%s!%s] URL is inccorect or destination file deleted'%(W,R,W))
except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W,R,W))
except IndexError:exit('%s[%s!%s] Use : python2 %s url_google_drive'%(W,R,W,sys.argv[0]))
except KeyboardInterrupt:exit('\n%s[%s!%s] Exit'%(W,R,W))