import requests
import datetime
import json

def getText(path):
  f = open(path,"r")
  text = f.read()
  return text

def getCountersList(text):
  counters = list()
  words = text.split()
  i = 0

  while i < len(words):
    elem = (words[i],int(words[i+1]))
    counters.append(elem)
    i = i+2

  return counters

def getSortedOutput(counters):
  counters = sorted(counters, key=lambda x: x[1])
  fillCounters = list()
  
  for elem in counters:
    if (elem[0][0].isupper()):
       fillCounters.append(elem)
  
  newCounters = list()

  for i in range(1,30):
    newCounters.append(fillCounters[-i])
  
  return newCounters

def getMessage(counters):
  message = ''
  
  for counter in counters:
    message = message + counter[0] + " " + str(counter[1]) + '\n'
  
  return message

def telegram_bot_sendtext(bot_message):
    
    cred = open("/home/pi/Desktop/FootballCounterBot/credentials.json")

    data = json.load(cred)
    
    bot_token = data["token"]
    bot_chatID = data["chatId"]
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

now = datetime.datetime.now()
today = str(now.year) + "/" + str(now.month) + "/" + str(now.day if now.day > 9 else "0" + str(now.day))
message = getText("/home/pi/Desktop/data/Counters/"+today+".txt")
counters = getSortedOutput(getCountersList(message))
output = getMessage(counters)

send = telegram_bot_sendtext(output)
print(send)

