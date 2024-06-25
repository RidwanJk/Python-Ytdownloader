from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLabel, QFrame
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtCore import QThread, Signal, QSize
from Youtube_Downloader_ui import Ui_Form
import downloader
import requests

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.central_widget)
        self.setCentralWidget(self.central_widget)
        
        # Set the initial size of the main window
        self.resize(700, 500)

        # Connect signals and slots
        self.ui.pushButton.clicked.connect(self.download_video)
        self.ui.searchButton.clicked.connect(self.update_resolutions)               

    def update_resolutions(self):
        video_url = self.ui.lineEdit.text()
        if not video_url:
            QMessageBox.warning(self, "Input Error", "Please enter a valid YouTube video URL.")
            return        
        streams = downloader.get_available_resolutions(video_url)        
        if streams:
            self.ui.comboBox.clear()
            for stream in streams:
                self.ui.comboBox.addItem(f"{stream.resolution} ({stream.mime_type})", stream) 
            thumbnail_url = downloader.get_thumbnail_url(video_url)
            self.preview_thumbnail(thumbnail_url)
        else:
            QMessageBox.critical(self, "Error", "An error occurred while fetching resolutions. Please check the URL and try again.")

    def preview_thumbnail(self, thumbnail_url):
        if thumbnail_url:
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)                    
                container_size = self.ui.label_image.size()
                pixmap = pixmap.scaled(container_size, Qt.AspectRatioMode.KeepAspectRatio)            
                self.ui.label_image.setPixmap(pixmap)
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
        
        stream = self.ui.comboBox.itemData(selected_index)
        
        self.worker = MergeWorker(video_url, stream)
        self.worker.progress.connect(self.show_message)
        self.worker.finished.connect(self.on_download_finished)
        self.worker.start()

    def show_message(self, message):
        QMessageBox.information(self, "Information", message)

    def on_download_finished(self, success):
        if success:
            QMessageBox.information(self, "Success", "The video has been downloaded successfully!")
        else:
            QMessageBox.critical(self, "Error", "An error occurred during the download. Please check the URL and try again.")

class MergeWorker(QThread):
    progress = Signal(str)
    finished = Signal(bool)

    def __init__(self, video_url, stream):
        super().__init__()
        self.video_url = video_url
        self.stream = stream

    def run(self):
        # Perform the merging process here
        success = downloader.download_video(self.video_url, self.stream)
        if success:
            self.progress.emit("The video has been downloaded successfully!")
            self.finished.emit(True)
        else:
            self.progress.emit("An error occurred during the download. Please check the URL and try again.")
            self.finished.emit(False)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec()
