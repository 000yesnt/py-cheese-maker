from PIL import Image, ImageDraw, ImageFont
from enum import Enum
import textwrap

class FrameTypes(Enum):
    FT_TEXT_SMALL = 0
    FT_TEXT_LARGE = 1
    FT_IMAGE = 2

def makeCheeseFrame(type: int, size: tuple, **kwargs):
    # TODO: jesus this is ugly
    """Generates a frame for py-cheese-maker and outputs it as a PIL Image object.
    Input:
     - type: int; 0 for normal text, 1 for large text and 2 for image
     - size: tuple; size in width/height
    Kwargs:
     - imagepath: str; required if type is 2. path of input image to be resized
     - text: str; required if type is 0 or 1. text to be drawn
     - font: str; optional, defaults to 'arial.ttf'; .ttf input file for text"""
    if type == FrameTypes.FT_IMAGE: # If we're an image...
        if "imagepath" not in kwargs: # ... and we're not given an input...
            raise KeyError("Plain image frame requested but no image path given!")
    if type == FrameTypes.FT_TEXT_LARGE or type == FrameTypes.FT_TEXT_SMALL: # If we're a text frame...
        if "text" not in kwargs:
            raise KeyError("Text frame requested but no image path given!")
    canvas = Image.new('RGB', size, kwargs.get("color", (45, 95, 182, 255)))
    drawer = ImageDraw.Draw(canvas)
    fnt, txt = None, None # shut the fuck up PyCharm
    if type == 0 or type == 1:
        if type == 0:
            fnt = ImageFont.truetype(kwargs.get("font", "arial.ttf"), 32)
            txt = textwrap.wrap(kwargs.get("text"), width=12, subsequent_indent="\n")
        elif type == 1:
            fnt = ImageFont.truetype(kwargs.get("font", "arial.ttf"), 36)
            txt = textwrap.wrap(kwargs.get("text"), width=10, subsequent_indent="\n")
        drawer.multiline_text((size[0]/2, size[1]/2), "".join(txt), anchor="mm", align="center", font=fnt, fill=(255, 255, 255))
        return canvas
    elif type == 2:
        with Image.open(kwargs.get("imagepath")) as img:
            return img.resize(size, resample=Image.BILINEAR)
