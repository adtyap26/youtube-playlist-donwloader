# YouTube Playlist Downloader

This script allows you to download a YouTube playlist in MP3 or MP4 format using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Requirements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) must be installed on your system.

## Usage

for download mp3 add keyword audio at the end of arguments.
```shell
./youtube-dl-playlist.py <youtube_playlist_url> <destination_directory> <audio> 

```



## Examples

To download a YouTube playlist with the URL `https://www.youtube.com/playlist?list=PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-` to the `~/Music/Download/Playlist` directory, run the following command:

```shell
./youtube-dl-playlist.py https://www.youtube.com/playlist?list=<youtube_playlist_id> ~/Music/Download/Playlist audio


```

Replace `<youtube_playlist_id>` with the ID of the playlist you want to download. This will download all the videos in the playlist to the specified directory in MP3 format.
I hope this helps! Let me know if you have any questions.



You can save this code as a `youtube-dl-playlist.py` file and make it executable by running the following command:

chmod +x youtube-dl-playlist.py


You can then run the script as follows:

./youtube-dl-playlist.py <youtube_playlist_url> <destination_directory>
