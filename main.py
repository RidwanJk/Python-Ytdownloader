from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal, Qt
from Youtube_Downloader_ui import Ui_Form
import downloader
import requests


class MergeWorker(QThread):
    finished = Signal(bool)
    progress = Signal(int)

    def __init__(self, video_url, stream):
        super().__init__()
        self.video_url = video_url
        self.stream = stream

    def run(self):
        success = downloader.download_video(
            self.video_url,
            self.stream,
            progress_callback=self.progress.emit
        )
        self.finished.emit(success)


class PlaylistWorker(QThread):
    finished = Signal(bool)
    progress = Signal(int)

    def __init__(self, playlist_url, stream_resolution):
        super().__init__()
        self.playlist_url = playlist_url
        self.stream_resolution = stream_resolution

    def run(self):
        success = downloader.download_playlist(
            self.playlist_url,
            self.stream_resolution,
            progress_callback=self.progress.emit
        )
        self.finished.emit(success)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.central_widget)
        self.setCentralWidget(self.central_widget)
        self.resize(761, 597)

        # --- YouTube Tab ---
        self.ui.pushButton.clicked.connect(self.download_video)
        self.ui.searchButton.clicked.connect(self.update_resolutions)

        # --- Playlist Tab ---
        self.ui.pushButton_2.clicked.connect(self.download_playlist)
        self.ui.searchButton_2.clicked.connect(self.update_playlist_resolutions)

    # ── YouTube Tab ────────────────────────────────────────────

    def update_resolutions(self):
        video_url = self.ui.lineEdit.text()
        if not video_url:
            QMessageBox.warning(self, "Input Error", "Please enter a valid YouTube video URL.")
            return
        streams = downloader.get_available_resolutions(video_url)
        if streams:
            self.ui.comboBox.clear()
            for stream in streams:
                filesize_mb = round(stream.filesize / 1024 / 1024, 1) if stream.filesize else "?"
                self.ui.comboBox.addItem(
                    f"{stream.resolution} | {stream.mime_type} | {stream.fps}fps | {filesize_mb}MB",
                    stream
                )
            thumbnail_url = downloader.get_thumbnail_url(video_url)
            self.preview_thumbnail(thumbnail_url, self.ui.label_image)
        else:
            QMessageBox.critical(self, "Error", "An error occurred while fetching resolutions. Please check the URL and try again.")

    def preview_thumbnail(self, thumbnail_url, label):
        if thumbnail_url:
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                container_size = label.size()
                pixmap = pixmap.scaled(container_size, Qt.AspectRatioMode.KeepAspectRatio)
                label.setPixmap(pixmap)
            else:
                QMessageBox.warning(self, "Thumbnail Error", "Unable to load thumbnail.")

    def download_video(self):
        video_url = self.ui.lineEdit.text()
        if not video_url:
            QMessageBox.warning(self, "Input Error", "Please enter a valid YouTube video URL.")
            return

        selected_index = self.ui.comboBox.currentIndex()
        if selected_index == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a resolution to download.")
            return

        self.ui.progressBar.setValue(0)  # Reset progress bar

        stream = self.ui.comboBox.itemData(selected_index)
        self.worker = MergeWorker(video_url, stream)
        self.worker.finished.connect(self.on_download_finished)
        self.worker.progress.connect(self.ui.progressBar.setValue)
        self.worker.start()

    def on_download_finished(self, success):
        if success:
            QMessageBox.information(self, "Success", "The video has been downloaded successfully!")
        else:
            QMessageBox.critical(self, "Error", "An error occurred during the download. Please check the URL and try again.")

    # ── Playlist Tab ───────────────────────────────────────────

    def update_playlist_resolutions(self):
        playlist_url = self.ui.PlaylistURL.text()
        if not playlist_url:
            QMessageBox.warning(self, "Input Error", "Please enter a valid YouTube playlist URL.")
            return
        streams = downloader.get_available_resolutions(playlist_url)
        if streams:
            self.ui.comboBox_2.clear()
            for stream in streams:
                filesize_mb = round(stream.filesize / 1024 / 1024, 1) if stream.filesize else "?"
                self.ui.comboBox_2.addItem(
                    f"{stream.resolution} | {stream.mime_type} | {stream.fps}fps | {filesize_mb}MB",
                    stream
                )
            thumbnail_url = downloader.get_playlist_thumbnail_url(playlist_url)
            self.preview_thumbnail(thumbnail_url, self.ui.label_image_2)
        else:
            QMessageBox.critical(self, "Error", "An error occurred while fetching resolutions. Please check the URL and try again.")

    def download_playlist(self):
        playlist_url = self.ui.PlaylistURL.text()
        if not playlist_url:
            QMessageBox.warning(self, "Input Error", "Please enter a valid YouTube playlist URL.")
            return

        selected_index = self.ui.comboBox_2.currentIndex()
        if selected_index == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a resolution to download.")
            return

        self.ui.progressBar_2.setValue(0)  # Reset progress bar

        stream = self.ui.comboBox_2.itemData(selected_index)
        self.playlist_worker = PlaylistWorker(playlist_url, stream.resolution)
        self.playlist_worker.finished.connect(self.on_playlist_finished)
        self.playlist_worker.progress.connect(self.ui.progressBar_2.setValue)
        self.playlist_worker.start()

    def on_playlist_finished(self, success):
        if success:
            QMessageBox.information(self, "Success", "The playlist has been downloaded successfully!")
        else:
            QMessageBox.critical(self, "Error", "An error occurred during the playlist download.")


if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec()
