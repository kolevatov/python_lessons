# Download all images from site.

from urllib.request import urlopen
import re

url = "http://lenta.ru/"
image_name = 0
content = urlopen(url).read()

imgUrls = re.findall('img .*?src="(.*?)"', content.decode())

for img in imgUrls:
    if img.endswith(".jpg"):
        image_name += 1
        out = open('D:\\Python\\tmp\\image_' + str(image_name) + '.jpg', 'wb')
        out.write(urlopen(img).read())
        out.close()