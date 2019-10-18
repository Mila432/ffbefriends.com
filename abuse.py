# -*- coding: utf-8 -*-
from main import API,Tools
from db import *
import io

_player='9DCB10ED-B4D9-47E4-9CC3-47235029CCE3'
_device=1

def save(data,file):
	with io.open(file, 'a', encoding='utf8') as thefile:
		thefile.write('%s\n'%unicode(data))
while(1):
	_dev=Tools().genRandomDeviceID()
	print _dev
	save(_dev,'ids.txt')
	a=API()
	a.setPlayerID(,_device)
	a.InitializeRequest()
	a.GetUserInfoRequest()
	res=json.loads(a.FriendSuggestRequest())['f6yGgCj2']
	for i in res:
		print 'adding:',i['m3Wghr1j']
		addAccount(i['m3Wghr1j'],json.dumps(i))