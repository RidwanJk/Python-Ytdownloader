from pytube import YouTube

# URL of the YouTube video
video_url = 'https://www.youtube.com/watch?v=TfY-YTkqKb8'

# Create a YouTube object
yt = YouTube(video_url)
        # on_progress_callback=progress_func,
        # on_complete_callback=complete_func,
        # proxies=my_proxies,
        # use_oauth=False,
        # allow_oauth_cache=True

print(yt.title)

print(yt.thumbnail_url)

print(yt.streams.filter(adaptive
                        =True))