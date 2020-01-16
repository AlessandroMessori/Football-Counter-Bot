import datetime

def word_count(str):
    counts = dict()
    words = str.split()
    counters = list()

    for word in words:
        if word in counts:
            counts[word] += 1       
        else:
            counts[word] = 1

    return counts

def getText(counts):

    text = ''

    for word,count in counts.items():
      text += word + " " + str(count) + '\n'
    
    return text
    
now = datetime.datetime.now()
today = str(now.year) + "/" + str(now.month if now.month > 9 else "0" + str(now.month)) + "/" + str(now.day if now.day > 9 else "0" + str(now.day))
f = open("/home/pi/Desktop/data/Posts/"+ today+"/all.csv")
counts = word_count(f.read())
text = getText(counts)

wf = open("/home/pi/Desktop/data/Counters/"+today+".txt","w")
wf.write(text)



