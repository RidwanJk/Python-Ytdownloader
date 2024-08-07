Certainly! Here's the `README.md` content formatted for a typical markdown file:

---

# YouTube Downloader

This application allows you to download YouTube videos by providing the video URL and selecting the desired resolution.

## Features

- **Input:** Enter a YouTube video URL.
- **Resolution Selection:** Fetch available resolutions for the video.
- **Preview:** Display a thumbnail preview of the video.
- **Download:** Download the selected video resolution.
- **Progress Bar:** Shows download progress.

## Requirements

- Python 3.x
- PySide6
- pytube
- moviepy

## Installation

### Clone the repository

```bash
git clone https://github.com/your/repository.git
cd repository
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application by executing `main.py`.

```bash
python main.py
```

### How to Use

1. Enter a valid YouTube video URL.
2. Click on **Search** to fetch available resolutions.
3. Select a resolution from the dropdown.
4. Click on **Download** to start the download.
5. Monitor download progress with the progress bar.
6. Once the download completes, a success message will appear.

## Project Structure

- `main.py`: Contains the main application logic and GUI setup using PySide6.
- `downloader.py`: Handles video downloading using pytube for video fetching and moviepy for merging audio and video streams.
- `Youtube_Downloader_ui.py`: UI file generated from Qt Designer, defining the application's layout.
- `Youtube_Downloader.ui`: Original UI file in Qt Designer format.

## Notes

- Ensure a stable internet connection for video fetching and downloading.
- Thumbnail previews are fetched directly from YouTube.
- Video merging (audio + video) is done locally after download.

## Things to add

- adding playlist downloader
- adding music downloader