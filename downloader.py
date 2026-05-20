from pytubefix import YouTube
import subprocess
import os
import re
import time
import pytubefix.request

pytubefix.request.default_range_size = 2048000  # 2MB chunk size


def sanitize_filename(title):
    # Remove invalid Windows filename characters
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    # Remove non-ASCII characters (fixes charmap encoding error)
    title = title.encode('ascii', 'ignore').decode('ascii')
    title = title.strip()
    return title or "video"  # fallback if title becomes empty


def finished(stream, file_handle):
    print("Download completed.")


def merge_audio_video(video_file, audio_file, output_file):
    subprocess.run([
        "ffmpeg",
        "-i", video_file,  # video stream
        "-i", audio_file,  # audio stream
        "-c:v", "copy",    # copy video as-is (no re-encoding)
        "-c:a", "copy",    # copy audio as-is (no re-encoding)
        output_file,
        "-y"               # overwrite if exists
    ], check=True)


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
            def on_progress(vid, chunk, bytes_remaining):
                total_size = vid.filesize
                bytes_downloaded = total_size - bytes_remaining
                percentage = round(bytes_downloaded / total_size * 100, 2)
                total_mb = round(total_size / 1024 / 1024, 1)
                downloaded_mb = round(bytes_downloaded / 1024 / 1024, 1)
                remaining_mb = round(bytes_remaining / 1024 / 1024, 1)
                print(f'Progress: {percentage}% | Total: {total_mb}MB | Downloaded: {downloaded_mb}MB | Remaining: {remaining_mb}MB')

            yt = YouTube(video_url, on_progress_callback=on_progress, on_complete_callback=finished)

            # Sanitize title to avoid encoding errors
            title = sanitize_filename(yt.title)

            # Create dirs if not exist
            os.makedirs('downloads/videos', exist_ok=True)
            os.makedirs('downloads/temp', exist_ok=True)

            print("Downloading video...")
            video_file = stream.download(output_path='downloads/temp', filename=title + "_video.mp4")

            print("Downloading audio...")
            audio_file = yt.streams.get_audio_only().download(output_path='downloads/temp', filename=title + "_audio.mp4")

            print("Merging...")
            output_path = f"downloads/videos/{title}.mp4"
            merge_audio_video(video_file, audio_file, output_path)

            # Cleanup temp files
            os.remove(video_file)
            os.remove(audio_file)

            print(f"Done! Saved to: {output_path}")
            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(2)

    return False


def get_playlist_thumbnail_url(playlist_url):
    try:
        from pytubefix import Playlist
        pl = Playlist(playlist_url)
        # Get thumbnail of the first video
        first_video = YouTube(pl.video_urls[0])
        return first_video.thumbnail_url
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


def download_playlist(playlist_url, resolution, progress_callback=None):
    try:
        from pytubefix import Playlist
        pl = Playlist(playlist_url)
        total = len(pl.video_urls)
        print(f"Playlist: {pl.title} | {total} videos")

        for i, url in enumerate(pl.video_urls):
            print(f"Downloading video {i+1}/{total}: {url}")
            yt = YouTube(url)
            stream = yt.streams.filter(
                mime_type="video/mp4",
                only_video=True,
                resolution=resolution
            ).first()

            # Fallback to best available if resolution not found
            if not stream:
                stream = yt.streams.filter(
                    mime_type="video/mp4",
                    only_video=True
                ).order_by('resolution').desc().first()

            if stream:
                download_video(url, stream)

            # Update progress based on number of videos done
            if progress_callback:
                progress_callback(int((i + 1) / total * 100))

        return True
    except Exception as e:
        print(f"Playlist download error: {e}")
        return False
