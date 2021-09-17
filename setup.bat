@echo off
setlocal
python --version >nul 2>&1 && (
    echo Python exists...
) || (
    echo Python is not installed or configured correctly. You can download Python here: https://www.python.org/downloads
    echo If you HAVE installed Python and this still shows up, you may have forgotten to check the 'Add to PATH' option.
    pause
    exit
)

ffmpeg -version >nul 2>&1 && (
    echo FFmpeg exists...
) || (
    echo FFmpeg is not installed or configured correctly. You can get pre-built Windows binaries here: https://ffmpeg.org/download.html
    pause
    exit
)
echo Installing Python dependencies...
rem MS is an asshole. 'python3' opens the Store. Yuck!
python -m pip install -r req.txt
endlocal
pause