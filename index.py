# -*- coding: utf-8 -*-
from __future__ import division
from flask import Flask,render_template,current_app,request,jsonify,url_for,send_from_directory,render_template_string,make_response
#import units
import abil
import correct
import db
import equip
import hashlib
import json
import materia
import matt
import os
import random
import sys
import traceback
import unitseries
from main import API
app = Flask(__name__)

dummy=['026CB300-C571-329B-6645-7F35B3F80A30','20E8D0D1-CB76-9435-D0C0-F925F88F2242','45EE1F9B-3226-5647-D002-8E89933A21DC','4C25B5AA-ABE3-7602-F734-50293D819555','801114ED-5B34-7F2C-76AC-75E45CF2AF9B','FB764A83-875C-7B94-493D-813BC0DE8897','23B3BFB5-AE63-E7A9-3D85-0E535D9AA898','29EFE12E-D38B-2BEC-95F7-BEC60315AD47','3D637B6A-F923-2FEC-C69B-652171BEE77F','4690EDF3-099E-570E-0521-91465B87840E','557D5DBE-E1ED-F822-840D-85EB3CD05592','7DDC1DCC-1D1F-AC95-3450-C62AA9C4663D','80C8972A-B240-1207-95EC-4B6CE91554ED','A43CAE31-E9D7-99E4-FB4F-4771C31F3CC4','B56E59BE-4CDB-3165-0188-F71FAE27BC3E','EACFC2FF-9221-F93D-92F7-4F3E0B0F488F','F409E08E-6033-4219-6371-0AB4783A91A8']

def parseMat(i,base):
	mats=i.split('@')
	for m in mats:
		m= m.split('-')[1]
		if m=='0':
			continue
		base=applyAbil(matt.data[str(m)],base)
	return base

def parseStats(i,base):
	for j in i:
		if 'em5hx4FX' in j:
			for k in i[j].split('-'):
				base['base']['hp']+=int(k)
		if 'L0MX7edB' in j:
			for k in i[j].split('-'):
				base['base']['mp']+=int(k)
		if 'o7Ynu1XP' in j:
			for k in i[j].split('-'):
				base['base']['atk']+=int(k)
		if '6tyb58Kc' in j:
			for k in i[j].split('-'):
				base['base']['def']+=int(k)
		if 'Y9H6TWnv' in j:
			for k in i[j].split('-'):
				base['base']['mag']+=int(k)
		if 'sa8Ewx3H' in j:
			for k in i[j].split('-'):
				base['base']['spr']+=int(k)
	return base

def parseEqu(i,uid,base):
	equips=i.split('@')
	for m in equips:
		m= m.split('-')[1]
		if m == '0':
			continue
		e=getEquipInfo(m)
		base['bonus']['hp']+=e['hp']
		base['bonus']['mp']+=e['mp']
		base['bonus']['atk']+=e['atk']
		base['bonus']['def']+=e['def']
		base['bonus']['mag']+=e['mag']
		base['bonus']['spr']+=e['spr']
		if e['ability']:
			base=applyAbil(e['ability'],base)
		weapon_mul=findEquipMul(uid,e['cat'])
		if weapon_mul:
			base['bonus']['hp']+=int(base['base']['hp']*weapon_mul['hp']/100)
			base['bonus']['mp']+=int(base['base']['mp']*weapon_mul['mp']/100)
			base['bonus']['atk']+=int(base['base']['atk']*weapon_mul['atk']/100)
			base['bonus']['def']+=int(base['base']['def']*weapon_mul['def']/100)
			base['bonus']['mag']+=int(base['base']['mag']*weapon_mul['mag']/100)
			base['bonus']['spr']+=int(base['base']['spr']*weapon_mul['spr']/100)
	return base
	
def applyAbil(aids,base):
	for aid in aids.split(','):
		try:
			data=abil.data[str(aid)].split('@')
		except:
			print 'failed applyAbil:%s %s'%(aids,base)
			continue
		for d in data:
			e=d.split(',')
			if len(e)==7:
				e=[int(x) for x in e]
				base['bonus']['hp']+=int(base['base']['hp']*(e[4])/100)
				base['bonus']['mp']+=int(base['base']['mp']*(e[5])/100)
				base['bonus']['atk']+=int(base['base']['atk']*(e[0])/100)
				base['bonus']['def']+=int(base['base']['def']*(e[1])/100)
				base['bonus']['mag']+=int(base['base']['mag']*(e[2])/100)
				base['bonus']['spr']+=int(base['base']['spr']*(e[3])/100)
			elif len(e)==5:
				e=[int(x) for x in e]
				base['bonus']['atk']+=int(base['base']['atk']*(e[1])/100)
			elif len(e)==6:
				e=[int(x) for x in e]
				if e[-1]==0:
					base['bonus']['hp']+=int(base['base']['hp']*(e[3])/100)
			else:
				print e,aid
	return base

def displayError(msg):
	return render_template('error.html',res=msg)

def displayStatus(msg):
	return render_template('status.html',res=msg)

@app.errorhandler(Exception)
def internal_error(error):
	print traceback.format_exc()
	return displayError('something went wrong, maybe admin should know this')

def parseEquipment(i):
	if i=='':
		return []
	wearing=[]
	equips=i.split('@')
	for e in equips:
		if len(e)==3:
			continue
		wearing.append(str(e.split('-')[1]))
	return wearing

def parseMats(i):
	if i=='':
		return []
	wearing=[]
	equips=i.split('@')
	for e in equips:
		if len(e)==3:
			continue
		wearing.append(str(e.split('-')[1]))
	return wearing

def getEquipInfo(i):
	return equip.equip[str(i)]
	
def findEquipMul(uid,equip_cat):
	try:
		return correct.multi[unitseries.series[str(uid)]][int(equip_cat)]
	except:
		return None

def parseBonus(b,uid):
	tmp= {'em5hx4FX':0,'L0MX7edB':0,'o7Ynu1XP':0,'6tyb58Kc':0,'Y9H6TWnv':0,'sa8Ewx3H':0,'hpm':0,'mpm':0,'atkm':0,'defm':0,'magm':0,'sprm':0} 
	for e in b:
		e=getEquipInfo(e)
		ecat=e['cat']
		weapon_mul=findEquipMul(uid,ecat)
		if weapon_mul:
			tmp['hpm']+=weapon_mul['hp']
			tmp['mpm']+=weapon_mul['mp']
			tmp['atkm']+=weapon_mul['atk']
			tmp['defm']+=weapon_mul['def']
			tmp['magm']+=weapon_mul['mag']
			tmp['sprm']+=weapon_mul['spr']
		tmp['em5hx4FX']+=e['hp']
		tmp['L0MX7edB']+=e['mp']
		tmp['o7Ynu1XP']+=e['atk']
		tmp['6tyb58Kc']+=e['def']
		tmp['Y9H6TWnv']+=e['mag']
		tmp['sa8Ewx3H']+=e['spr']
	return tmp
	
def getMulti(uid):
	return correct.multi[unitseries.series[str(uid)]]

def applyMulti(uid,base):
	_m=getMulti(uid)
	base['bonus']['hp']+=int(base['base']['hp']*_m['hp']/100)
	base['bonus']['mp']+=int(base['base']['mp']*_m['mp']/100)
	base['bonus']['atk']+=int(base['base']['atk']*_m['atk']/100)
	base['bonus']['def']+=int(base['base']['def']*_m['def']/100)
	base['bonus']['mag']+=int(base['base']['mag']*_m['mag']/100)
	base['bonus']['spr']+=int(base['base']['spr']*_m['spr']/100)
	return base

def getEquipName(e):
	try:
		return equip.equip[str(e)]['name']
	except:
		return 'no name'

def getMatName(e):
	try:
		return materia.mats[str(e)]['name']
	except:
		return 'no name'

def displayData(data):
	jdata=json.loads(data.replace('USER_TEAM_INFO_DEFAULT_MSG','Let\'s work together!'))
	equipment=parseEquipment(jdata['93Y6evuT'])
	mats=parseMats(jdata['80NUYFMJ'])
	esper=jdata['XZ4Kh7Ic'].split(',')
	_materia=jdata['80NUYFMJ']
	_equip=jdata['93Y6evuT']
	base={'base':{'hp':0,'mp':0,'atk':0,'def':0,'mag':0,'spr':0},'bonus':{'hp':0,'mp':0,'atk':0,'def':0,'mag':0,'spr':0}}
	base=parseStats(jdata,base)
	base=applyMulti(jdata['3HriTp6B'],base)
	if _equip:
		base=parseEqu(_equip,jdata['3HriTp6B'],base)
	if _materia:
		base=parseMat(_materia,base)
	return render_template('show.html',found=jdata,base=base,equipment=','.join([getEquipName(x) for x in equipment]),mats=','.join([getMatName(x) for x in mats]),esper='%s%s'%(esper[0],esper[1]) if len(esper)>=2 else None)
	
def getUserData(_id):
	a=API()
	a.setPlayerID(random.choice(dummy),1)
	a.InitializeRequest()
	a.GetUserInfoRequest()
	return a.FriendSearchRequest(_id)
	
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.png')
	
@app.route('/search',methods=['POST'])
def path_search():
	if request.method == 'POST':
		_id=request.form.get('id', None)
		if not _id:
			return displayError('data missing')
		_id=_id.replace('.','').replace(',','').replace(' ','')
		if not _id or len(str(_id))<>9:
			return displayError('data missing')
		_id=_id.zfill(9)
		isNew=False
		res=db.searchAccount(_id)
		if not res:
			res=getUserData(_id)
			isNew=True
		if res:
			if isNew:	db.addAccount(_id,res)
			return displayData(res)
		return displayStatus('no user found')
	else:
		return displayError('what is dis?')

@app.route('/id/<_id>',methods=['GET'])
def path_id(_id):
	if request.method == 'GET':
		if not _id:
			return displayError('data missing')
		_id=_id.replace('.','').replace(',','').replace(' ','')
		if not _id or len(str(_id))<>9:
			return displayError('data missing')
		_id=_id.zfill(9)
		isNew=False
		res=db.searchAccount(_id)
		if not res:
			res=getUserData(_id)
			isNew=True
		if res:
			if isNew:	db.addAccount(_id,res)
			return displayData(res)
		return displayStatus('no user found')
	else:
		return displayError('what is dis?')

@app.route('/update/<_id>',methods=['GET'])
def path_update(_id):
	if request.method == 'GET':
		if not _id:
			return displayError('data missing')
		_id=_id.replace('.','').replace(',','').replace(' ','')
		if not _id or len(str(_id))<>9:
			return displayError('data missing')
		_id=_id.zfill(9)
		res=getUserData(_id)
		if res:
			db.addAccount(_id,res)
			return displayData(res)
		return displayStatus('no user found')
	else:
		return displayError('what is dis?')

@app.route('/',methods=['GET'])
def path_index():
	return render_template('search.html')

@app.route('/todo',methods=['GET'])
def path_todo():
	return render_template('todo.html')

@app.route('/help',methods=['GET'])
def path_help():
	return render_template('log.html')

if __name__ == "__main__":
	app.jinja_env.auto_reload = True
	app.run(host='0.0.0.0',port=8002,debug=True,threaded=True)
