#!/usr/bin/env bash

if ! command -v python --version &> /dev/null
then
    echo "Python is not installed or configured correctly. You can download Python here: https://www.python.org/downloads"
    echo "If you HAVE installed Python and this still shows up, you may have forgotten to check the 'Add to PATH' option."
    read -n1 -r
    exit
else
    echo "Python exists..."
fi

if ! command -v ffmpeg -version &> /dev/null
then
    echo "FFmpeg is not installed or configured correctly. You can get pre-built Windows binaries here: https://ffmpeg.org/download.html"
    read -n1 -r
    exit
else
    echo "Python exists..."
fi
echo "Installing Python dependencies..."
python3 -m pip install -r req.txt
read -n1 -r -p "Press any key to continue..."