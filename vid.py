from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=8JW6qzPCkE8&list=FLuY9KxmfFlx2CLnXP_nd_eA&index=5"
yt = YouTube(video_url, on_progress_callback=loading, on_complete_callback=finished)

# Download The Video

def loading():
    print("Downloading...")
    
def finsihed():
    print("Download Complete")

stream = yt.streams.filter(adaptive=True, mime_type="video/mp4").order_by('resolution').desc()

for i in range(len(stream)):
    print(f"{i+1}. {stream[i].resolution}",
          f"Type: {stream[i].mime_type}",        
          )
    
stream_number = int(input("Enter the number to download: "))
stream = stream[stream_number-1]
stream.download(output_path='downloads/videos', filename=yt.title + ".mp4")
