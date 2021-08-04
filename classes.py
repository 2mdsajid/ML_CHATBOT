import datetime, json,os,time
from functions import clear,greet,day,month,path,slow,bot,user
from model import train_model, save_data

global bot,user,in_known
in_known = False

class Time:
    def get(text,inp):
        hour = int(datetime.datetime.now().hour)
        if hour >= 12:
            hour = hour%12
        slow(text)
        slow(f"\nit's {greet()} {hour}:{datetime.datetime.now().minute}")
        
class Date:
    def get(text,inp):
        slow(text)
        slow(f"\nit's {day()}\n{month()} {datetime.datetime.now().day},{datetime.datetime.now().year}")

class Bot:
    def get(text,inp):
        slow(text.replace('$',bot[-1]))

class BotName:
    def get(text,inp):
        slow("what you'd like to call me ?")
        name = input("\n> ")
        bot.append(name)
        slow(text.replace('$',bot[-1]))

class User:
    def get(text,inp):
        slow(text.replace('$',user[-1]))

class UserName:
    def get(text,inp):
        slow('what should I call you sir ?')
        name = input("\n> ")
        user.append(name)
        slow(text.replace('$',user[-1]))

class TrainData:
    def get(text,inp):
        slow(text+'\n')
        save_data()
        train_model()

class Quit:
    def get(text,inp):
        slow(text)
        exit()

class Clear:
    def get(text,inp):
        clear()
        slow(text)
        
class Person:        
        def add(name,data,desc):
            data[name] = desc
            new_file = open(path+'KnownPerson.json','w')
            json.dump(data,new_file,indent=4)
        
        def known(name=""):
            old_file = open(path+'KnownPerson.json','r')
            old_data = json.load(old_file)
            
            if name in old_data.keys():
                    slow(f'\n{old_data[name]}')
            else:
                slow(f'\n(Searching........)')
                time.sleep(1)
                slow(f'\noops !\nLooks like there is no data available about {name} !\nTell me so that I can store for the next time !\n')
                desc = input('\n> ')
                if "leave" in desc.split():
                    slow("I also hate that person !")
                    pass
                else:
                    slow(f'\nDone ! {name} is in my memory now !')
                    Person.add(name,old_data,desc)
            
        def get(text,inp):
            f = open(path+'names.json','r')
            data = json.load(f)
            
            female = data['names'][0]['female']
            male = data['names'][0]['male']
            names = male+female
            iterated_names = []
            a = inp.lower().split()
           
            for name in names:
                if name in a:
                    slow(text.replace('$',name))
                    time.sleep(1)
                    in_known = True
                    Person.known(name)
                    break
                else:
                    in_known = False

            if not in_known:
                slow('sorry ! I\'ve got no idea')
                            
      