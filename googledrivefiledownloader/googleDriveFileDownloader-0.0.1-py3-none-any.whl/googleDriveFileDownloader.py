import os
import requests
from bs4 import BeautifulSoup 

class googleDriveFileDownloader():
    
    def __init__(self):
        print("Imported !")

    def downloadFile(self,url):

        if(url.startswith("https://drive.google.com/uc")):
            print("Download is starting")

            URL = "https://drive.google.com/uc?id=0BzQ6rtO2VN95bndCZDdpdXJDV1U&export=download"
            r = requests.get(URL) 

            soup = BeautifulSoup(r.content, 'html5lib') 

            FileName = soup.select('.uc-name-size')

            print(FileName[0].select('a')[0].text)

            print("before")

            url = r'wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=0BzQ6rtO2VN95cmNuc2xwUS1wdEE" -O- | sed -rn "s/.*confirm=([0-9A-Za-z_]+).*/\1\n/p")&id=0BzQ6rtO2VN95cmNuc2xwUS1wdEE" -O cnn_stories_tokenized.zip && rm -rf /tmp/cookies.txt'

            return(os.system(url))
        else:
            return "Unable to process the URL \n Make sure to have it in this format 'https://drive.google.com/uc...'"