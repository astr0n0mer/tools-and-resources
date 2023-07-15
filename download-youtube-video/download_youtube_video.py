import json, os
from pytube import YouTube, Playlist

def createDownloadLocation(downloadLocation):
    if not(os.path.exists(downloadLocation)):
        os.makedirs(downloadLocation)

def checkVideoExists(downloadLocation, videoTitle, downloadFileFormat):
    return os.path.exists(downloadLocation + '/' + videoTitle + '.' + downloadFileFormat)

def toValidFilename(invalidFilename):
    invalidChars = r'\/:*?"<>|'
    validFilename = []
    for c in invalidFilename:
        if(c not in invalidChars):
            validFilename.append(c)
    return ''.join(validFilename)

def downloadVideo(downloadLocation, downloadFileFormat, videoObj, playlistObj = None):
    isDownloadSuccessful = True
    videoObj.title = toValidFilename(videoObj.title)
    if (checkVideoExists(downloadLocation, videoObj.title, downloadFileFormat)):
        print("File already exists: " + videoObj.title)
    else:
        try:
            print(f"Downloading {videoObj.title}")
            if(downloadFileFormat == "mp3"):
                # mp4AudioFile = videoObj.streams.filter(only_audio = True).first().download(downloadLocation)
                mp4AudioFile = videoObj.streams.get_audio_only().download(downloadLocation)
                # os.rename(mp4AudioFile, os.path.splitext(mp4AudioFile)[0] + ".mp3")
                os.replace(mp4AudioFile, os.path.splitext(mp4AudioFile)[0] + ".mp3")
            elif(downloadFileFormat == "mp4"):
                mp4VideoFile = videoObj.streams.get_highest_resolution().download(downloadLocation)
            
            if(playlistObj is None):
                downloadSuccessfulMsg(videoObj.title)
            else:
                downloadSuccessfulMsg(videoObj.title, playlistObj.title)
        except Exception as e:
            print(e)
            isDownloadSuccessful = False
    return isDownloadSuccessful

def updateArchive(URL, URLType = "video"):
    if(URLType == "video"):
        videos.remove(URL)
        archiveVideos.append(URL)
    elif(URLType == "playlist"):
        playlists.remove(URL)
        archivePlaylists.append(URL)

def downloadSuccessfulMsg(videoTitle, playlistTitle = ""):
    if(playlistTitle == ""):
        print("Successfully downloaded: " + videoTitle)
    else:
        print("Successfully downloaded: " + videoTitle + " from playlist: " + playlistTitle)

# -------------------- main --------------------
with open("./data.json", "r") as jsonFile:
    jsonData = json.load(jsonFile);

videos = jsonData["pending_downloads"]["yt_videos"]
playlists = jsonData["pending_downloads"]["yt_playlists"]
location = jsonData["download_location"]
fileFormat = jsonData["download_file_format"]
archiveVideos = jsonData["archive"]["yt_videos"]
archivePlaylists = jsonData["archive"]["yt_playlists"]

# Download all pending videos
if(len(videos) > 0):
    createDownloadLocation(location)
    for videoURL in videos:
        videoObj = YouTube(videoURL)
        isVideoDownloaded = downloadVideo(location, fileFormat, videoObj)
        if(isVideoDownloaded):
            updateArchive(videoURL, "video")

# Download all pending playlists
if(len(playlists) > 0):
    createDownloadLocation(location)
    for playlistURL in playlists:
        try:
            videoDownloadLimit = int(playlistURL.split("&limit=")[1].split("&")[0])
        except IndexError as ie:
            videoDownloadLimit = 2**31 - 1 # Maximum int value for int32 variable
        playlistObj = Playlist(playlistURL)
        isPlaylistDownloaded = True
        numberOfVideosDownloaded = 0
        for videoObj in playlistObj.videos:
            if(numberOfVideosDownloaded >= videoDownloadLimit):
                break
            isPlaylistDownloaded = isPlaylistDownloaded and downloadVideo(location, fileFormat, videoObj, playlistObj)
            numberOfVideosDownloaded += 1
        if(isPlaylistDownloaded):
            updateArchive(playlistURL, "playlist")

# Remove downloaded videos/playlists from pending lists and update the archive
jsonData["pending_downloads"]["yt_videos"] = videos
jsonData["pending_downloads"]["yt_playlists"] = playlists
archiveVideos = list(set(archiveVideos))
archiveVideos.sort()
archivePlaylists = list(set(archivePlaylists))
archivePlaylists.sort()
jsonData["archive"]["yt_videos"] = archiveVideos
jsonData["archive"]["yt_playlists"] = archivePlaylists

if(jsonData["auto_update_archive"]):
    with open("./data.json", 'w') as jsonFile:
        json.dump(jsonData, jsonFile, indent = 4)

os.system("pause")
