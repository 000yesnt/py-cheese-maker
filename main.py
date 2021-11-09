#!/usr/bin/env python3
from shutil import which
import argparse
from glob import glob
import os
from subprocess import run as cmd

from CheeseFactory import makeCheeseFrame
from CheeseFactory import FrameTypes as ft
import coolstuff

psr = argparse.ArgumentParser(prog="'Top X Cheese' maker",
                              description="This script generates those funny 'top 50000 cheese' memes that are all over Discord now from input files.")

psr.add_argument('--path', help="path to use as input", type=str, default="in/")
psr.add_argument('--font', help="font file (.ttf) to use", type=str, default="arial.ttf")
psr.add_argument('-s', help="string to use at the start, supports formatting ({ln} = amount of files in input)",
                 type=str, default="top {ln} images")
psr.add_argument('-r', help="framerate of output video, default 1", type=int, default=1)
psr.add_argument('-o', help="name of output mp4", type=str, default="result")
psr.add_argument('--width', help="width of video, default 256", type=int, default=256)
psr.add_argument('--height', help="height of video, default 256", type=int, default=256)

args = psr.parse_args()
if not os.path.exists(args.path):
    coolstuff.Msg(coolstuff.levels.ERROR, "Path does not exist")
    exit(1)

if which("ffmpeg") is None:
    coolstuff.Msg(coolstuff.levels.ERROR, "FFmpeg is not installed or configured correctly!\nYou can get binaries here: https://ffmpeg.org/download.html")
    exit(1)

imlist = glob(f"{args.path}/*.png") + glob(f"{args.path}/*.jpg") + glob(f"{args.path}/*.jfif") + glob(f"{args.path}/*.jpeg")
u = len(imlist)
if u == 0:
    coolstuff.Msg(coolstuff.levels.ERROR, "Input path is empty!")
    exit(1)

FrameOrder = [
    makeCheeseFrame(ft.FT_TEXT_LARGE, (args.width, args.height), text=str(args.s).format(ln=len(imlist)), font=args.font),
    makeCheeseFrame(ft.FT_TEXT_LARGE, (args.width, args.height), text=f"number {u}", font=args.font)
]

coolstuff.MakeAnimatedMsgThread("Making frames", 0.3)
for f in imlist:
    FrameOrder.append(makeCheeseFrame(ft.FT_IMAGE, (args.width, args.height), imagepath=f))
    u -= 1
    if u == 0:
        makeCheeseFrame(1, (args.width, args.height), text=f"thanks for watching", font=args.font)
        break
    FrameOrder.append(makeCheeseFrame(ft.FT_TEXT_SMALL, (args.width, args.height), text=f"number {u}", font=args.font))

coolstuff.MakeAnimatedMsgThread("Writing frames", 0.3)
imindex = 0
for img in FrameOrder:
    img.save(f"out/imindex{imindex}.png")
    imindex += 1

coolstuff.MakeAnimatedMsgThread("Processing...", 0.3)
cmd(["ffmpeg", "-hide_banner", "-framerate", str(args.r), "-y", "-i", "out/imindex%d.png", "-c", "libx264", f"out/{args.o}.mp4"], capture_output=True)
coolstuff.KillAnimatedMsgThread(coolstuff.levels.BLANK, "Cleaning up")

tg = glob(f"out/*.png")
for g in tg:
    os.remove(g)

print("Done")