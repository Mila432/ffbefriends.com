# -*- coding: utf-8 -*-
import MySQLdb
import json
import base64

def searchAccount(id):
	db = MySQLdb.connect("localhost","root","password","ffbefriends")
	cursor = db.cursor()
	sql='select data from users where id = %s'%(id)
	cursor.execute(sql)
	data = cursor.fetchone()
	db.close()
	if data:
		return data[0]
	return None
	
def addAccount(id,data):
	db = MySQLdb.connect("localhost","root","password","ffbefriends")
	cursor = db.cursor()
	cursor.execute("set names utf8;")
	db.commit()
	cursor.execute('''INSERT INTO users (id,data) VALUES(%s,%s) ON DUPLICATE KEY UPDATE id=%s,data=%s''',(id,data,id,data))
	db.commit()
	db.close()