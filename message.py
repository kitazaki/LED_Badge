import sys
import unicodedata
from PIL import Image, ImageDraw, ImageFont

args = sys.argv
if len(args) < 2:
  print("usage:", args[0], "message")
  sys.exit()

text = args[1]
if len(text) < 1:
  print("usage:", args[0], "message")
  sys.exit()

def get_east_asian_width_count(text):
  count = 0
  for c in text:
    if unicodedata.east_asian_width(c) in 'FWA':
      count += 2
    else:
      count += 1
  return count

length = get_east_asian_width_count(text)
img = Image.new("RGB",(length*5,11),(0,0,0))

draw = ImageDraw.Draw(img)
fontpath = "./PixelMplus10-Regular.ttf"
#fontpath = "./PixelMplus10-Bold.ttf"
draw.font = ImageFont.truetype(fontpath, 10)
draw.text((0,0), text, (255, 255, 255))

img.save("./message.png")

