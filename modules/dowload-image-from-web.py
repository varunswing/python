import urllib.request
import random

def download_web_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

download_web_image("https://www.vemco.com/wp-content/uploads/2012/09/image-banner2.jpg")