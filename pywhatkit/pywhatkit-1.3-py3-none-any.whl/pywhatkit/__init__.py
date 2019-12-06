import time
import webbrowser as web
import pyautogui as pg
import wikipedia
import requests
from bs4 import BeautifulSoup

last = time.time()

sleeptm = "None, You can use this function to print the remaining time in seconds."
def prnt_sleeptm():
    return sleeptm

def check_window():
    web.open("https://www.google.com")
    pg.alert("If the browser's window is not maximised\nMaximise and then close it if you want,\nor sendwhatmsg() function will not work","Pywhatkit")
    
def sendwhatmsg(phone_no, message, time_hour, time_min, print_waitTime=True):
    '''Sends whatsapp message to a particulal number at given time
Phone number should be in string format not int
***This function will not work if the browser's window is minimised,
first check it by calling 'check_window()' function'''
    if "+" not in phone_no:
        raise Exception("Country code missing from phone_no")
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)+(time_min*60)

    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm

    if lefttm < 60:
        raise Exception("Call time must be greater than one minute")

    else:
        global sleeptm
        sleeptm = lefttm-60
        if print_waitTime :
            print(prnt_sleeptm(),"+ 60 seconds left")
        time.sleep(sleeptm)
        web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
        time.sleep(60)
        width,height = pg.size()
        pg.click(width,height/2)
        pg.press('enter')

def info(topic,lines=3):
    '''Gives information on the topic'''
    spe = wikipedia.summary(topic, sentences = lines)
    print(spe)
    
def playonyt(title):
    '''Opens YouTube video with following title'''
    url = 'https://www.youtube.com/results?q=' + title
    sc = requests.get(url)
    sctext = sc.text
    soup = BeautifulSoup(sctext,"html.parser")
    songs = soup.findAll("div",{"class":"yt-lockup-video"})
    song = songs[0].contents[0].contents[0].contents[0]
    songurl = song["href"]
    web.open("https://www.youtube.com"+songurl)

def search(topic):
    '''Searches about the topic on Google'''
    link = 'https://www.google.com/search?q={}'.format(topic)
    web.open(link)

try : 
    requests.get("https://www.google.com")
    current = time.time()
    tyme = current-last
        
except Exception:
    exc = ("NO INTERNET - Pywhatkit needs active internet connection")
    raise Exception(exc)

if tyme >= 5:
        raise Warning("INTERNET IS SLOW, extraction of information might take longer time")
#Made by Ankit Raj Mahapatra ;-)
