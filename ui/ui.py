from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    isPlaying = False

    def playStopMusic(self):
        print("Play or stop music here")

        if self.isPlaying:
            self.isPlaying = False
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.playStopButton.setIcon(icon)
        else:
            self.isPlaying = True
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.playStopButton.setIcon(icon)        

    def goToLastMusic(self):
        print("Go to last music")
        self.labelAlbumPic.setPixmap(QtGui.QPixmap(_fromUtf8("PATH TO NEW IMAGE")))

    def goToNextMusic(self):
        print("Go to next music")
        self.labelAlbumPic.setPixmap(QtGui.QPixmap(_fromUtf8("PATH TO NEW IMAGE")))

    def sendYoutubeID(self):
        print("Send Youtube ID")
        print(self.lineEdit.text())
        self.diagramPic.setPixmap(QtGui.QPixmap(_fromUtf8("PATH TO NEW IMAGE")))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1280, 600)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.labelNaviBar = QtGui.QLabel(self.centralwidget)
        self.labelNaviBar.setGeometry(QtCore.QRect(0, 0, 1280, 48))
        self.labelNaviBar.setText(_fromUtf8(""))
        self.labelNaviBar.setPixmap(QtGui.QPixmap(_fromUtf8("images/navibar.png")))
        self.labelNaviBar.setScaledContents(True)
        self.labelNaviBar.setObjectName(_fromUtf8("labelNaviBar"))
        
        self.labelPlayB = QtGui.QLabel(self.centralwidget)
        self.labelPlayB.setGeometry(QtCore.QRect(0, 480, 1280, 120))
        self.labelPlayB.setText(_fromUtf8(""))
        self.labelPlayB.setPixmap(QtGui.QPixmap(_fromUtf8("images/playerbackground.png")))
        self.labelPlayB.setScaledContents(True)
        self.labelPlayB.setObjectName(_fromUtf8("labelPlayB"))
        
        self.labelAlbumPic = QtGui.QLabel(self.centralwidget)
        self.labelAlbumPic.setGeometry(QtCore.QRect(20, 500, 75, 75))
        self.labelAlbumPic.setText(_fromUtf8(""))
        self.labelAlbumPic.setPixmap(QtGui.QPixmap(_fromUtf8("images/albumpic.png")))
        self.labelAlbumPic.setScaledContents(True)
        self.labelAlbumPic.setObjectName(_fromUtf8("labelAlbumPic"))
        
        self.labelHappyEco = QtGui.QLabel(self.centralwidget)
        self.labelHappyEco.setGeometry(QtCore.QRect(620, 350, 90, 90))
        self.labelHappyEco.setText(_fromUtf8(""))
        self.labelHappyEco.setPixmap(QtGui.QPixmap(_fromUtf8("images/happyemo.png")))
        self.labelHappyEco.setScaledContents(True)
        self.labelHappyEco.setObjectName(_fromUtf8("labelHappyEco"))
        
        self.labelSadEco = QtGui.QLabel(self.centralwidget)
        self.labelSadEco.setGeometry(QtCore.QRect(1130, 350, 90, 90))
        self.labelSadEco.setText(_fromUtf8(""))
        self.labelSadEco.setPixmap(QtGui.QPixmap(_fromUtf8("images/angryemo.png")))
        self.labelSadEco.setScaledContents(True)
        self.labelSadEco.setObjectName(_fromUtf8("labelSadEco"))
        
        self.labelEmotionBar = QtGui.QLabel(self.centralwidget)
        self.labelEmotionBar.setGeometry(QtCore.QRect(720, 390, 401, 20))
        self.labelEmotionBar.setText(_fromUtf8(""))
        self.labelEmotionBar.setPixmap(QtGui.QPixmap(_fromUtf8("images/emobar.png")))
        self.labelEmotionBar.setScaledContents(True)
        self.labelEmotionBar.setObjectName(_fromUtf8("labelEmotionBar"))
        
        self.labelPlayBar = QtGui.QLabel(self.centralwidget)
        self.labelPlayBar.setGeometry(QtCore.QRect(590, 540, 482, 3))
        self.labelPlayBar.setText(_fromUtf8(""))
        self.labelPlayBar.setPixmap(QtGui.QPixmap(_fromUtf8("images/playbar.png")))
        self.labelPlayBar.setScaledContents(True)
        self.labelPlayBar.setObjectName(_fromUtf8("labelPlayBar"))
        
        self.labelVolume = QtGui.QLabel(self.centralwidget)
        self.labelVolume.setGeometry(QtCore.QRect(1110, 530, 27, 25))
        self.labelVolume.setText(_fromUtf8(""))
        self.labelVolume.setPixmap(QtGui.QPixmap(_fromUtf8("images/volume.png")))
        self.labelVolume.setScaledContents(True)
        self.labelVolume.setObjectName(_fromUtf8("labelVolume"))
        
        self.labelVolumeBar = QtGui.QLabel(self.centralwidget)
        self.labelVolumeBar.setGeometry(QtCore.QRect(1150, 540, 103, 3))
        self.labelVolumeBar.setText(_fromUtf8(""))
        self.labelVolumeBar.setPixmap(QtGui.QPixmap(_fromUtf8("images/volumebar.png")))
        self.labelVolumeBar.setScaledContents(True)
        self.labelVolumeBar.setObjectName(_fromUtf8("labelVolumeBar"))
        
        self.playStopButton = QtGui.QPushButton(self.centralwidget)
        self.playStopButton.setGeometry(QtCore.QRect(375, 515, 50, 50))
        
        palette = QtGui.QPalette()
        
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        
        self.playStopButton.setPalette(palette)
        self.playStopButton.setAutoFillBackground(False)
        self.playStopButton.setText(_fromUtf8(""))
        self.playStopButton.setStyleSheet("background-color: transparent")
        playIcon = QtGui.QIcon()
        playIcon.addPixmap(QtGui.QPixmap(_fromUtf8("images/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pauseIcon = QtGui.QIcon()
        pauseIcon.addPixmap(QtGui.QPixmap(_fromUtf8("images/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playStopButton.setIcon(playIcon)
        self.playStopButton.setIconSize(QtCore.QSize(50, 50))
        self.playStopButton.setObjectName(_fromUtf8("playStopButton"))
        
        self.lastButton = QtGui.QPushButton(self.centralwidget)
        self.lastButton.setGeometry(QtCore.QRect(280, 530, 34, 20))
        self.lastButton.setText(_fromUtf8(""))
        self.lastButton.setStyleSheet("background-color: transparent")
        lastIcon = QtGui.QIcon()
        lastIcon.addPixmap(QtGui.QPixmap(_fromUtf8("images/last.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastButton.setIcon(lastIcon)
        self.lastButton.setIconSize(QtCore.QSize(34, 20))
        self.lastButton.setObjectName(_fromUtf8("lastButton"))
        
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(480, 530, 34, 20))
        self.nextButton.setText(_fromUtf8(""))
        self.nextButton.setStyleSheet("background-color: transparent")
        nextIcon = QtGui.QIcon()
        nextIcon.addPixmap(QtGui.QPixmap(_fromUtf8("images/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(nextIcon)
        self.nextButton.setIconSize(QtCore.QSize(34, 20))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(770, 280, 401, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        
        self.youtubeLabel = QtGui.QLabel(self.centralwidget)
        self.youtubeLabel.setGeometry(QtCore.QRect(620, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(24)
        font.setItalic(False)
        self.youtubeLabel.setFont(font)
        self.youtubeLabel.setObjectName(_fromUtf8("youtubeLabel"))
        
        self.okButton = QtGui.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(1180, 270, 71, 41))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        
        self.diagramPic = QtGui.QLabel(self.centralwidget)
        self.diagramPic.setGeometry(QtCore.QRect(100, 70, 400, 400))
        self.diagramPic.setText(_fromUtf8(""))
        self.diagramPic.setPixmap(QtGui.QPixmap(_fromUtf8("images/examplePic.png")))
        self.diagramPic.setScaledContents(True)
        self.diagramPic.setObjectName(_fromUtf8("diagramPic"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.playStopButton.clicked.connect(self.playStopMusic)
        self.lastButton.clicked.connect(self.goToLastMusic)
        self.nextButton.clicked.connect(self.goToNextMusic)
        self.okButton.clicked.connect(self.sendYoutubeID)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.youtubeLabel.setText(_translate("MainWindow", "Youtube ID", None))
        self.okButton.setText(_translate("MainWindow", "Submit", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

