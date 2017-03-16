# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime
from resources.lib.common_variables import *
from resources.lib.directory import *
from resources.lib.youtubewrapper import *
from resources.lib.watched import * 

fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Vodlahav', 'fanart.jpg'))
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Vodlahav/resources/img', ''))

def CATEGORIES():
        addDir3('חיפוש ביוטיוב','plugin://plugin.video.youtube/kodion/search/input/',35,art + 'ysearch.png')
        addDir('אוכל ובישול','url',17,art + 'cooking.png')
        addDir('אוכל', 'url', 42, art + 'lacook.jpg')
        addDir('מוזיקה','url',41,art + 'lamusic.jpg')
        addDir('הופעות חיות','url',43,art + 'lamusic.jpg')
        addDir('סרטים','url',44,art + 'lamusic.jpg')
        addDir('דעת','url',40,art + 'lahav.jpg')
        addDir('שעה היסטורית', 'url', 45, art + 'hrsagor.jpg')
		
def lahav():
        addDir('אלוהים ויהדות בלי סיפורי אגדות','PLPpE92HjGRlnuEuWDq_HWe8RzuGKLvSoV',1,art + 'lahav.png')
        addDir('ד"ר יובל הררי - היסטוריה עולמית','PLfHmQCZe1ktg9G7Too6IjmJfVPEeHfXCq',1,art + 'lahav.jpg')
        addDir('קורס תכנות בפייתון','PLPpE92HjGRlmznhxNpEEDC6fgTQDO32EN',1,art + 'lahav.jpg')

def lahist():
        addDir('שעה היסטורית עם פרופ הרסגור', 'PLi3ABZgzV07L9O3Mh3ELo0Fg2jZo-Dxi4', 1, art + 'hrsagor.jpg')
        addDir('ד"ר יובל הררי - היסטוריה עולמית', 'PLfHmQCZe1ktg9G7Too6IjmJfVPEeHfXCq', 1, art + 'lahav.jpg')
        addDir('בית שני', 'PLC4C505694FD95258', 1, art + 'lahav.jpg')
        addDir('ישראל הקדום, ארכיאולוגיה ומקרא', 'PLPpE92HjGRlkYELCoBb0BhQsSWDLqyaQr', 1, art + 'lahav.jpg')

def lamusic():
        addDir('שירים נבחרים','PLPpE92HjGRlmMBqCBdPiTzfPB74LRRWfk',1,art + 'lamusic.png')
        addDir('שירים שאהבתי', 'PLPpE92HjGRll4aSe4awPYd5faMEoD_pl4&autoplay=1&loop=1', 1, art + 'lamusic.png')
        addDir('My 80s - 90s Rock Playlist','PL3485902CC4FB6C67',1,art + 'lamusic.jpg')
        addDir('שירים עבריים הותיקים ויפים','PLPpE92HjGRll_a0pSe7VGgdbdGUbjqbpf',1,art + 'lamusic.jpg')
        addDir('Relax','PLsxPn-1_PWG9Gef0JsbLIXhT1g3SGTpDw',1,art + 'lamusic.jpg')
        addDir('מוזיקה מרגיעה וסרטי טבע','PLPpE92HjGRlmy30bcbi_ggnoTjmAEp7mq',1,art + 'lamusic.jpg')
        addDir('Celtic Music Relaxing','PLPpE92HjGRlmJB5XW4ti6vYxNrNi4mQfd',1,art + 'lamusic.jpg')
        addDir('ENIGMA','PLPpE92HjGRlmt5I_YrMXT6cw7uCzOn9SV',1,art + 'lamusic.jpg')
        addDir('סתם שירים יפים עברית','PLPpE92HjGRll_gMbji8ymDxPnxv80EKVK',1,art + 'lamusic.jpg')
        addDir('סתם שירים יפים לעוזית','PLPpE92HjGRlmnOg9MvV_Yue884FlgjuXt',1,art + 'lamusic.jpg')
        addDir('7 Seconds','PLPpE92HjGRllfDso9JQXX8omcCXx_k2Pn',1,art + 'lamusic.jpg')
        addDir('ColdPlay','PLPpE92HjGRlm_e974LZWKWgQsbsRammht',1,art + 'lamusic.jpg')
        addDir('מוזיקה מהעולם','PLPpE92HjGRlnBYIC-NpwU1PcWtW4F4cMe',1,art + 'lamusic.jpg')
        addDir('הופעות חיות', 'PLPpE92HjGRllxp4mUf6F08aSGig9kqXcZ', 1, art + 'lamusic.jpg')

def lacook():
        addDir('מתכונים נבחרים','PLPpE92HjGRllnKB-aztb5TPBHWg4W9Dwm',1,art + 'lacook.jpg')
        addDir('ארוחת ערב - tasty','PL8zglt-LDl-iwBHEl3Pw1IhWGp9cfgMrc',1,art + 'lacook.jpg')
        addDir('ארוחת בוקר - tasty','PL8zglt-LDl-i0xOKNOyfp3MHejOv1Kyov',1,art + 'lacook.jpg')
        addDir('מתאבנים - tasty','PL8zglt-LDl-jp8PpdleYo6o2-ogLAxjzD',1,art + 'lacook.jpg')
        addDir('תוכניות אוכל מיוחד','PLPpE92HjGRlkBeYOQuXza0z7L-XUkGCJ0',1,art + 'lacook.jpg')

def lashow():
        addDir('לילה גוב עונה ראשונה','PL0HqiSqEXnIBp1UWXrlRkas-hpy-w_dn0',1,art + 'lacook.jpg')
        addDir('לילה גוב עונה שנייה','PL0HqiSqEXnIDYk1o0Timz69ZKhTUBq6G3',1,art + 'lacook.jpg')
        addDir('לילה גוב עונה שלישית','PL0HqiSqEXnIBmCUhhyw6IUI3b9g9tfaly',1,art + 'lacook.jpg')
        addDir('לילה גוב עונה רביעית','PL3VbzQ6kUVhEgzu-swdD2LoWoWrBM1qC2',1,art + 'lacook.jpg')
        addDir('לילה גוב עונה חמישית','PL0HqiSqEXnIBhap-Jl7qdAQtMXIZOinPD',1,art + 'lacook.jpg')
        addDir('הופעות חיות','PLPpE92HjGRllxp4mUf6F08aSGig9kqXcZ',1,art + 'lacook.jpg')

def lamovies():
        addDir('סרטי מדע בדיוני','PLPpE92HjGRlnWico2Vzc-nsFWQrmUfoUi',1,art + 'lacook.jpg')
        addDir('סרטים שלי פנטזיה','PLPpE92HjGRllhu-DxYhw3euNYM_yKHldY',1,art + 'lacook.jpg')

def cooking():
        addDir('מתכונים כלליים','PLF685A5B80B86FE3B',1,art + 'cooking.png')
        addDir('מתכונים כשרים','PL3zcxKFd7HIKL3oSXq6rCH-fvFGCaOaS9',1,art + 'cooking.png')
        addDir('מתכונים. מטבח יהודי ומזרח ים תיכוני','PLRUtxvlnaqwx3KugKPtd4C3Iexv0Ee5U3',1,art + 'cooking.png')
        addDir(''+translate(70002)+'','PLnzhIyrsnB5YJYfCNr4B9ewwTMhzS8pn9',1,art + 'cooking.png')
        addDir(''+translate(70004)+'','PLnzhIyrsnB5ZNE1PhI4hWyyvE6gbieoFs',1,art + 'cooking.png')       
        addDir('סודות מתוקים עונה 1','ELAMi0KPlVcsg',1,art + 'cooking.png')
        addDir('סודות מתוקים עונה 3','ELmeqByVOghVE',1,art + 'cooking.png')
        addDir('שגב במטבח','CLWEuLXV2ejHk',1,art + 'cooking.png')         
        addDir('מיקי שמו','PLqQIVRFHrR1rsA0RqsAkzMxa2Xc4tcO25',1,art + 'cooking.png')
        addDir('בישולים','PLkSacTgmGKr6a6sPE1F7q3VF7T00lffQc',1,art + 'cooking.png')
        addDir('בישולים 2','PLdDyYBhRKiyG21-epuoI57b7zBfAyQcvI',1,art + 'cooking.png') 
        addDir('לאכול - יסודות הבישול - ויקטור גלוגר','PL8jMo70ebRM5dsJOjJXzGylZny1dnFPI7',1,art + 'cooking.png')         
        addDir('לאכול - חומרי גלם - אוראל קמחי','PL8jMo70ebRM778yBMGXg5Bb0wKm60wtb3',1,art + 'cooking.png')
        addDir('לאון אל דנטה','PL8jMo70ebRM7nnRez1MyfKBFLTj9jzl1V',1,art + 'cooking.png')
        addDir('במטבח עם אמא','PL8jMo70ebRM6gYuy9d7yoPLTGg1asK78w',1,art + 'cooking.png')
        addDir('מיקי שמו עושה בית ספר - עונה ראשונה','PL8jMo70ebRM7tvFCZsiXhakIsbDwHOe9c',1,art + 'cooking.png')         
        addDir('מועדון ארוחת הבוקר עם אביב משה','PL8jMo70ebRM6CAq8sKdjfI4_N3qUO5U1j',1,art + 'cooking.png')
        addDir('פשוט לאפות','PL8jMo70ebRM6aT0ZciSlv_YhP2Kjp1tuk',1,art + 'cooking.png')
        addDir('המטבחון של ירון','PL156601B302C8F462',1,art + 'cooking.png')
		
def vodil(url):

    ok=True        
    xbmc.executebuiltin('XBMC.Container.Update(%s)' % url )
    return ok
        
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param


params=get_params()
url=None
name=None
mode=None
iconimage=None
page = None
token = None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except:
	try: 
		mode=params["mode"]
	except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: token=urllib.unquote_plus(params["token"])
except: pass
try: page=int(params["page"])
except: page = 1

print ("Mode: "+str(mode))
print ("URL: "+str(url))
print ("Name: "+str(name))
print ("iconimage: "+str(iconimage))
print ("Page: "+str(page))
print ("Token: "+str(token))

		
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        if mode==35 :
               ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
               return ok
				
def create_directory(dir_path, dir_name=None):
    if dir_name:
        dir_path = os.path.join(dir_path, dir_name)
    dir_path = dir_path.strip()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        return_youtubevideos(name,url,token,page)

elif mode==5: 
        play_youtube_video(url)

elif mode==6:
        mark_as_watched(url)

elif mode==7:
        removed_watched(url)

elif mode==8:
        add_to_bookmarks(url)

elif mode==9:
        remove_from_bookmarks(url)
		
elif mode==10:
        print ""+url
        lifestyle()
		
elif mode==11:
        print ""+url
        documentary()

elif mode==12:
        print ""+url
        kids()

elif mode==13:
        print ""+url
        Music()
        
elif mode==14:
        print ""+url
        travel()

elif mode==15:
        print ""+url
        Sports()

elif mode==16:
        print ""+url
        liveshows()

elif mode==17:
        print ""+url
        cooking()
			
elif mode==18:
        print ""+url
        junior()
		
elif mode==19:
        print ""+url
        nickjunior()

elif mode==20:
        print ""+url
        nicklodeon()

elif mode==21:
        print ""+url
        logy()

elif mode==22:
        print ""+url
        hop()

elif mode==23:
        print ""+url
        hopy()	

elif mode==24:
        print ""+url
        luly()

elif mode==25:
        print ""+url
        baby()

elif mode==26:
        print ""+url
        hot()

elif mode==27:
        print ""+url
        kidstv()

elif mode==28:
        print ""+url
        ch23()

elif mode==29:
        print ""+url
        zoom()		

elif mode==30:
        print ""+url
        dsjunior()

elif mode==31:
        print ""+url
        NBA()

elif mode==32:
        print ""+url
        basket()

elif mode==33:
        print ""+url
        soccer()		

elif mode==34:
        print ""+url
        box()		

elif mode==37:
        print ""+url
        nostal()				
		
elif mode==35:
        vodil(url)
	
elif mode==38:
        print ""+url
        movies()

elif mode==39:
        print ""+url
        poker()
elif mode==40:
        print ""+url
        lahav()

elif mode==41:
        print ""+url
        lamusic()

elif mode==42:
        print ""+url
        lacook()

elif mode==43:
        print ""+url
        lashow()

elif mode==44:
        print ""+url
        lamovies()

elif mode == 45:
        print "" + url
        lahist()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
