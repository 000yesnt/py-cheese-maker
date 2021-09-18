# py-cheese-maker
[here's an example of what this script *tries* to do](https://cdn.discordapp.com/attachments/285880764493725696/888102683456716820/top_5000_cheeses_1_1_1.mp4)

### what does it do exactly
if the example video wasnt enough, it basically generates and stitches frames for a slideshow/compilation video using PIL and FFmpeg.

### how to use
1. Make sure you have FFmpeg, Python and necessary modules.

   Windows: double click the setup.bat

   Linux: ``chmod +x setup.sh && ./setup.sh`` (or just double click the setup script)
2. Run main.py and it should Just Work(tm)

### arguments
``--path``: path of the input image directory. by default it's the "in" folder. **Images must be jpgs or pngs!**

``-s``: string to use at the first frame. supports formatting: ``{ln}`` for amount of input images. default is ``top {ln} images``

``-r``: framerate of the video. this affects the length of the resulting video, so choose a low value. default 1

``-o``: name of the output mp4. default "result"

``-w`` and ``-h``: width and height of the video. default 256x256
### why are you doing this
i dont fucking know, boredom? curiosity?

# look at it

![look](https://octodex.github.com/images/inflatocat.png)