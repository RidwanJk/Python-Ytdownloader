# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Youtube_Downloader.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(761, 597)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.YoutubeTab = QWidget()
        self.YoutubeTab.setObjectName(u"YoutubeTab")
        self.verticalLayout_2 = QVBoxLayout(self.YoutubeTab)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.YoutubeTab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.YoutubeTab)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.searchButton = QPushButton(self.YoutubeTab)
        self.searchButton.setObjectName(u"searchButton")

        self.verticalLayout_2.addWidget(self.searchButton)

        self.label_3 = QLabel(self.YoutubeTab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.comboBox = QComboBox(self.YoutubeTab)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.label = QLabel(self.YoutubeTab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_image = QLabel(self.YoutubeTab)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setMinimumSize(QSize(0, 200))
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_image)

        self.label_4 = QLabel(self.YoutubeTab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.YoutubeTab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.pushButton = QPushButton(self.YoutubeTab)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.tabWidget.addTab(self.YoutubeTab, "")
        self.PlaylistTab = QWidget()
        self.PlaylistTab.setObjectName(u"PlaylistTab")
        self.verticalLayout_3 = QVBoxLayout(self.PlaylistTab)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.PlaylistURLlabel = QLabel(self.PlaylistTab)
        self.PlaylistURLlabel.setObjectName(u"PlaylistURLlabel")

        self.verticalLayout_3.addWidget(self.PlaylistURLlabel)

        self.PlaylistURL = QLineEdit(self.PlaylistTab)
        self.PlaylistURL.setObjectName(u"PlaylistURL")

        self.verticalLayout_3.addWidget(self.PlaylistURL)

        self.searchButton_2 = QPushButton(self.PlaylistTab)
        self.searchButton_2.setObjectName(u"searchButton_2")

        self.verticalLayout_3.addWidget(self.searchButton_2)

        self.label_7 = QLabel(self.PlaylistTab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.comboBox_2 = QComboBox(self.PlaylistTab)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_3.addWidget(self.comboBox_2)

        self.label_8 = QLabel(self.PlaylistTab)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_image_2 = QLabel(self.PlaylistTab)
        self.label_image_2.setObjectName(u"label_image_2")
        self.label_image_2.setMinimumSize(QSize(0, 200))
        self.label_image_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_image_2)

        self.label_6 = QLabel(self.PlaylistTab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.progressBar_2 = QProgressBar(self.PlaylistTab)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar_2)

        self.pushButton_2 = QPushButton(self.PlaylistTab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.tabWidget.addTab(self.PlaylistTab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"YouTube Downloader", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Video URL", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"https://www.youtube.com/watch?v=...", None))
        self.searchButton.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Resolution", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"-- Search a video first --", None))

        self.label.setText(QCoreApplication.translate("Form", u"Preview", None))
        self.label_image.setText(QCoreApplication.translate("Form", u"No preview", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Progress", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.YoutubeTab), QCoreApplication.translate("Form", u"YouTube Downloader", None))
        self.PlaylistURLlabel.setText(QCoreApplication.translate("Form", u"Playlist URL", None))
        self.PlaylistURL.setPlaceholderText(QCoreApplication.translate("Form", u"https://www.youtube.com/playlist?list=...", None))
        self.searchButton_2.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Resolution", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"-- Search a playlist first --", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"Preview", None))
        self.label_image_2.setText(QCoreApplication.translate("Form", u"No preview", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Progress", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PlaylistTab), QCoreApplication.translate("Form", u"Playlist Downloader", None))
    # retranslateUi

