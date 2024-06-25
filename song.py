from pytube import YouTube


video_url = ""
yt = YouTube(video_url)

# Download The Song

stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
stream.download(output_path='downloads/music', filename=yt.title + ".mp3")


