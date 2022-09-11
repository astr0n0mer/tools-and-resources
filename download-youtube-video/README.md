# YouTube Video Downloader

## Steps:

1. Define the download parameters using [data.json](./data.json).
1. Run [download_youtube_video.exe](./download_youtube_video.exe) to download a YouTube video/playlist.

## Potential values for [data.json](./data.json)

| Parameter            | Potential value                                                                                                                                                                   | Notes                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| yt_videos            | https://<span></span>www.youtube.com/watch?v=_&lt;video\_id&gt;_ <br/> https://<span></span>www.youtube.com/watch?v=_&lt;video\_id&gt;_&list=_&lt;playlist\_id&gt;_               | List of YouTube videos to be downloaded.                                                                          |
| yt_playlists         | https://<span></span>www.youtube.com/playlist?list=_&lt;playlist\_id&gt;_ <br/> https://<span></span>www.youtube.com/watch?v=_&lt;video\_id&gt;_&list=_&lt;playlist\_id&gt;_      | List of YouTube playlists to be downloaded.                                                                       |
| download_location    | ./youtube-downloads                                                                                                                                                               | Absolute/Relative path to your preferred download directory. <br/> Please prefer '/' instead of '\\' in the path. |
| download_file_format | mp3 _or_ mp4                                                                                                                                                                      | File format of your downloaded file.                                                                              |
| archive              | _Read Only_                                                                                                                                                                       | List of YouTube videos & playlists that have been downloaded and are being kept as historical data.               |
