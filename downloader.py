from pytube import YouTube
import moviepy.editor as mp
import os
import time

def loading(stream, file_handler, bytes_remaining):
    total = stream.filesize
    bytes_remaining = total - file_handler
    return bytes_remaining

def finished(stream, file_handle):
    print("Download completed.")

def merge_audio_video(video_file, audio_file, output_file):
    video = mp.VideoFileClip(video_file)
    audio = mp.AudioFileClip(audio_file)
    video = video.set_audio(audio)
    video.write_videofile(output_file)
    video.close()
    audio.close()

def get_available_resolutions(video_url):
    try:
        yt = YouTube(video_url)
        streams = yt.streams.filter(mime_type="video/mp4").order_by('resolution').desc()
        return streams
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_thumbnail_url(video_url):
    try:
        yt = YouTube(video_url)
        return yt.thumbnail_url
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def download_video(video_url, stream):
    retries = 3
    for _ in range(retries):
        try:
            yt = YouTube(video_url, on_progress_callback=loading, on_complete_callback=finished)
            video_file = stream.download(output_path='downloads/videos', filename=yt.title + "temp.mp4")
            audio_file = yt.streams.get_audio_only().download(output_path='downloads', filename=yt.title + ".mp3")

            merge_audio_video(video_file, audio_file, f"downloads/videos/{yt.title}.mp4")

            os.remove(video_file)
            os.remove(audio_file)

            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(2)  # Wait for 2 seconds before retrying
    return False
