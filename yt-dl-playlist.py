#!/usr/bin/env python

import os
import sys
import subprocess

# check if yt-dlp is installed
if not os.path.exists("/usr/bin/yt-dlp"):
    print("Error: yt-dlp is not installed. Please install yt-dlp first.")
    sys.exit(1)

# parse command line arguments
if len(sys.argv) < 3:
    print("Usage: youtube-dl-playlist <youtube_playlist_url> <destination_directory> [audio]")
    sys.exit(1)

youtube_playlist_url = sys.argv[1]
destination_directory = sys.argv[2]

# make sure the destination directory exists
if not os.path.exists(destination_directory):
    print("Error: destination directory does not exist.")
    sys.exit(1)

# download youtube playlist using yt-dlp
if len(sys.argv) == 4 and sys.argv[3] == "audio":
    command = [
        "yt-dlp",
        "--ignore-errors",
        "--format",
        "bestaudio",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "--audio-quality",
        "160K",
        "--output",
        '"%(title)s.%(ext)s"',
        "--yes-playlist",
        youtube_playlist_url,
    ]
else:
    command = [
        "yt-dlp",
        "-f",
        "'bv*[height<=720][ext=mp4]+ba[ext=m4a]'",
        "--merge-output-format",
        "mp4",
        "--output",
        '"%(title)s.%(ext)s"',
        "--yes-playlist",
        youtube_playlist_url,
    ]

subprocess.run(" ".join(command), shell=True)

