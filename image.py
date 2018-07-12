import random
import urllib.request

def download_web_image(url):
    name= random.randrange(1, 1000)
    file_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, file_name)

download_web_image("https://www.facebook.com/ItsaCancerThing/photos/a.206621396346773.1073741828.206168526392060/675441999464708/?type=3&theater")