#!/usr/bin/env python
from telegram import Bot, ChatActions
from datetime import datetime
from time import gmtime, strftime
import os,sys
import time
myBot = Bot('telegram bot account_id')
chat_id = 'chat_id'
result = myBot.getMe()
now1 = time.ctime()
num = len(sys.argv)
if num <=3:
	result = myBot.sendMessage(chat_id,u"\U0001F44D "+sys.argv[1]+'\n\n     '+sys.argv[2]+'\n\n'+'Time :'+now1)
else:
	result = myBot.sendMessage(chat_id,'\n\xF0\x9F\x98\x89SCAN COMPLETED\xF0\x9F\x98\x89\n---------------------------------------\ndomain name : '+sys.argv[1]+'\ntotal subdomains : '+sys.argv[2]+'\ntotal live domains : '+sys.argv[3]+'\ntotal live urls : '+sys.argv[4]+'\n'+'\n'+'Time :'+now1)

