#!/usr/bin/env python
from telegram import Bot, ChatActions
from datetime import datetime
from time import gmtime, strftime
import os,sys,time
import time
myBot = Bot('telegrambot account_id')
chat_id = 'chat_id'
result = myBot.getMe()
now1 = time.ctime()
urls=[]
count = 0
for i in open(sys.argv[2]):
	count+=1
	urls.append('\n'+str(count)+'] '+i.rstrip().encode('utf-8'))
if "subdomain-takeover-scan.txt" in sys.argv[2]:
	result = myBot.sendMessage(chat_id,u"\u2705 "u"\U0001F4B0Subdomain-TKO Vulnerability Found\U0001F4B0"+'\n-----------------------------------------------------------------------\nDomain name     :'+sys.argv[1]+'\nVulnerable Domain :'+str(count)+'\n'+''.join(line for line in urls)+'\nTime :'+now1)
elif "open-redirect-scan" in sys.argv[2]:
	result = myBot.sendMessage(chat_id,u"\u2705 "u"\U0001F4B0Open-Redirect Vulnerability Found\U0001F4B0"+'\n-----------------------------------------------------------------------\n\nDomain name  :'+sys.argv[1]+'\nVulnerable urls :'+str(count)+'\n'+''.join(line for line in urls)+'\nTime : '+now1)

