#!/usr/bin/env python3
import shutil
import argparse
import glob
import os
import subprocess

import CheeseFactory

psr = argparse.ArgumentParser(prog="'Top X Cheese' maker",
                              description="This script generates those funny 'top 50000 cheese' memes that are all over Discord now from input files.")

psr.add_argument('--path', help="path to use as input", type=str, default="in/")
psr.add_argument('-s', help="string to use at the start, supports formatting ({ln} = amount of files in input)",
                 type=str, default="top {ln} images")
psr.add_argument('-r', help="framerate of output video, default 1", type=int, default=1)
psr.add_argument('-o', help="name of output mp4", type=str, default="result")
psr.add_argument('-w', help="width of video, default 256", type=int, default=256)
psr.add_argument('-h', help="height of video, default 256", type=int, default=256)

args = psr.parse_args()
if not os.path.exists(args.path):
    raise Exception("Path does not exist")

if shutil.which("ffmpeg") is None:
    raise Exception("You forgot ffmpeg")

imlist = glob.glob(f"{args.path}/*.png") + glob.glob(f"{args.path}/*.jpg") + glob.glob(f"{args.path}/*.jfif") + glob.glob(f"{args.path}/*.jpeg")
u = len(imlist)
if u == 0:
    raise Exception("Input path empty")

FrameOrder = [
    CheeseFactory.MakeCheeseFrame(1, (args.w, args.h), text=str(args.s).format(ln=len(imlist))),
    CheeseFactory.MakeCheeseFrame(1, (args.w, args.h), text=f"number {u}")
]

print("Making frames")
for f in imlist:
    FrameOrder.append(CheeseFactory.MakeCheeseFrame(2, (args.w, args.h), imagepath=f))
    u -= 1
    if u == 0:
        CheeseFactory.MakeCheeseFrame(1, (args.w, args.h), text=f"thanks for watching")
        break
    FrameOrder.append(CheeseFactory.MakeCheeseFrame(0, (args.w, args.h), text=f"number {u}"))

print("Writing frames")
imindex = 0
for img in FrameOrder:
    img.save(f"out/imindex{imindex}.png")
    imindex += 1

print("Processing with ffmpeg")
subprocess.run(["ffmpeg", "-hide_banner", "-framerate", str(args.r), "-y", "-i", "out/imindex%d.png", "-c", "libx264", f"out/{args.o}.mp4"], capture_output=True)
print("Cleaning up")

tg = glob.glob(f"out/*.png")
for g in tg:
    os.remove(g)

print("Done")