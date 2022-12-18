# YouTube video downloader

## Steps:

1. Define the download parameters using [data.json](./data.json).
1. Run [download_youtube_video.exe](./download_youtube_video.exe) to download YouTube videos/playlists.

## Parameters in [data.json](./data.json)

- `yt_videos`: List of YouTube videos to be downloaded
  - Format: https://<span>www</span>.youtube.com/watch?v=_&lt;video_id&gt;_&list=_&lt;playlist_id&gt;_
    - Mandatory input: _&lt;video_id&gt;_
    - Optional input: _&lt;playlist_id&gt;_
  - Examples:
    - https://www.youtube.com/watch?v=_k-F-MMvQV4
    - https://www.youtube.com/watch?v=DC471a9qrU4&list=PL0vfts4VzfNiI1BsIK5u7LpPaIDKMJIDN
- `yt_playlists`: List of YouTube playlists to be downloaded
  - Format: https://<span>www</span>.youtube.com/playlist?list=_&lt;playlist_id&gt;_&limit=_&lt;video_download_limit&gt;_ `OR` https://<span>www</span>.youtube.com/watch?v=_&lt;video_id&gt;_&list=_&lt;playlist_id&gt;_&limit=_&lt;video_download_limit&gt;_
    - Mandatory input: _&lt;playlist_id&gt;_
    - Optional input: _&lt;video_download_limit&gt;_
  - Examples:
    - https://www.youtube.com/playlist?list=PL0vfts4VzfNiI1BsIK5u7LpPaIDKMJIDN
    - https://www.youtube.com/watch?v=DC471a9qrU4&list=PL0vfts4VzfNiI1BsIK5u7LpPaIDKMJIDN&limit=10
- `download_location`: Absolute/Relative path to your preferred download directory
  - Use `/` instead of `\` in the path
  - Example: ./youtube-downloads
- `download_file_format`: File format of your downloaded file
  - mp3
  - mp4
- `archive`: List of YouTube videos & playlists that have been downloaded and are being kept as historical data
