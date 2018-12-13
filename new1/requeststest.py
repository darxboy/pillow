import  requests

from io import BytesIO
from PIL import Image

#params = {"q" :"sukses"}

#r = requests.get("http://bing.com/search" , params=params)

r = requests.get("https://hdlislamicwallpapers.files.wordpress.com/2012/08/allah_059_by_almubdi-d38qjw6.jpg")
print("status:", r.status_code)
image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image." + image.format

#print(r.url)
#f = open("./page.html", "w+")
#f.write(r.text)

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")