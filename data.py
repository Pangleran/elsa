from version import Version
from requests import get
from color import color
from menu import UI
from time import sleep
from re import findall
from inputimeout import TimeoutOccurred, inputimeout
import json
ui = UI()
class data:
	def __init__(self):
		self.commands=[
			"hunt",
			"battle"
			]
		self.wbm = [13,18]
		self.OwOID = '408785106942164992'
		self.totalcmd = 0
		self.totaltext = 0
		self.username=""
		self.userid = ""
		self.checknogem=False
		self.stopped = False
		self.version = int(''.join(map(str, Version)))
		self.wait_time_daily = 60
		self.channel2 = []
		#Gems
		self.checkgemtime=0
		self.checkusegem = 0
		self.skipcheckgem=0
		
		with open('settings.json', "r") as file:
			data = json.load(file)
			self.token = data["token"]
			self.channel = data["channel"]
			self.gems = data["gems"]
			self.wcrate = data["wcrate"]
			self.lbox = data["lbox"]
			self.usegem = data["usegem"]
			self.sm = data["sm"]
			self.pc = data["pc"]
			self.prayid = data["prayid"]
			self.em = data["em"]
			self.allowedid = data["allowedid"]
			self.webhook = data["webhook"]
			self.solve = data['solve']
			self.Mode2 = data['Mode2']
			self.Mode1 = data['Mode1']
			#PENTING
			self.dmsID = None
			self.channelocf =data["channelocf"]
			self.api=data['api']
		self.tokenbackup=self.token
a = data()