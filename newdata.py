from menu import UI
from json import load, dump
from time import sleep
from color import color
ui = UI()

def main():
	with open("settings.json", "r") as f:
		data = load(f)
	ui.newData()
	choice = input(f"{color.okgreen}Enter Your Choice:  {color.reset}")
	if choice == "0":
        
		pass
	elif choice == "1":

		t(data, True)
		channel(data, True)
		pc(data, True)
		gems(data, True)
		sm(data, True)
		webhook(data, True)
		solve(data, True)
		Mode(data,True)
		api(data,True)

	elif choice == "2":
		t(data, False)
	elif choice == "3":
		channel(data, False)
	elif choice == "4":
		Mode(data, False)
	elif choice == "5":
		pc(data, False)
	elif choice == "6":
		gems(data, False)
	elif choice == "7":
		sm(data, False)
	elif choice == "8":
		webhook(data, False)
	elif choice == "9":
		solve(data, False)
	elif choice == "10":
		api(data, False)    
	else:
		ui.slowPrinting(f"{color.fail}[INFO] {color.reset}Invalid Choice")

def t(data,all):
 data['token'] = input("Please Enter Your Account Token: ")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()

def channel(data,all):
 data['channel'] = input("Please Enter Your Channel ID: ")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()

def Mode(data, all):
 data['Mode2'] = input("Do you want to use 2:1 mode?: (YES/NO)")
 #if data['Mode1'].lower() == "yes" or data['Mode1'].lower() == "no":
    #data['Mode2'] = input("Do you want to use 2:1 mode?: (YES/NO)") 

 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()

def pc(data,all):
 data['pc'] = input("Toggle Automatically Send Pray/Curse/No (PRAY/CURSE/NO): ")
 if data['pc'].lower() == "pray" or data['pc'].lower() == "curse":
    data['prayid'] = input("Do You Want To Pray/Curse A Specified User? If Yes Enter UserID. Otherwise Enter \"None\":")
 else:
    data['prayid'] = "None"
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()

def gems(data,all):
 data['gems'] = input("Toggle Automatically Use Gems Mode (YES/NO): ")
 if data['gems'].lower() == "yes":
    data['wcrate'] = input("Toggle Automatically Open Weapon Crate Mode (YES/NO):")
    data['lbox'] = input("Toggle Automatically Open Loot Box Mode (YES/NO):")
    data['usegem'] = input("(DO you prefer using gem from MIN or MAX) [MIN/MAX]:")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()

def sm(data,all):
 data['sm'] = input("Toggle Sleep Mode (YES/NO): ")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()

def webhook(data, all):
	data['webhook']['link'] = input("Toggle Discord Webhook (Enter Webhook Link. Otherwise Enter \"None\"): ")
	if data['webhook']['link'].lower() != "none":
		data['webhook']['ping'] = input("\t +)Do You Want To Ping. If Yes Enter User ID. Otherwise Enter \"None\": ")
	file = open("settings.json", "w")
	if data['webhook']['link'].lower() == "none":
		data['webhook']['link'] = None
	if data['webhook']['ping'] and data['webhook']['ping'].lower() == "none":
		data['webhook']['ping'] = None
	dump(data, file, indent = 4)
	file.close()
	ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
	if not all:
		main()

def solve(data, all):
 data['solve'] = input("Toggle Automatically Solve Captcha With AI (YES/NO): ")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()

def api(data, all):
 data['api'] = input("Do you have API 2Capcha, Enter API 2 Capcha If You have. Otherwise Enter \"None\". :")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()

if __name__ == "__main__":
  main()

