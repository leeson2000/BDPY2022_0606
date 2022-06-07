from urllib.request import urlopen
from PIL import Image

url1 = "https://www.uuu.com.tw/Public/content/ad/home/220301_AWSpromote.jpg"

stream1 = urlopen(url1)
image1 = Image.open(stream1)
image1.save("images/demo46.jpg")
stream1.close()
halfsize = (image1.size[0] // 2, image1.size[1] // 2)
image2 = image1.resize(halfsize)
image2.save("images/small.jpg")
transposes = [Image.Transpose.ROTATE_90, Image.Transpose.ROTATE_180, Image.Transpose.ROTATE_270]
fileNames = ["r90.jpg", "r180.jpg", "r270.jpg"]
for t, f in zip(transposes, fileNames):
    rot = image2.transpose(t)
    rot.save("images/%s" % f)
r60 = image2.rotate(60)
r60.save("images/r60.jpg")