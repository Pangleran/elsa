import os, time, sys
from version import version
from color import color
class UI:

	@classmethod
	def slowPrinting (cls, text):
		for letter in text:
			sys.stdout.write(letter)
			sys.stdout.flush()

			time.sleep(0.000001)
		print()

	@classmethod
	def m4(cls):
		print(f"""\
{color.white}Sayang Kamu...{color.reset}
{color.cyan}███████╗██╗     ███████╗{color.reset}
{color.cyan}██╔════╝██║     ██╔════╝{color.reset}
{color.cyan}█████╗  ██║     ███████╗{color.reset}
{color.cyan}██╔══╝  ██║     ╚════██║{color.reset}
{color.cyan}███████╗███████╗███████║   {color.reset}
{color.cyan}╚══════╝╚══════╝╚══════╝	{color.reset}""")
		print()

	@classmethod
	def logo(cls):
		print("╔════════════════════════════════════╗")
		print(f" {color.yellow}Dev {color.okcyan}ahihiyou20{color.yellow} the Original version.{color.reset}")
		print(f" {color.yellow}Dev {color.okcyan}Iris{color.yellow} the Solve version.{color.reset}")
		print(f"    {color.purple}Version : {version} mode VIP ONLY{color.reset}")
		print("╚════════════════════════════════════╝")

	@classmethod
	def start(cls):
		print("╔═══════════════════════════════╗")
		print(f"     {color.red}[1]{color.reset} Load Data")
		print(f"     {color.red}[2]{color.reset} Setting data")
		print("╚═══════════════════════════════╝")

	@classmethod
	def newData(cls):
		print("╔═══════════════════════════════════════════╗")
		print()
		print("         [0] Exit And Save")
		print("         [1] Change All Settings")
		print("         [2] Change Token")
		print("         [3] Change Channel")
		print("         [4] Change Mode Grind")
		print("         [5] Change Pray/Curse Mode")
		print("         [6] Change Gems Mode")
		print("         [7] Change Sleep Mode")
		print("         [8] Change Webhook Settings")
		print("         [9] Change Solve Captcha")
		print("         [10] Change API 2Capcha Setting")		
		print()
		print("╚═══════════════════════════════════════════╝")


elsa='''
Sayang Kamu...
███████╗██╗     ███████╗
██╔════╝██║     ██╔════╝
█████╗  ██║     ███████╗
██╔══╝  ██║     ╚════██║
███████╗███████╗███████║
╚══════╝╚══════╝╚══════╝
'''
