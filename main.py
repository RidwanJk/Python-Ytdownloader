from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from Youtube_Downloader_ui import Ui_Form
import downloader

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
        
        self.ui.searchButton.pressed.connect(self.update_resolutions)               

    def update_resolutions(self):
        video_url = self.ui.lineEdit.text()
        if not video_url:
            QMessageBox.warning(self, "Input Error", "Please enter a valid YouTube video URL.")
            return        
        streams = downloader.get_available_resolutions(video_url)
        if streams:
            self.comboBox.clear()
            for stream in streams:
                self.comboBox.addItem(f"{stream.resolution} ({stream.mime_type})", stream)
        else:
            QMessageBox.critical(self, "Error", "An error occurred while fetching resolutions. Please check the URL and try again.")

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
        success = downloader.download_video(video_url, stream)
        if success:
            QMessageBox.information(self, "Success", "The video has been downloaded successfully!")
        else:
            QMessageBox.critical(self, "Error", "An error occurred during the download. Please check the URL and try again.")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec()
