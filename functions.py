import time, datetime,os,sys

global bot,user

bot = ['saara']
user = ['sajid']
path = os.getcwd()+'/Data/'

def day():
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = datetime.datetime.now().day
    if day>= 7:
        day = day%7
    return days[day]

def month():
    mon = ['','January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    month = datetime.datetime.now().month
    return mon[month]

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour <= 12:
        return 'morning'
    elif hour <= 18:
        return 'afternoon'
    return 'evening'
    
def slow(txt):
	for char in txt:
  	  time.sleep(0.05)
  	  sys.stdout.write(char)
  	  sys.stdout.flush()

def bot_name():
    for cha in bot[-1].upper()+' : ':
  	  sys.stdout.write(cha)
  	  sys.stdout.flush()

def clear():
    import os
    os.system( 'clear' )

def start():
    slow(f"Hello from the other side !\nI'm an AI based ChatBot.You can talk to me like your friend.I can learn new things & even remember people names. My \ndefault name is SAARA but you can change it anytime you like\n\nWhat should I call you sir ?")
    sir = input(" ") or 'USER'
    user.append(sir)
    clear()
    slow(f"Hello {sir.upper()}, good {greet()} ! \nI'm glad to be at your service\nYou can start by saying Hi,Hello or whatever xD !")
 
