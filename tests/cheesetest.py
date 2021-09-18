import CheeseFactory
from PIL import Image
im = CheeseFactory.MakeCheeseFrame(2, (256, 256), imagepath="ffmpeg-logo.png")
im.show()