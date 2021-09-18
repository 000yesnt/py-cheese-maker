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
```optional arguments:
  -h, --help   show this help message and exit
  --path PATH  path to use as input
  -s S         string to use at the start, supports formatting ({ln} = amount of files in input)
  -r R         framerate of output video
  -o O         name of output mp4
  ```
### why are you doing this
i dont fucking know

# look at it

![look](https://octodex.github.com/images/inflatocat.png)