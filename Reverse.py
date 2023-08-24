from PIL import Image
import sys

Image.MAX_IMAGE_PIXELS = 933120000

im = Image.open(sys.argv[1])
for y in range(im.size[1]):
    for x in range(im.size[0]):
        pixel = im.getpixel((x,y))
        im.putpixel((x,y),(255-pixel[0], 255-pixel[1], 255-pixel[2]))
im.save("".join(sys.argv[1].split(".")[0:-1])+"_reverse.png")