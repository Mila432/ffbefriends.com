# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import base64
import io
import json
import os
import re
import sys
import time
import conf
import socket

def getK(i):
	if i in conf.vars:
		return conf.vars[i]
	else:
		return None

def rp(ii):
	if 'Admin-PC' == socket.gethostname():
		content=ii
		keys=re.findall('"([a-zA-Z0-9]{8,8})"',content)
		found=[]
		for k in keys:
			if k not in found:
				found.append(k)
		for i in found:
			kf=getK(i)
			if i in content:
				if kf:
					content=content.replace(i,'%s:%s'%(i,kf))
		return content
	else:
		return ii

class Tools(object):
	def __init__(self):
		self.mode = AES.MODE_ECB
		self.encoder = PKCS7Encoder()
		self.names={'F_ABILITY_EXPLAIN_MST':{'id':'7FGj2bCh','key':'B2Ka3kft'},'F_ABILITY_MST':{'id':'TK61DudV','key':'4sPQ8aXo'},'F_AI_MST':{'id':'PCm9K3no','key':'yFr6Kj3P'},'F_ARCHIVE_MST':{'id':'Wmd5K32b','key':'t3T1hELp'},'F_AREA_MST':{'id':'Fvix6V0n','key':'pR2DHS6i'},'F_AWARD_MST':{'id':'xH4WGNk8','key':'HZgmc2u9'},'F_AWARD_TYPE_MST':{'id':'jsX49HtE','key':'t3IEWke8'},'F_BANNER_MST':{'id':'oB0YVw67','key':'C6ci5pfG'},'F_BATTLE_BG_MST':{'id':'bqR4p8SN','key':'39mEiDNB'},'F_BATTLE_SCRIPT_MST':{'id':'i7STtbw8','key':'o28ckLUb'},'F_BEAST_BOARD_PIECE_EXT_MST':{'id':'5o0Z6Gwn','key':'Knh15FzM'},'F_BEAST_BOARD_PIECE_MST':{'id':'E9z2e4UZ','key':'XvkVU34H'},'F_BEAST_CP_MST':{'id':'dzA5MC6f','key':'Syax34vR'},'F_BEAST_EXPLAIN_MST':{'id':'J3BkY7wT','key':'jw0X2ZNm'},'F_BEAST_EXP_PATTERN_MST':{'id':'42JaImDh','key':'UY7D3dpn'},'F_BEAST_GROW_MST':{'id':'tSb4Y8QR','key':'7YUDsew3'},'F_BEAST_MST':{'id':'WF57bvfG','key':'hdFeT14k'},'F_BEAST_SKILL_MST':{'id':'zE1hx53P','key':'Y4Fds1Jr'},'F_BEAST_STATUS_MST':{'id':'tWp7f5Ma','key':'XuWn97Hf'},'F_CAPTURE_MST':{'id':'65fHqgnT','key':'w1A9S5sr'},'F_CHALLENGE_MST':{'id':'GL9t6cMF','key':'8Dx2QUZS'},'F_CHARACTER_MST':{'id':'cf29diuR','key':'ru39Q4YK'},'F_CLSM_GRADE_MST':{'id':'q14CSpIb','key':'sn8QPJ24'},'F_CLSM_PROGRESS_MST':{'id':'pF3JiA6L','key':'h8Za6TiL'},'F_CLSM_RANK_MST':{'id':'W2f5GThw','key':'jtbur0h5'},'F_CLSM_ROUND_MST':{'id':'7zEc85n1','key':'V4wZA7Hn'},'F_CRAFT_EXT_MST':{'id':'1GPYxQR3','key':'eHn8EU5o'},'F_DEFINE_MST':{'id':'zg5P1AxM','key':'Zib6m5ed'},'F_DESCRIPTION_FORMAT_MST':{'id':'HL3rXQh7','key':'WvJI5AB8'},'F_DIAMOND_MST':{'id':'mo47BaST','key':'p9sk1MjH'},'F_DUNGEON_MST':{'id':'1Bj4oy5Q','key':'9bEA2SYP'},'F_EFFECT_GROUP_MST':{'id':'ZM06fUem','key':'4WipzuH2'},'F_EFFECT_MST':{'id':'HfRPdg65','key':'d4KR8YSq'},'F_EMBLEM_ITEM_MST':{'id':'SuM2XA05','key':'UyE6HP3h'},'F_ENCOUNT_FIELD_MST':{'id':'2Jtkc4Ar','key':'mhok0p7B'},'F_EQUIP_ITEM_EXPLAIN_MST':{'id':'psuJ5VE2','key':'r6PSK8QW'},'F_EQUIP_ITEM_MST':{'id':'S67QEJsz','key':'T1kP80NU'},'F_EXCHANGE_SHOP_ITEM_MST':{'id':'5hYf3xv1','key':'sg3fXED8'},'F_EXPEDITION_DIFFICULTY_MST':{'id':'4Xy9386a','key':'0vkM7772'},'F_EXPEDITION_MST':{'id':'TdE7Oasq','key':'fFx92pYD'},'F_EXPLORE_AREA_MST':{'id':'b2VdS9Pv','key':'6wm49Yur'},'F_EXPLORE_TIME_MST':{'id':'1jVfJ6CB','key':'0WaTe2ZH'},'F_EXVIUS_POINT_REWARD_MST':{'id':'jiSF1p9I','key':'h8x1tiwz'},'F_FOOTPRINT_MST':{'id':'q3jTCo8m','key':'iI7aS2oq'},'F_FUNCTION_MST':{'id':'6wibj9m8','key':'sy6GRuY2'},'F_GACHA_EFFECT_BLOCK_MST':{'id':'fDI1T97q','key':'7H3P6zF4'},'F_GACHA_EFFECT_PATTERN_MST':{'id':'uw07SXpU','key':'48HhnaKP'},'F_GACHA_SELECT_UNIT_MST':{'id':'qRb73JSY','key':'H9Jye1j3'},'F_GAME_TITLE_MST':{'id':'91D3CfxA','key':'yFZs58K7'},'F_GIFT_MST':{'id':'AK5v1YEd','key':'1cJ4IuP9'},'F_ICON_MST':{'id':'LM1APs6u','key':'8XT23CYy'},'F_IMAGE_SWITCHING_MST':{'id':'K4rvk96u','key':'Ne92GPyR'},'F_IMPORTANT_ITEM_EXPLAIN_MST':{'id':'Nny6xD90','key':'89fcSX4v'},'F_IMPORTANT_ITEM_MST':{'id':'vdeSoq61','key':'tnNGLk45'},'F_ITEM_EXPLAIN_MST':{'id':'E7YMdK3P','key':'TERM4PD7'},'F_ITEM_EXT_BEAST_MST':{'id':'hc8Ham29','key':'wZ5IkW2f'},'F_ITEM_MST':{'id':'1CUX0Qwr','key':'L3f8nko1'},'F_JOB_MST':{'id':'F2mQ87Wt','key':'3CVoZu7s'},'F_LAND_MST':{'id':'23yVcGpH','key':'Y9wKxzI0'},'F_LEARNING_MST':{'id':'DLVF0cN1','key':'4HCdYk80'},'F_LIMITBURST_LV_MST':{'id':'0EvyjKh8','key':'g2hZpVW7'},'F_LIMITBURST_MST':{'id':'c5T4PIyL','key':'6q3eIR9k'},'F_LOGIN_BONUS_MST':{'id':'P3raZX89','key':'8xQP3fUZ'},'F_LOGIN_BONUS_SP_MST':{'id':'gjkPJ95T','key':'o64t9Qmd'},'F_LOGIN_BONUS_SP_REWARD_MST':{'id':'JQ1c6DCd','key':'Ym2rpIA7'},'F_LOGIN_BONUS_TOTAL_REWARD_MST':{'id':'J6dVmNv5','key':'y57ZhtLI'},'F_MAGIC_EXPLAIN_MST':{'id':'8qbVQUx5','key':'8LE2hk3r'},'F_MAGIC_MST':{'id':'6J8jwSDW','key':'2zyP4WQY'},'F_MAP_EVENT_MST':{'id':'91vNbdxg','key':'1YAk2fcr'},'F_MAP_EXT_RESOURCE_MST':{'id':'En90A5BC','key':'9dA6bguS'},'F_MAP_OBJECT_MST':{'id':'7d25gta1','key':'1zYSh5ps'},'F_MAP_ROUTE_MST':{'id':'F1a5PZYq','key':'rASW8N5L'},'F_MATERIA_EXPLAIN_MST':{'id':'bW2GHT1N','key':'7mof2RVP'},'F_MATERIA_LIMIT_MST':{'id':'BX0pRc8A','key':'CVERk9KN'},'F_MATERIA_MST':{'id':'Af46DrVW','key':'4MbdRZI6'},'F_MISSION_MST':{'id':'24Eka6wL','key':'naJ3P84b'},'F_MONSTER_DICTIONARY_EXPLAIN_MST':{'id':'Svq1K0rh','key':'wA4Dxp1m'},'F_MONSTER_DICTIONARY_MST':{'id':'1r6jb9wB','key':'wL4N16V3'},'F_NPC_MST':{'id':'94diC1bt','key':'fvQ37cE0'},'F_PICTURE_STORY_MST':{'id':'PSDIR8b1','key':'SDV4mZL0'},'F_PLAYBACK_CHAPTER_MST':{'id':'Nm36woZx','key':'gHLE4DM0'},'F_PLAYBACK_EVENT_MST':{'id':'IL78hX09','key':'qWr8ZE2D'},'F_PLAYBACK_MAP_MST':{'id':'9Zdr5ap0','key':'ZdM9VQb0'},'F_PLAYBACK_SEASON_MST':{'id':'D2zaT7Ru','key':'UgLId19h'},'F_PRODUCT_MST':{'id':'DEC8Jmy2','key':'OEl4ZmDY'},'F_PURCHASE_AGE_LIMIT_MST':{'id':'okUH6yV7','key':'ZDvrb16x'},'F_QUEST_MST':{'id':'2Px75LpY','key':'20mEeKo3'},'F_QUEST_SUB_MST':{'id':'myGc0U5v','key':'oWcL37sK'},'F_RB_ABILITY_GROUP_MST':{'id':'UHk7x2V8','key':'Q83j0GvZ'},'F_RB_AI_PATTERN_MST':{'id':'A6DJx0Qj','key':'2phgAJt3'},'F_RB_BONUS_RULE_MST':{'id':'09u3Nzk2','key':'7Hm6jxe3'},'F_RB_DEFINE_MST':{'id':'qzTG4ba0','key':'2y1oT5gq'},'F_RB_FORBIDDEN_INFO_MST':{'id':'x6iQrD2e','key':'8yWH5IGC'},'F_RB_LS_MST':{'id':'8tR1K79p','key':'2nJN19qh'},'F_RB_LS_REWARD_MST':{'id':'0Nc4PkAJ','key':'m7XJdkp1'},'F_RB_SS_MST':{'id':'gd74jWQn','key':'gY7NiJL8'},'F_RB_SS_REWARD_MST':{'id':'cg5k2Mxn','key':'KNWf37Bm'},'F_RB_TRADE_BOARD_MST':{'id':'yiuv0Fb9','key':'cbqYR3s7'},'F_RB_TRADE_BOARD_PIECE_MST':{'id':'7Si5wPLj','key':'fXZse89L'},'F_RECIPE_BOOK_MST':{'id':'yu5rvEI3','key':'3t8DMRQE'},'F_RECIPE_MST':{'id':'27pGMZDm','key':'JveAwh98'},'F_RESOURCE_MAP_VERSION_MST_LOCALIZE':{'id':'YIgCpDKW','key':'geHlpoos'},'F_RESOURCE_VERSION_MST_LOCALIZE':{'id':'A1L1GlaQ','key':'JchlFPWK'},'F_RULE_MST':{'id':'7s4egUBN','key':'sf2o1jWL'},'F_SACRIFICE_MST':{'id':'w5JFGPh3','key':'J2u0YBPr'},'F_SEASON_EVENT_ABILITY_MST':{'id':'VMIe9c6U','key':'Na71Z6kg'},'F_SEASON_EVENT_ABILITY_TYPE_MST':{'id':'I0SUr3WY','key':'XY2MA1x3'},'F_SEASON_EVENT_GROUP_FRIEND_LV_MST':{'id':'v5aCt9ne','key':'g7VmK5a9'},'F_SG_TIME_DUNGEON_MST':{'id':'pnjSbo89','key':'UhUsWVhw'},'F_SHOP_MST':{'id':'1ks9q4Pj','key':'X0FA6Ewh'},'F_SOUND_MST':{'id':'9bnqECY6','key':'m2zHEtV0'},'F_SP_CHALLENGE_MST':{'id':'4b6NcpLo','key':'wd1t3MPf'},'F_STORY_EVENT_MST':{'id':'YW9MUm2H','key':'LyjM2nU9'},'F_STORY_MST':{'id':'IiVw7H6k','key':'Cf2WZ8qA'},'F_STORY_SUB_MST':{'id':'8vneWT7G','key':'8ci0TamY'},'F_STRONGBOX_MST':{'id':'X1xsdRk7','key':'qPpXT0Z2'},'F_SUBLIMATION_RECIPE_MST':{'id':'M9K0SJgR','key':'vnkfer76'},'F_SWITCH_MST':{'id':'T46RpNZH','key':'AUx51pni'},'F_SWITCH_TYPE_MST':{'id':'PJw28YRg','key':'5NUkhS4Q'},'F_TEAM_LV_MST':{'id':'NCPTw2p0','key':'qP7TGZE8'},'F_TEXT_ABILITY_EXPLAIN_LONG':{'id':'uxMPAs4y','key':'lECkWwBw'},'F_TEXT_ABILITY_EXPLAIN_SHORT':{'id':'8GJBzdQV','key':'D9UVupRQ'},'F_TEXT_ABILITY_NAME':{'id':'eSB5Ry3E','key':'At4ghcWo'},'F_TEXT_ABILITY_PARAM_MSG':{'id':'3oM745kA','key':'OTxnCDr7'},'F_TEXT_ARCHIVE_NAME':{'id':'QR3zeiJr','key':'CrZmyr8k'},'F_TEXT_AREA_NAME':{'id':'4qiOcmtJ','key':'FhWJxFlW'},'F_TEXT_AWARD_EXPLAIN':{'id':'TlrlvFx5','key':'XfXmnCNF'},'F_TEXT_AWARD_NAME':{'id':'mGPBqPdv','key':'G9IOqfaz'},'F_TEXT_AWARD_TYPE':{'id':'soohaWOo','key':'b23aWS6d'},'F_TEXT_BEAST_NAME':{'id':'148O76GI','key':'pzLuYoDO'},'F_TEXT_BEAST_SKILL_DES':{'id':'Yjq14lAB','key':'g5SJviEC'},'F_TEXT_BEAST_SKILL_NAME':{'id':'k51drhZ6','key':'JHJRAcEx'},'F_TEXT_BUNDLE':{'id':'4OBhnBKu','key':'3VkESseA'},'F_TEXT_CAPTURE_INFO':{'id':'Ir2B1EBL','key':'Ak7An4Ys'},'F_TEXT_CHALLENGE_NAME':{'id':'4bQbA2FH','key':'SFaS7rXZ'},'F_TEXT_CHARACTER_NAME':{'id':'JIqrNzje','key':'iizk8FjI'},'F_TEXT_COLOSSEUM_GRADE':{'id':'Y2rngIF3','key':'7Vzk5Oq9'},'F_TEXT_COLOSSEUM_MONSTER_GROUP_NAME':{'id':'q4z5D08C','key':'04zFXazI'},'F_TEXT_DAILY_QUEST_DES':{'id':'W4525rcx','key':'1ihwWs7f'},'F_TEXT_DAILY_QUEST_DETAIL':{'id':'gCfFcx75','key':'xpLyjA9A'},'F_TEXT_DAILY_QUEST_NAME':{'id':'FBBD8vv6','key':'BhDl8FWG'},'F_TEXT_DIAMOND_NAME':{'id':'mcQeT7mq','key':'tN7Gjdpv'},'F_TEXT_DUNGEON_NAME':{'id':'AyVqkz2B','key':'0cqVvd61'},'F_TEXT_EXCHANGE_SHOP_ITEM':{'id':'r1ZLxyyg','key':'fT1SbKUm'},'F_TEXT_EXPN_STORY':{'id':'N1FxjkHa','key':'AC7L89p8'},'F_TEXT_GACHA':{'id':'ZJz5QwAy','key':'Ab2Kb6yJ'},'F_TEXT_GAME_TITLE_NAME':{'id':'3CzC5zn7','key':'SA6Bv7i1'},'F_TEXT_IMPORTANT_ITEM_EXPLAIN_LONG':{'id':'aJ4tvgSq','key':'iElLxksB'},'F_TEXT_IMPORTANT_ITEM_EXPLAIN_SHORT':{'id':'YBqAUJt1','key':'Fc6H1Udw'},'F_TEXT_IMPORTANT_ITEM_NAME':{'id':'TIKwbf3D','key':'lx4HCdrQ'},'F_TEXT_IMPORTANT_ITEM_SHOP':{'id':'JO7UqqJ6','key':'EzACmD0Y'},'F_TEXT_ITEM_EQUIP_LONG':{'id':'CD4giPVu','key':'jqe9yQm0'},'F_TEXT_ITEM_EQUIP_NAME':{'id':'E0NdslwL','key':'SGMI0nIq'},'F_TEXT_ITEM_EQUIP_SHORT':{'id':'Nao9HYWk','key':'I0l1uc2s'},'F_TEXT_ITEM_EXPLAIN_LONG':{'id':'9NCIDltW','key':'s3fVSywt'},'F_TEXT_ITEM_EXPLAIN_SHORT':{'id':'IAPS1jOu','key':'TZh30bbo'},'F_TEXT_ITEM_NAME':{'id':'VhkhtvDn','key':'xDkegMbe'},'F_TEXT_JOB_NAME':{'id':'yUkwbFyc','key':'R6mBb3T3'},'F_TEXT_LAND_NAME':{'id':'sKLZVYWQ','key':'yYnTSUtm'},'F_TEXT_LIMIT_BURST_DES':{'id':'EUsG7rlQ','key':'ZcXYp8BI'},'F_TEXT_LIMIT_BURST_NAME':{'id':'XBS8hLZD','key':'zswbSb5U'},'F_TEXT_MAGIC_EXPLAIN_LONG':{'id':'Jcavjyxo','key':'ZFHehCN4'},'F_TEXT_MAGIC_EXPLAIN_SHORT':{'id':'Hs9KVVnj','key':'raokY9Xl'},'F_TEXT_MAGIC_NAME':{'id':'1ZqISaBp','key':'9TAwFj0e'},'F_TEXT_MAP_OBJECT':{'id':'15KaBQci','key':'U56G5oiU'},'F_TEXT_MATERIA_EXPLAIN_LONG':{'id':'QEbXmDTD','key':'3ZaDmbq1'},'F_TEXT_MATERIA_EXPLAIN_SHORT':{'id':'8g18k8jD','key':'DvdwoXYQ'},'F_TEXT_MATERIA_NAME':{'id':'2Eg5s20D','key':'E5jbLGyb'},'F_TEXT_MISSION':{'id':'pa6vblsG','key':'GdAhtrNB'},'F_TEXT_MONSTER_DICTIONARY_NAME':{'id':'F1VQsGpG','key':'uEOGF11w'},'F_TEXT_MONSTER_DIC_EXPLAIN_LONG':{'id':'xe6RH45K','key':'p9l4ys4L'},'F_TEXT_MONSTER_DIC_EXPLAIN_SHORT':{'id':'zf7USTwU','key':'OJir9FR5'},'F_TEXT_MONSTER_NAME':{'id':'0xkPiwVI','key':'UOz3hI2k'},'F_TEXT_MONSTER_PART_DIC_NAME':{'id':'P4c5fq2t','key':'XhCacZZv'},'F_TEXT_MONSTER_SKILL_NAME':{'id':'F1z92dkt','key':'B41kLp2C'},'F_TEXT_MONSTER_SKILL_SET_NAME':{'id':'76oKZdNU','key':'mOz786Zr'},'F_TEXT_NPC_NAME':{'id':'A55coosK','key':'xQj2cuc8'},'F_TEXT_PICTURE_STORY_NAME':{'id':'j525zYCH','key':'Pe21ACFe'},'F_TEXT_PLAYBACK':{'id':'cvz0lj48','key':'svmqgt6n'},'F_TEXT_QUEST':{'id':'NMwfx1lf','key':'KVBowHC2'},'F_TEXT_QUEST_SUB_DETAIL':{'id':'vb5Nom5d','key':'sCFyRxng'},'F_TEXT_QUEST_SUB_NAME':{'id':'uuU68I2u','key':'cnW2w71S'},'F_TEXT_QUEST_SUB_STORY':{'id':'fULaqIeB','key':'CueuZNTN'},'F_TEXT_QUEST_SUB_TARGET_PARAM':{'id':'Cw3B65ql','key':'W4rz5Sas'},'F_TEXT_RB_ABILITY_GROUP_DESCRIPTION':{'id':'3sxyv1w9','key':'v30p83B2'},'F_TEXT_RB_ABILITY_GROUP_NAME':{'id':'69zUY4Zb','key':'qEAmEfJU'},'F_TEXT_RB_BONUS_RULE_DESCRIPTION':{'id':'10Ew2Rth','key':'AGItS6CC'},'F_TEXT_RB_BONUS_RULE_NAME':{'id':'6YYynT87','key':'YC0psthA'},'F_TEXT_RB_FORBIDDEN_INFO_DESCRIPTION':{'id':'M6bRb5Eg','key':'ScqX2kIE'},'F_TEXT_RB_FORBIDDEN_INFO_NAME':{'id':'DaNvFWp7','key':'wxea5c0t'},'F_TEXT_RECIPE_BOOK_NAME':{'id':'tFnHkR8G','key':'lEWsm9iI'},'F_TEXT_RECIPE_EXPLAIN_LONG':{'id':'DS21iNC5','key':'9uTG75o7'},'F_TEXT_RULE_DESCRIPTION':{'id':'a6kiwI22','key':'EahlebAb'},'F_TEXT_SCENARIO_BATTLE':{'id':'TGxop4tW','key':'ZCIcuxf3'},'F_TEXT_SEASON_EVENT_ABILITY_NAME':{'id':'q81b55dv','key':'E6Jrump4'},'F_TEXT_SEASON_EVENT_ABILITY_TYPE_DESCRI':{'id':'q81b55dv','key':'E6Jrump4'},'F_TEXT_SEASON_EVENT_ABILITY_TYPE_DESCRIPTION':{'id':'q81b55dv','key':'E6Jrump4'},'F_TEXT_SEASON_EVENT_ABILITY_TYPE_NAME':{'id':'xT67VZAS','key':'jFgn6bIU'},'F_TEXT_SEASON_EVENT_DESCRIPTION':{'id':'mKbhB8ai','key':'Kt30PvJg'},'F_TEXT_SEASON_EVENT_NAME':{'id':'FxaCYmHE','key':'NwKi0CpP'},'F_TEXT_SHOP':{'id':'NYz5Oxm4','key':'yBd5wOHp'},'F_TEXT_SPCHALLENGE':{'id':'hge62ssc','key':'lklesd2w'},'F_TEXT_STORY_NAME':{'id':'fKGHnuPm','key':'nJswCIXz'},'F_TEXT_STORY_SUB':{'id':'hiiVWxXJ','key':'ucOQs1YO'},'F_TEXT_SUBLIMATION_EXPLAIN':{'id':'JF89DHPE','key':'SkUNQP6F'},'F_TEXT_TELEPO_NAME':{'id':'ca5XNnWD','key':'WfvQbAKG'},'F_TEXT_TEXT_EN':{'id':'0ThfQQWd','key':'s9E34w78'},'F_TEXT_TICKER':{'id':'RUPcXt7J','key':'tHaAyyqI'},'F_TEXT_TOWN_EXPLAIN':{'id':'KLoYS0Tj','key':'0BZOtiRB'},'F_TEXT_TOWN_NAME':{'id':'N12vEZpN','key':'11yq2cUt'},'F_TEXT_TOWN_STORE':{'id':'h23JuUGF','key':'Jovaw62m'},'F_TEXT_TOWN_STORE_COMMENT':{'id':'SZXTrTgq','key':'oVpBUtX2'},'F_TEXT_TOWN_STORE_OWNER_NAME':{'id':'KFL34pbm','key':'Q9HMWNZG'},'F_TEXT_TRIBE':{'id':'Z6OfsPv9','key':'FAfGhIMo'},'F_TEXT_TROPHY_EXPLAIN':{'id':'pNeHXqpJ','key':'OJV9Jpm8'},'F_TEXT_TROPHY_METER_SERIF':{'id':'7BfBBf9E','key':'S410iF8y'},'F_TEXT_UNITS_NAME':{'id':'sZE3Lhgj','key':'3IfWAnJ3'},'F_TEXT_UNIT_AFFINITY':{'id':'Zfw0jmyn','key':'xCppLKwD'},'F_TEXT_UNIT_DESCRIPTION':{'id':'w6U2ntyZ','key':'VNh3r92R'},'F_TEXT_UNIT_EVO':{'id':'7tfppWVS','key':'OYQn68Hu'},'F_TEXT_UNIT_EXPLAIN_SHOP':{'id':'3uEWl5CV','key':'QrOn67A8'},'F_TEXT_UNIT_FUSION':{'id':'TpbDECdR','key':'v47OlIK4'},'F_TEXT_UNIT_SUMMON':{'id':'hWE8dJMC','key':'GInxSlTN'},'F_TEXT_WORLD_NAME':{'id':'GPNXLUJP','key':'uDFuhlR6'},'F_TICKER_DEFINE_MESSAGE_MST':{'id':'tUQ2Lkc1','key':'6TQR0hSX'},'F_TICKER_LOG_CATEGORY_MST':{'id':'QmnZ48Fs','key':'hJ91Gkz5'},'F_TICKER_MST':{'id':'5WJ9MQ3n','key':'h92Fk0Qw'},'F_TICKET_MST':{'id':'95KFiNTM','key':'0sDdWku8'},'F_TOWN_MST':{'id':'6P9XZ7ts','key':'IavY38oB'},'F_TOWN_STORE_COMMENT_MST':{'id':'ASh8IH0b','key':'1L7oneM4'},'F_TOWN_STORE_MST':{'id':'v34C8PdG','key':'Si9bxe86'},'F_TRIBE_MST':{'id':'3Lc1DWQV','key':'adj41LQC'},'F_TROPHY_METER_SERIF_MST':{'id':'4Qz7qK51','key':'SGjk89Tr'},'F_TROPHY_MST':{'id':'9ZN4Eo1m','key':'5qRZs6Kz'},'F_TROPHY_REWARD_MST':{'id':'GN1bMQm3','key':'KyAC0q3D'},'F_UNIT_CLASS_UP_MST':{'id':'60FtuAhp','key':'pjW5TI0K'},'F_UNIT_EXPLAIN_MST':{'id':'Da62x85q','key':'zU6L4Gng'},'F_UNIT_EXP_PATTERN_MST':{'id':'kMnY10ry','key':'B38YWDtF'},'F_UNIT_GROW_MST':{'id':'i3YrEM1t','key':'6cUguh10'},'F_UNIT_MST':{'id':'SsidX62G','key':'UW0D8ouL'},'F_UNIT_SERIES_LV_ACQUIRE_MST':{'id':'Eb5ewi87','key':'t8QV2WvE'},'F_URL_MST':{'id':'9wmd4iua','key':'UREmi85S'},'F_WORLD_MST':{'id':'JLxQW68j','key':'t8bWUq9Z'},'F_TOWN_EXPLAIN_MST':{'id':'QJF37LcR','key':'1ThX6WNZ'},'F_TROPHY_EXPLAIN_MST':{'id':'yhnT19Z4','key':'JPTK6q4V'},'F_MONSTER_SKILL_SET_MST':{'id':'B9K8ULHc','key':'p6iXmLh4'},'F_AWARD_EXPLAIN_MST':{'id':'B2mKN0M4','key':'0FfIgG67'},'F_MEDAL_EXCHANGE_MST':{'id':'2qDEnLF9','key':'7FmTj0hp'},'F_STORE_ITEM_MST':{'id':'03cY9vXe','key':'d60DCUMp'},'F_TELEPO_MST':{'id':'zw0kb3To','key':'KENf4db1'},'F_RESOURCE_MAP_MST':{'id':'B7LnP2TH','key':'U0Vd7AfQ'},'F_RESOURCE_MST':{'id':'ZQqB38Ns','key':'u6q3F02d'},'F_TEXT_ANALYTICS_LOCALIZE':{'id':'3sI39BAT','key':'6zAQarn1'},'F_TEXT_ANALYTICS_ITEMS':{'id':'8e6PGb3p','key':'7nyO4pC9'},'F_TEXT_BATTLE_SCRIPT':{'id':'dhR7sSxt','key':'QuxKHQQT'}}
		
	def fillKeyNoBase(self,key):
		return key+((16-len(key))*'\00')

	def fillKeyWithBase(self,key):
		return base64.b64encode(key+((16-len(key))*'\00'))

	def findFileName(self,id):
		try:
			return self.names[id]['id']
		except:
			return None

	def findFileKey(self,id):
		try:
			return self.names[id]['key']
		except:
			print 'key not found %s'%id
			return None

	def cleanName(self,n):
		return re.sub('.dat.*','',n)

	def encrypt(self,s,key):
		if len(key)<16:
			key=self.fillKeyNoBase(key)
		e = AES.new(key, self.mode)
		padded_text = self.encoder.encode(s.encode('utf-8'))
		return base64.b64encode(e.encrypt(padded_text))

	def decrypt(self,s,key):
		if len(key)<16:
			key=self.fillKeyNoBase(key)
		e = AES.new(key, self.mode)
		return self.encoder.decode(e.decrypt(base64.b64decode(s)))

class Updater(object):
	def __init__(self,region=1):
		self.region=region
		if self.region==1:
			self.base_txt='http://lapis-dlc.gumi.sg/dlc_assets_prod/localized_texts/%s'
			self.base_mst='http://lapis-dlc.gumi.sg/dlc_assets_prod/mst/%s'
		else:
			self.base_txt='http://cdn.resource.exvius.com/dlc_assets_prod/localized_texts/%s'
			self.base_mst='http://cdn.resource.exvius.com/lapis/resource/mst/%s'
		self.tools=Tools()

	def log(self,msg):
		print('[%s]:%s'%(time.strftime('%H:%M:%S'),msg))

	def setTT(self,data):
		self.updateData=data
		self.findMST()
		self.doUpdate()
		self.unpackAll()
		try:
			self.updateAll()
		except:
			pass

	def updateAll(self):
		self.parseMissionTypes()
		self.parseItemNames()
		self.parseMissionNames()
		self.parseLevels()
		self.parseUnit()
		self.parseChallenges()

	def doUpdate(self):
		if hasattr(self,'updateData'):
			self.makeFolder(self.mst)
			for ufile in  self.updateData:
				ufilename=self.tools.findFileName(ufile['a4hXTIm0'])
				if ufilename:
					self.downloadFile(ufile['a4hXTIm0'],ufile['wM9AfX6I'],ufilename)
				else:
					self.log('missing:%s %s'%(ufile['a4hXTIm0'],ufile['wM9AfX6I']))

	def makeFolder(self,name):
		if not os.path.exists(name):
			os.makedirs(name)

	def isFolder(self,file):
		return os.path.exists(file)
			
	def ensure_unicode(self,v):
		if isinstance(v, str):
			v = v.decode('utf8')
		return unicode(v)

	def save(self,data,file):
		with io.open(file, 'w', encoding='utf8') as the_file:
			if '_MST' in file:
				the_file.write('%s'%(unicode(json.dumps(json.loads(data), indent=4, sort_keys=True,ensure_ascii=False))))
			else:
				the_file.write('%s'%(unicode(self.ensure_unicode(data))))

	def downloadFile(self,file,version,filename):
		download_name='Ver%s_%s.dat'%(version,filename)
		local_name='%s.dat'%(file)
		if not os.path.isfile('%s/%s'%(self.mst,local_name)):
			os.system('wget -q --header="User-Agent: FF%%20EXVIUS/2.1.1 CFNetwork/808.2.16 Darwin/16.3.0" -O %s/%s %s'%(self.mst,local_name,self.base_mst%(download_name) if '_MST' in file else self.base_txt%(download_name)))

	def getFileContent(self,file,MST=False):
		clean_filename= self.tools.cleanName(file)
		file_key=self.tools.findFileKey(clean_filename)
		with open('%s/%s'%(self.mst,file)) as data_file:    
			data = data_file.readlines()
			rr=[]
			if MST:
				rr.append('[')
			for l in data:
				if MST:
					rr.append(self.tools.decrypt(l,file_key)+',' if l <> data[-1] else self.tools.decrypt(l,file_key))
				else:
					rr.append(self.tools.decrypt(l,file_key))
			if MST:
				rr.append(']')
			self.save(rp(''.join(rr)),'%s/%s.json'%(self.mst,clean_filename))

	def parseMissionTypes(self):
		target='%s/F_MISSION_MST.json'%(self.mst)
		if self.isFolder(target):
			_t={}
			with open(target) as data_file:    
				data = json.load(data_file)
				for m in data:
					B6kyCQ9M=int(m['B6kyCQ9M'])#energy use
					qo3PECw6=int(m['qo3PECw6'])#mission id
					Y4VoF8yu=int(m['Y4VoF8yu'])
					v8xi6Xvyk=int(m['8xi6Xvyk'])
					_t[qo3PECw6]={}
					_t[qo3PECw6]['type']=Y4VoF8yu
					_t[qo3PECw6]['energy']=B6kyCQ9M
					_t[qo3PECw6]['rounds']=v8xi6Xvyk
				self.save('# -*- coding: utf-8 -*-\nmission_types=%s'%unicode(json.dumps(_t, ensure_ascii=False)),'mission_types_%s.py'%('gl' if self.region == 1 else 'jp'))
				
	def parseItemNames(self):
		fin={}
		if self.region==1:
			target='%s/F_TEXT_ITEM_NAME.json'%(self.mst)
			if self.isFolder(target):
				with open(target) as data_file:    
					data = data_file.readlines()
					for l in data:
						l=l.rstrip().split('^')
						if len(l[0]) >=1:
							try:
								cn= self.cleanMissionName(l[0])
								fin[cn]={}
								fin[cn]['name']=l[1]
							except:
								pass
					self.save('# -*- coding: utf-8 -*-\nitems=%s'%fin,'item_names_%s.py'%('gl' if self.region == 1 else 'jp'))
		else:
			target='%s/F_ITEM_MST.json'%(self.mst)
			if self.isFolder(target):
				with open(target) as data_file:
					data = json.load(data_file)
					for m in data:
						G4L0YIB2=m['G4L0YIB2']#name
						tL6G9egd=str(m['tL6G9egd'])#id
						fin[tL6G9egd]={}
						fin[tL6G9egd]['name']=G4L0YIB2
					self.save('# -*- coding: utf-8 -*-\nitems=%s'%fin,'item_names_%s.py'%('gl' if self.region == 1 else 'jp'))

	def parseMissionNames(self):
		fin={}
		if self.region==1:
			target='%s/F_TEXT_MISSION.json'%(self.mst)
			if self.isFolder(target):
				with open(target) as data_file:
					data = data_file.readlines()
					for l in data:
						l=l.rstrip().split('^')
						if len(l[0]) >=1:
							try:
								cn= self.cleanMissionName(l[0])
								fin[cn]={}
								fin[cn]['name']=l[1].decode('utf-8')
							except:
								pass
					self.save('# -*- coding: utf-8 -*-\nmissions=%s'%self.ensure_unicode(unicode(json.dumps(fin, ensure_ascii=False))),'mission_names_%s.py'%('gl' if self.region == 1 else 'jp'))
		else:
			target='%s/F_MISSION_MST.json'%(self.mst)
			if self.isFolder(target):
				with open(target) as data_file:    
					data = json.load(data_file)
					for m in data:
						G4L0YIB2=m['G4L0YIB2']#name
						qo3PECw6=str(m['qo3PECw6'])#id
						fin[qo3PECw6]={}
						fin[qo3PECw6]['name']=G4L0YIB2
					self.save('# -*- coding: utf-8 -*-\nmissions=%s'%unicode(json.dumps(fin, ensure_ascii=False)),'mission_names_%s.py'%('gl' if self.region == 1 else 'jp'))

	def parseLevels(self):
		_t={}
		target='%s/F_TEAM_LV_MST.json'%(self.mst)
		if self.isFolder(target):
			with open(target) as data_file:
				data = json.load(data_file)
				for m in data:
					qo3PECw6=int(m['7wV3QZ80'])#energy use
					Z0EN6jSh=int(m['B6H34Mea'])#energy use
					if qo3PECw6 in _t:
						_t[qo3PECw6]=Z0EN6jSh
					else:
						_t[qo3PECw6]={}
						_t[qo3PECw6]=Z0EN6jSh
				self.save('# -*- coding: utf-8 -*-\nlevels=%s'%unicode(json.dumps(_t, ensure_ascii=False)),'levels_%s.py'%('gl' if self.region == 1 else 'jp'))
				
	def parseUnit(self):
		_t={}
		target='%s/F_UNIT_MST.json'%(self.mst)
		if self.isFolder(target):
			with open(target) as data_file:
				data = json.load(data_file)
				for m in data:
					u18nfD7p=int(m['u18nfD7p'])#price
					woghJa61=str(m['3HriTp6B'])#unit id
					_t[woghJa61]={}
					_t[woghJa61]['price']=u18nfD7p
				self.save('# -*- coding: utf-8 -*-\nunits=%s'%unicode(json.dumps(_t, ensure_ascii=False)),'units_%s.py'%('gl' if self.region == 1 else 'jp'))

	def parseChallenges(self):
		_t={}
		target='%s/F_CHALLENGE_MST.json'%(self.mst)
		if self.isFolder(target):
			with open(target) as data_file:
				data = json.load(data_file)
				for m in data:
					qo3PECw6=int(m['qo3PECw6'])
					Pzn5h0Ga=str(m['Pzn5h0Ga'])
					Z0EN6jSh=int(m['Z0EN6jSh'])
					if qo3PECw6 in _t:
						_t[qo3PECw6][Z0EN6jSh]=Pzn5h0Ga
					else:
						_t[qo3PECw6]={}
						_t[qo3PECw6][Z0EN6jSh]=Pzn5h0Ga
				self.save('# -*- coding: utf-8 -*-\nchallenges=%s'%unicode(json.dumps(_t, ensure_ascii=False)),'challenges_%s.py'%('gl' if self.region == 1 else 'jp'))

	def cleanMissionName(self,n):
		return re.sub('.*NAME_','',n)

	def unpackAll(self):
		for file in os.listdir(self.mst):
			if '.dat' in file and ('_MST' in file or 'F_TEXT_' in file):
				self.getFileContent(file,'_MST' in file)

	def findMST(self):
		for i in self.updateData:
			if i['a4hXTIm0']=='F_MST_VERSION':
				self.log('found MST:%s'%(i['wM9AfX6I']))
				self.mst=i['wM9AfX6I']

if __name__ == "__main__":
	u=Updater()
	u.setTT([{"a4hXTIm0":"F_MST_VERSION","wM9AfX6I":"1308"},{"a4hXTIm0":"F_ABILITY_EXPLAIN_MST","wM9AfX6I":"89"},{"a4hXTIm0":"F_ABILITY_MST","wM9AfX6I":"112"},{"a4hXTIm0":"F_AI_MST","wM9AfX6I":"73"},{"a4hXTIm0":"F_ARCHIVE_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_AREA_MST","wM9AfX6I":"119"},{"a4hXTIm0":"F_AWARD_EXPLAIN_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_AWARD_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_AWARD_TYPE_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_BANNER_MST","wM9AfX6I":"73"},{"a4hXTIm0":"F_BATTLE_BG_MST","wM9AfX6I":"39"},{"a4hXTIm0":"F_BATTLE_SCRIPT_MST","wM9AfX6I":"32"},{"a4hXTIm0":"F_BEAST_BOARD_PIECE_EXT_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_BEAST_BOARD_PIECE_MST","wM9AfX6I":"30"},{"a4hXTIm0":"F_BEAST_CLASS_UP_MST","wM9AfX6I":"23"},{"a4hXTIm0":"F_BEAST_CP_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_BEAST_EXPLAIN_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_BEAST_EXP_PATTERN_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_BEAST_GROW_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_BEAST_MST","wM9AfX6I":"24"},{"a4hXTIm0":"F_BEAST_SKILL_MST","wM9AfX6I":"28"},{"a4hXTIm0":"F_BEAST_STATUS_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_CAPTURE_MST","wM9AfX6I":"9"},{"a4hXTIm0":"F_CHALLENGE_COMPLETE_REWARD_MST","wM9AfX6I":"12"},{"a4hXTIm0":"F_CHALLENGE_MST","wM9AfX6I":"52"},{"a4hXTIm0":"F_CHARACTER_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_CLSM_GRADE_MST","wM9AfX6I":"23"},{"a4hXTIm0":"F_CLSM_PROGRESS_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_CLSM_RANK_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_CLSM_ROUND_MST","wM9AfX6I":"29"},{"a4hXTIm0":"F_CRAFT_EXT_MST","wM9AfX6I":"53"},{"a4hXTIm0":"F_CREST_SWITCH_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_DEFINE_MST","wM9AfX6I":"45"},{"a4hXTIm0":"F_DIAMOND_MST","wM9AfX6I":"44"},{"a4hXTIm0":"F_DUNGEON_MST","wM9AfX6I":"102"},{"a4hXTIm0":"F_EFFECT_GROUP_MST","wM9AfX6I":"63"},{"a4hXTIm0":"F_EFFECT_MST","wM9AfX6I":"57"},{"a4hXTIm0":"F_ENCOUNT_FIELD_MST","wM9AfX6I":"23"},{"a4hXTIm0":"F_ENCOUNT_MONSTER_EXT_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_ENCOUNT_MST","wM9AfX6I":"41"},{"a4hXTIm0":"F_EQUIP_ITEM_EXPLAIN_MST","wM9AfX6I":"68"},{"a4hXTIm0":"F_EQUIP_ITEM_MST","wM9AfX6I":"83"},{"a4hXTIm0":"F_EXCHANGE_SHOP_ITEM_MST","wM9AfX6I":"23"},{"a4hXTIm0":"F_EXCHANGE_SHOP_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_EXPEDITION_DIFFICULTY_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_EXPEDITION_MST","wM9AfX6I":"38"},{"a4hXTIm0":"F_EXPLORE_AREA_MST","wM9AfX6I":"3"},{"a4hXTIm0":"F_EXPLORE_TIME_MST","wM9AfX6I":"1"},{"a4hXTIm0":"F_EXVIUS_POINT_REWARD_MST","wM9AfX6I":"6"},{"a4hXTIm0":"F_FIELD_TREASURE_MST","wM9AfX6I":"47"},{"a4hXTIm0":"F_FOOTPRINT_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_FUNCTION_MST","wM9AfX6I":"24"},{"a4hXTIm0":"F_GACHA_EFFECT_BLOCK_MST","wM9AfX6I":"26"},{"a4hXTIm0":"F_GACHA_EFFECT_PATTERN_MST","wM9AfX6I":"50"},{"a4hXTIm0":"F_GAME_TITLE_MST","wM9AfX6I":"27"},{"a4hXTIm0":"F_GUEST_UNIT_MST","wM9AfX6I":"32"},{"a4hXTIm0":"F_HERO_MST","wM9AfX6I":"7"},{"a4hXTIm0":"F_ICON_MST","wM9AfX6I":"76"},{"a4hXTIm0":"F_IMAGE_SWITCHING_MST","wM9AfX6I":"4"},{"a4hXTIm0":"F_IMPORTANT_ITEM_EXPLAIN_MST","wM9AfX6I":"33"},{"a4hXTIm0":"F_IMPORTANT_ITEM_MST","wM9AfX6I":"31"},{"a4hXTIm0":"F_ITEM_EXPLAIN_MST","wM9AfX6I":"62"},{"a4hXTIm0":"F_ITEM_EXT_BEAST_MST","wM9AfX6I":"25"},{"a4hXTIm0":"F_ITEM_MST","wM9AfX6I":"78"},{"a4hXTIm0":"F_JOB_MST","wM9AfX6I":"44"},{"a4hXTIm0":"F_LAND_EXPLAIN_MST","wM9AfX6I":"23"},{"a4hXTIm0":"F_LAND_MST","wM9AfX6I":"33"},{"a4hXTIm0":"F_LEARNING_MST","wM9AfX6I":"24"},{"a4hXTIm0":"F_LIMITBURST_LV_MST","wM9AfX6I":"52"},{"a4hXTIm0":"F_LIMITBURST_MST","wM9AfX6I":"62"},{"a4hXTIm0":"F_LOCATION_GOAL_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_LOGIN_BONUS_MST","wM9AfX6I":"10"},{"a4hXTIm0":"F_LOGIN_BONUS_SP_MST","wM9AfX6I":"15"},{"a4hXTIm0":"F_LOGIN_BONUS_SP_REWARD_MST","wM9AfX6I":"12"},{"a4hXTIm0":"F_LOGIN_BONUS_TOTAL_REWARD_MST","wM9AfX6I":"8"},{"a4hXTIm0":"F_MAGIC_EXPLAIN_MST","wM9AfX6I":"35"},{"a4hXTIm0":"F_MAGIC_MST","wM9AfX6I":"41"},{"a4hXTIm0":"F_MAP_EVENT_MST","wM9AfX6I":"40"},{"a4hXTIm0":"F_MAP_EXT_RESOURCE_MST","wM9AfX6I":"47"},{"a4hXTIm0":"F_MAP_OBJECT_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_MAP_ROUTE_MST","wM9AfX6I":"23"},{"a4hXTIm0":"F_MATERIA_EXPLAIN_MST","wM9AfX6I":"60"},{"a4hXTIm0":"F_MATERIA_LIMIT_MST","wM9AfX6I":"45"},{"a4hXTIm0":"F_MATERIA_MST","wM9AfX6I":"58"},{"a4hXTIm0":"F_MEDAL_EXCHANGE_MST","wM9AfX6I":"51"},{"a4hXTIm0":"F_MISSION_MST","wM9AfX6I":"126"},{"a4hXTIm0":"F_MONSTER_DICTIONARY_EXPLAIN_MST","wM9AfX6I":"51"},{"a4hXTIm0":"F_MONSTER_DICTIONARY_MST","wM9AfX6I":"50"},{"a4hXTIm0":"F_MONSTER_PASSIVE_SKILL_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_MONSTER_PASSIVE_SKILL_SET_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_MONSTER_SKILL_MST","wM9AfX6I":"88"},{"a4hXTIm0":"F_MONSTER_SKILL_SET_MST","wM9AfX6I":"61"},{"a4hXTIm0":"F_MONSTER_UNIQUE_ANIME_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_NPC_MST","wM9AfX6I":"31"},{"a4hXTIm0":"F_PICTURE_STORY_MST","wM9AfX6I":"44"},{"a4hXTIm0":"F_PLAYBACK_CHAPTER_MST","wM9AfX6I":"9"},{"a4hXTIm0":"F_PLAYBACK_EVENT_MST","wM9AfX6I":"5"},{"a4hXTIm0":"F_PLAYBACK_MAP_MST","wM9AfX6I":"4"},{"a4hXTIm0":"F_PLAYBACK_SEASON_MST","wM9AfX6I":"4"},{"a4hXTIm0":"F_PRODUCT_MST","wM9AfX6I":"10"},{"a4hXTIm0":"F_PURCHASE_AGE_LIMIT_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_QUEST_MST","wM9AfX6I":"28"},{"a4hXTIm0":"F_QUEST_SUB_MST","wM9AfX6I":"28"},{"a4hXTIm0":"F_RB_ABILITY_GROUP_MST","wM9AfX6I":"33"},{"a4hXTIm0":"F_RB_AI_PATTERN_MST","wM9AfX6I":"8"},{"a4hXTIm0":"F_RB_BONUS_RULE_MST","wM9AfX6I":"9"},{"a4hXTIm0":"F_RB_DEFINE_MST","wM9AfX6I":"9"},{"a4hXTIm0":"F_RB_FORBIDDEN_INFO_MST","wM9AfX6I":"10"},{"a4hXTIm0":"F_RB_LS_MST","wM9AfX6I":"11"},{"a4hXTIm0":"F_RB_LS_REWARD_MST","wM9AfX6I":"11"},{"a4hXTIm0":"F_RB_SS_MST","wM9AfX6I":"92"},{"a4hXTIm0":"F_RB_SS_REWARD_MST","wM9AfX6I":"17"},{"a4hXTIm0":"F_RB_TRADE_BOARD_MST","wM9AfX6I":"8"},{"a4hXTIm0":"F_RB_TRADE_BOARD_PIECE_MST","wM9AfX6I":"8"},{"a4hXTIm0":"F_RECIPE_BOOK_MST","wM9AfX6I":"60"},{"a4hXTIm0":"F_RECIPE_MST","wM9AfX6I":"61"},{"a4hXTIm0":"F_RESOURCE_MAP_MST","wM9AfX6I":"127"},{"a4hXTIm0":"F_RESOURCE_MAP_VERSION_MST_LOCALIZE","wM9AfX6I":"204"},{"a4hXTIm0":"F_RESOURCE_MST","wM9AfX6I":"124"},{"a4hXTIm0":"F_RESOURCE_VERSION_MST_LOCALIZE","wM9AfX6I":"247"},{"a4hXTIm0":"F_RULE_MST","wM9AfX6I":"7"},{"a4hXTIm0":"F_SCENARIO_BATTLE_GROUP_MST","wM9AfX6I":"45"},{"a4hXTIm0":"F_SCENARIO_BATTLE_MST","wM9AfX6I":"36"},{"a4hXTIm0":"F_SEASON_EVENT_ABILITY_MST","wM9AfX6I":"32"},{"a4hXTIm0":"F_SEASON_EVENT_ABILITY_TYPE_MST","wM9AfX6I":"32"},{"a4hXTIm0":"F_SEASON_EVENT_GROUP_FRIEND_LV_MST","wM9AfX6I":"10"},{"a4hXTIm0":"F_SG_TIME_DUNGEON_MST","wM9AfX6I":"7"},{"a4hXTIm0":"F_SHOP_MST","wM9AfX6I":"26"},{"a4hXTIm0":"F_SKILL_SUBLIMATION_BOARD_MST","wM9AfX6I":"7"},{"a4hXTIm0":"F_SKILL_SUBLIMATION_PIECE_MST","wM9AfX6I":"7"},{"a4hXTIm0":"F_SOUND_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_SP_CHALLENGE_MST","wM9AfX6I":"9"},{"a4hXTIm0":"F_STORE_ITEM_MST","wM9AfX6I":"51"},{"a4hXTIm0":"F_STORY_EVENT_MST","wM9AfX6I":"42"},{"a4hXTIm0":"F_STORY_FLOW_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_STORY_MST","wM9AfX6I":"23"},{"a4hXTIm0":"F_STORY_SUB_MST","wM9AfX6I":"25"},{"a4hXTIm0":"F_STRONGBOX_MST","wM9AfX6I":"25"},{"a4hXTIm0":"F_SUBLIMATION_RECIPE_MST","wM9AfX6I":"25"},{"a4hXTIm0":"F_SWITCH_MST","wM9AfX6I":"80"},{"a4hXTIm0":"F_SWITCH_TYPE_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_TEAM_LV_MST","wM9AfX6I":"26"},{"a4hXTIm0":"F_TELEPO_MST","wM9AfX6I":"24"},{"a4hXTIm0":"F_TEXT_ABILITY_EXPLAIN_LONG","wM9AfX6I":"145"},{"a4hXTIm0":"F_TEXT_ABILITY_EXPLAIN_SHORT","wM9AfX6I":"200"},{"a4hXTIm0":"F_TEXT_ABILITY_NAME","wM9AfX6I":"164"},{"a4hXTIm0":"F_TEXT_ABILITY_PARAM_MSG","wM9AfX6I":"40"},{"a4hXTIm0":"F_TEXT_ANALYTICS_ITEMS","wM9AfX6I":"13"},{"a4hXTIm0":"F_TEXT_ANALYTICS_LOCALIZE","wM9AfX6I":"12"},{"a4hXTIm0":"F_TEXT_ARCHIVE_NAME","wM9AfX6I":"46"},{"a4hXTIm0":"F_TEXT_AREA_NAME","wM9AfX6I":"125"},{"a4hXTIm0":"F_TEXT_AWARD_EXPLAIN","wM9AfX6I":"40"},{"a4hXTIm0":"F_TEXT_AWARD_NAME","wM9AfX6I":"40"},{"a4hXTIm0":"F_TEXT_AWARD_TYPE","wM9AfX6I":"39"},{"a4hXTIm0":"F_TEXT_BATTLE_SCRIPT","wM9AfX6I":"88"},{"a4hXTIm0":"F_TEXT_BEAST_NAME","wM9AfX6I":"70"},{"a4hXTIm0":"F_TEXT_BEAST_SKILL_DES","wM9AfX6I":"70"},{"a4hXTIm0":"F_TEXT_BEAST_SKILL_NAME","wM9AfX6I":"65"},{"a4hXTIm0":"F_TEXT_BUNDLE","wM9AfX6I":"68"},{"a4hXTIm0":"F_TEXT_CAPTURE_INFO","wM9AfX6I":"30"},{"a4hXTIm0":"F_TEXT_CHALLENGE_DESCRIPTION","wM9AfX6I":"68"},{"a4hXTIm0":"F_TEXT_CHALLENGE_NAME","wM9AfX6I":"107"},{"a4hXTIm0":"F_TEXT_CHARACTER_NAME","wM9AfX6I":"43"},{"a4hXTIm0":"F_TEXT_COLOSSEUM_GRADE","wM9AfX6I":"37"},{"a4hXTIm0":"F_TEXT_COLOSSEUM_MONSTER_GROUP_NAME","wM9AfX6I":"18"},{"a4hXTIm0":"F_TEXT_CRAFT","wM9AfX6I":"36"},{"a4hXTIm0":"F_TEXT_DAILY_QUEST_COMPLETED","wM9AfX6I":"18"},{"a4hXTIm0":"F_TEXT_DAILY_QUEST_DES","wM9AfX6I":"42"},{"a4hXTIm0":"F_TEXT_DAILY_QUEST_DETAIL","wM9AfX6I":"69"},{"a4hXTIm0":"F_TEXT_DAILY_QUEST_NAME","wM9AfX6I":"32"},{"a4hXTIm0":"F_TEXT_DEFINE","wM9AfX6I":"47"},{"a4hXTIm0":"F_TEXT_DIAMOND_NAME","wM9AfX6I":"66"},{"a4hXTIm0":"F_TEXT_DUNGEON_NAME","wM9AfX6I":"124"},{"a4hXTIm0":"F_TEXT_EXCHANGE_SHOP","wM9AfX6I":"38"},{"a4hXTIm0":"F_TEXT_EXCHANGE_SHOP_ITEM","wM9AfX6I":"37"},{"a4hXTIm0":"F_TEXT_EXPN_STORY","wM9AfX6I":"12"},{"a4hXTIm0":"F_TEXT_GACHA","wM9AfX6I":"179"},{"a4hXTIm0":"F_TEXT_GAME_TITLE_NAME","wM9AfX6I":"24"},{"a4hXTIm0":"F_TEXT_IMPORTANT_ITEM_EXPLAIN_LONG","wM9AfX6I":"72"},{"a4hXTIm0":"F_TEXT_IMPORTANT_ITEM_EXPLAIN_SHORT","wM9AfX6I":"69"},{"a4hXTIm0":"F_TEXT_IMPORTANT_ITEM_NAME","wM9AfX6I":"73"},{"a4hXTIm0":"F_TEXT_IMPORTANT_ITEM_SHOP","wM9AfX6I":"35"},{"a4hXTIm0":"F_TEXT_ITEM_EQUIP_LONG","wM9AfX6I":"157"},{"a4hXTIm0":"F_TEXT_ITEM_EQUIP_NAME","wM9AfX6I":"147"},{"a4hXTIm0":"F_TEXT_ITEM_EQUIP_SHORT","wM9AfX6I":"145"},{"a4hXTIm0":"F_TEXT_ITEM_EXPLAIN_LONG","wM9AfX6I":"136"},{"a4hXTIm0":"F_TEXT_ITEM_EXPLAIN_SHORT","wM9AfX6I":"121"},{"a4hXTIm0":"F_TEXT_ITEM_NAME","wM9AfX6I":"121"},{"a4hXTIm0":"F_TEXT_JOB_NAME","wM9AfX6I":"122"},{"a4hXTIm0":"F_TEXT_LAND_NAME","wM9AfX6I":"53"},{"a4hXTIm0":"F_TEXT_LIMIT_BURST_DES","wM9AfX6I":"130"},{"a4hXTIm0":"F_TEXT_LIMIT_BURST_NAME","wM9AfX6I":"112"},{"a4hXTIm0":"F_TEXT_MAGIC_EXPLAIN_LONG","wM9AfX6I":"92"},{"a4hXTIm0":"F_TEXT_MAGIC_EXPLAIN_SHORT","wM9AfX6I":"106"},{"a4hXTIm0":"F_TEXT_MAGIC_NAME","wM9AfX6I":"89"},{"a4hXTIm0":"F_TEXT_MAP_OBJECT","wM9AfX6I":"40"},{"a4hXTIm0":"F_TEXT_MATERIA_EXPLAIN_LONG","wM9AfX6I":"137"},{"a4hXTIm0":"F_TEXT_MATERIA_EXPLAIN_SHORT","wM9AfX6I":"138"},{"a4hXTIm0":"F_TEXT_MATERIA_NAME","wM9AfX6I":"119"},{"a4hXTIm0":"F_TEXT_MISSION","wM9AfX6I":"148"},{"a4hXTIm0":"F_TEXT_MISSION_PHASE","wM9AfX6I":"34"},{"a4hXTIm0":"F_TEXT_MONSTER_DICTIONARY_NAME","wM9AfX6I":"130"},{"a4hXTIm0":"F_TEXT_MONSTER_DIC_EXPLAIN_LONG","wM9AfX6I":"136"},{"a4hXTIm0":"F_TEXT_MONSTER_DIC_EXPLAIN_SHORT","wM9AfX6I":"119"},{"a4hXTIm0":"F_TEXT_MONSTER_NAME","wM9AfX6I":"139"},{"a4hXTIm0":"F_TEXT_MONSTER_PART_DIC_NAME","wM9AfX6I":"97"},{"a4hXTIm0":"F_TEXT_MONSTER_SKILL_NAME","wM9AfX6I":"132"},{"a4hXTIm0":"F_TEXT_MONSTER_SKILL_SET_NAME","wM9AfX6I":"40"},{"a4hXTIm0":"F_TEXT_NPC_NAME","wM9AfX6I":"103"},{"a4hXTIm0":"F_TEXT_PICTURE_STORY_NAME","wM9AfX6I":"26"},{"a4hXTIm0":"F_TEXT_PLAYBACK","wM9AfX6I":"22"},{"a4hXTIm0":"F_TEXT_QUEST","wM9AfX6I":"76"},{"a4hXTIm0":"F_TEXT_QUEST_SUB_DETAIL","wM9AfX6I":"89"},{"a4hXTIm0":"F_TEXT_QUEST_SUB_NAME","wM9AfX6I":"79"},{"a4hXTIm0":"F_TEXT_QUEST_SUB_STORY","wM9AfX6I":"99"},{"a4hXTIm0":"F_TEXT_QUEST_SUB_TARGET_PARAM","wM9AfX6I":"56"},{"a4hXTIm0":"F_TEXT_RB_ABILITY_GROUP_DESCRIPTION","wM9AfX6I":"10"},{"a4hXTIm0":"F_TEXT_RB_ABILITY_GROUP_NAME","wM9AfX6I":"11"},{"a4hXTIm0":"F_TEXT_RB_BONUS_RULE_DESCRIPTION","wM9AfX6I":"13"},{"a4hXTIm0":"F_TEXT_RB_BONUS_RULE_NAME","wM9AfX6I":"13"},{"a4hXTIm0":"F_TEXT_RB_FORBIDDEN_INFO_DESCRIPTION","wM9AfX6I":"10"},{"a4hXTIm0":"F_TEXT_RB_FORBIDDEN_INFO_NAME","wM9AfX6I":"13"},{"a4hXTIm0":"F_TEXT_RECIPE_BOOK_NAME","wM9AfX6I":"107"},{"a4hXTIm0":"F_TEXT_RECIPE_EXPLAIN_LONG","wM9AfX6I":"33"},{"a4hXTIm0":"F_TEXT_RULE_DESCRIPTION","wM9AfX6I":"16"},{"a4hXTIm0":"F_TEXT_SCENARIO_BATTLE","wM9AfX6I":"39"},{"a4hXTIm0":"F_TEXT_SEASON_EVENT_ABILITY_NAME","wM9AfX6I":"9"},{"a4hXTIm0":"F_TEXT_SEASON_EVENT_ABILITY_TYPE_DESCRIPTION","wM9AfX6I":"9"},{"a4hXTIm0":"F_TEXT_SEASON_EVENT_ABILITY_TYPE_NAME","wM9AfX6I":"9"},{"a4hXTIm0":"F_TEXT_SEASON_EVENT_DESCRIPTION","wM9AfX6I":"9"},{"a4hXTIm0":"F_TEXT_SEASON_EVENT_NAME","wM9AfX6I":"9"},{"a4hXTIm0":"F_TEXT_SHOP","wM9AfX6I":"48"},{"a4hXTIm0":"F_TEXT_SPCHALLENGE","wM9AfX6I":"10"},{"a4hXTIm0":"F_TEXT_STORY_NAME","wM9AfX6I":"56"},{"a4hXTIm0":"F_TEXT_STORY_SUB","wM9AfX6I":"80"},{"a4hXTIm0":"F_TEXT_SUBLIMATION_EXPLAIN","wM9AfX6I":"77"},{"a4hXTIm0":"F_TEXT_TELEPO_NAME","wM9AfX6I":"76"},{"a4hXTIm0":"F_TEXT_TEXT_EN","wM9AfX6I":"243"},{"a4hXTIm0":"F_TEXT_TICKER","wM9AfX6I":"62"},{"a4hXTIm0":"F_TEXT_TITLE","wM9AfX6I":"36"},{"a4hXTIm0":"F_TEXT_TOWN_EXPLAIN","wM9AfX6I":"75"},{"a4hXTIm0":"F_TEXT_TOWN_NAME","wM9AfX6I":"72"},{"a4hXTIm0":"F_TEXT_TOWN_STORE","wM9AfX6I":"90"},{"a4hXTIm0":"F_TEXT_TOWN_STORE_COMMENT","wM9AfX6I":"106"},{"a4hXTIm0":"F_TEXT_TOWN_STORE_OWNER_NAME","wM9AfX6I":"49"},{"a4hXTIm0":"F_TEXT_TRIBE","wM9AfX6I":"38"},{"a4hXTIm0":"F_TEXT_TROPHY_EXPLAIN","wM9AfX6I":"37"},{"a4hXTIm0":"F_TEXT_TROPHY_METER_SERIF","wM9AfX6I":"18"},{"a4hXTIm0":"F_TEXT_UNITS_NAME","wM9AfX6I":"115"},{"a4hXTIm0":"F_TEXT_UNIT_AFFINITY","wM9AfX6I":"126"},{"a4hXTIm0":"F_TEXT_UNIT_DESCRIPTION","wM9AfX6I":"147"},{"a4hXTIm0":"F_TEXT_UNIT_EVO","wM9AfX6I":"137"},{"a4hXTIm0":"F_TEXT_UNIT_EXPLAIN_SHOP","wM9AfX6I":"32"},{"a4hXTIm0":"F_TEXT_UNIT_FUSION","wM9AfX6I":"134"},{"a4hXTIm0":"F_TEXT_UNIT_SUMMON","wM9AfX6I":"133"},{"a4hXTIm0":"F_TEXT_URL","wM9AfX6I":"40"},{"a4hXTIm0":"F_TEXT_WORLD_NAME","wM9AfX6I":"40"},{"a4hXTIm0":"F_TICKER_DEFINE_MESSAGE_MST","wM9AfX6I":"4"},{"a4hXTIm0":"F_TICKER_LOG_CATEGORY_MST","wM9AfX6I":"4"},{"a4hXTIm0":"F_TICKER_MST","wM9AfX6I":"32"},{"a4hXTIm0":"F_TICKET_MST","wM9AfX6I":"7"},{"a4hXTIm0":"F_TITLE_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_TOWN_EXPLAIN_MST","wM9AfX6I":"24"},{"a4hXTIm0":"F_TOWN_MST","wM9AfX6I":"29"},{"a4hXTIm0":"F_TOWN_STORE_COMMENT_MST","wM9AfX6I":"33"},{"a4hXTIm0":"F_TOWN_STORE_MST","wM9AfX6I":"34"},{"a4hXTIm0":"F_TRIBE_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_TROPHY_EXPLAIN_MST","wM9AfX6I":"21"},{"a4hXTIm0":"F_TROPHY_METER_SERIF_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_TROPHY_MST","wM9AfX6I":"23"},{"a4hXTIm0":"F_TROPHY_REWARD_MST","wM9AfX6I":"22"},{"a4hXTIm0":"F_UNIT_CLASS_UP_MST","wM9AfX6I":"79"},{"a4hXTIm0":"F_UNIT_EXPLAIN_MST","wM9AfX6I":"56"},{"a4hXTIm0":"F_UNIT_EXP_PATTERN_MST","wM9AfX6I":"24"},{"a4hXTIm0":"F_UNIT_GROW_MST","wM9AfX6I":"24"},{"a4hXTIm0":"F_UNIT_LV_ACQUIRE_MST","wM9AfX6I":"27"},{"a4hXTIm0":"F_UNIT_MST","wM9AfX6I":"91"},{"a4hXTIm0":"F_UNIT_SERIES_LV_ACQUIRE_MST","wM9AfX6I":"72"},{"a4hXTIm0":"F_UNIT_SERIES_SWITCH_SKILL_MST","wM9AfX6I":"1"},{"a4hXTIm0":"F_UNIT_UNIQUE_ANIME_MST","wM9AfX6I":"48"},{"a4hXTIm0":"F_URL_MST","wM9AfX6I":"62"},{"a4hXTIm0":"F_WORLD_MST","wM9AfX6I":"22"}])