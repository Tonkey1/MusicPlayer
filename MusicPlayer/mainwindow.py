import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QFileDialog, QAction, qApp, QTreeWidgetItem, QDialog
from PyQt5.QtGui import QIcon
from ui import ui_window
from ui import add
# import pygame
import Wave_play
import time
from test import Test
import threading 

class MainWindow(ui_window.Ui_MainWindow, QMainWindow):
    def __init__(self, port):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pop = PopWindow()

        self.play = False
        self.music = 0
        self.song = 0
        self.progerss = 0
        self.songs = []

        self.duration = 0
        self.t = TimeControl(self.duration, self.updateProgressBar)
        self.musicSlider.setMinimum(0)
        self.musicSlider.setMaximum(1000)


        self.initButton()
        # self.list_view.hide()

        self.data = Test(port)

        self.view_controller = [self.album_view, self.list_view, self.fav_view, self.song_view]
        self.tab_controller = [self.btnMusic, self.btnFavorite]
        self.btnAlbum.hide()

        self.tab_highlight_style = "QPushButton {font: Bold 15pt \"Arial\";color: rgb(250, 220, 62);text-decoration: underline;background-color: rgba(255, 255, 255, 0);}"
        self.tab_default_style = "QPushButton {font: Bold 15pt \"Arial\";color: rgb(255, 255, 255);background-color: rgba(255, 255, 255, 0);}"

        self.showView(self.list_view)
        self.highlightTab(self.btnMusic)
        self.initWindow()


    def initButton(self):
        self.btnSearch.clicked.connect(self.searchButton_callback) 

        # self.btnAlbum.clicked.connect(self.albumButton_callback)
        self.btnMusic.clicked.connect(self.musicButton_callback)
        self.btnFavorite.clicked.connect(self.favoriteButton_callback)
        self.btnNet.clicked.connect(self.netButton_callback)

        self.btnLast.clicked.connect(self.lastButton_callback)
        self.btnPlay.clicked.connect(self.playButton_callback)
        self.btnNext.clicked.connect(self.nextButton_callback)
        # self.btnVol.clicked.connect(self.volButton_callback)

        self.addFav.clicked.connect(self.addFavButton_callback)
        self.treeWidget.itemDoubleClicked['QTreeWidgetItem*','int'].connect(self.tree1_callback)
        self.fav_treeWidget.itemDoubleClicked['QTreeWidgetItem*','int'].connect(self.tree1_callback)


    def initWindow(self):
        self.showView(self.list_view)
        self.highlightTab(self.btnMusic)
        songs = self.data.displaySong()
        self.songs = songs
        self.treeWidget.clear()
        for song in songs:
            # print(song)
            item = QTreeWidgetItem(self.treeWidget)
            for i in range(4):
                item.setText(i, str(song[i]))

    def searchButton_callback(self):
        string = self.lineEdit.text()
        songs = self.data.selectSong(string)
        self.treeWidget.clear()
        item = QTreeWidgetItem(self.treeWidget)
        for song in songs:
            for i in range(4):
                item.setText(i, song[i])

    def addFavButton_callback(self):
        if not self.song == 0:
            # print(self.data.getFav(self.song))
            if self.data.getFav(self.song) == 0:
                self.data.setFav(self.song ,1)
                self.addFav.setStyleSheet("border-image: url(D:/Y3CUHK/T2/CSCI3280/Project/pyqt/finally/ui/images/xin.png)")
            else:
                # print("13"
                self.data.setFav(self.song, 0)
                self.addFav.setStyleSheet("border-image: url(D:/Y3CUHK/T2/CSCI3280/Project/pyqt/finally/ui/images/kongxin.png)")

    def musicButton_callback(self):
        self.showView(self.list_view)
        self.highlightTab(self.btnMusic)
        songs = self.data.displaySong()
        self.songs = songs
        self.treeWidget.clear()
        for song in songs:
            # print(song)
            item = QTreeWidgetItem(self.treeWidget)
            for i in range(4):
                item.setText(i, str(song[i]))

    def favoriteButton_callback(self):
        self.showView(self.fav_view)
        self.highlightTab(self.btnFavorite)
        favoriteSongs = self.data.getFavSongs()
        self.songs = favoriteSongs
        self.fav_treeWidget.clear()
        for song in favoriteSongs:
            item = QTreeWidgetItem(self.fav_treeWidget)
            for i in range(4):
                item.setText(i, str(song[i]))
        
    
    def netButton_callback(self):
        # self.pop.show()
        self.pop.exec()
        if self.pop.tab == 1:
            ip_addr = self.pop.ip_addr
            port = self.pop.port
            if not ip_addr == '' and not port == '':
                self.data.setClient(ip_addr, int(port))
                # self.data.clientStart()
                print("Connected to " + ip_addr + ' ! ' + port)
                songs = self.data.displaySong()
                self.songs = songs
                self.treeWidget.clear()
                for song in songs:
                    # print(song)
                    item = QTreeWidgetItem(self.treeWidget)
                    for i in range(4):
                        item.setText(i, str(song[i]))

        elif self.pop.tab == 2:
            filename = self.pop.filename
            song_name = self.pop.song.text()
            album_name = self.pop.album.text()
            singer_name = self.pop.singer.text()
            # print("albumfile:"+)
            albumfile =  self.pop.input_artwork.text()
            lrcfile = self.pop.input_lyrics.text()
            self.data.addSong(song_name, album_name, singer_name, 0, filename, lrcfile, albumfile)
            songs = self.data.displaySong()
            self.songs = songs
            self.treeWidget.clear()
            for song in songs:
                # print(song)
                item = QTreeWidgetItem(self.treeWidget)
                for i in range(4):
                    item.setText(i, str(song[i]))

    def lastButton_callback(self):
        numOfSongs = len(self.songs)

        for i in range(numOfSongs):

            if self.songs[i][0] == self.song:

                self.music.stop()
                self.showView(self.song_view)
                self.highlightTab(None)

                self.playMusic(self.songs[(i-1)%numOfSongs][0])

                break

    def playButton_callback(self):
        if not self.play:
            if self.music != 0:
                self.t.play()
                self.play = True
                self.music.resume()
                self.btnPlay.setStyleSheet(
                    "QPushButton {border-image: url(D:/Y3CUHK/T2/CSCI3280/Project/pyqt/finally/ui/images/pause.png);}")
        else:
            self.t.pause()
            self.play = False
            self.btnPlay.setStyleSheet(
                "QPushButton {border-image: url(D:/Y3CUHK/T2/CSCI3280/Project/pyqt/finally/ui/images/bofang.png);}")
            self.music.pause()

    def nextButton_callback(self):
        numOfSongs = len(self.songs)

        for i in range(numOfSongs):

            if self.songs[i][0] == self.song:

                self.music.stop()
                self.showView(self.song_view)
                self.highlightTab(None)

                self.playMusic(self.songs[(i+1)%numOfSongs][0])

                break

    def tree1_callback(self, item, column_no):
        self.showView(self.song_view)
        self.highlightTab(None)

        song = item.text(0)
        if self.song != song and self.music != 0:
            self.music.stop()
            self.music = 0
        
        if self.music == 0:
            # ip_addr = '0'
            ip_addr = self.data.getIpAddress(song)
            print(song, ip_addr)
            if ip_addr == 0:
                print(song)
                minute, second = item.text(3).split(':')
                self.duration = int(minute)*60 + int(second)
                self.t = TimeControl(self.duration, self.updateProgressBar)
                self.t.setDuration(self.duration)
                self.t.play()

                self.playMusic(song)
            else:

                self.data.getSong(song)
                time.sleep(1)
                self.playMusic(song)
                fileName = self.data.getFilename(song)
                lrcName = self.data.getLRCFilename(song)

    def playMusic(self, song):
        if self.data.getFav(song) == 0:
            self.addFav.setStyleSheet("border-image: url(D:/Y3CUHK/T2/CSCI3280/Project/pyqt/finally/ui/images/kongxin.png)")
        else:
            self.addFav.setStyleSheet("border-image: url(D:/Y3CUHK/T2/CSCI3280/Project/pyqt/finally/ui/images/xin.png)")
        
        self.song = song
        self.play = True
        fileName = self.data.getFilename(song)
        lrcName = self.data.getLRCFilename(song)
        imagePath = self.data.getAlbumFilename(song)
        singer = self.data.getSinger(song)
        # lrcName = ''
        self.musicSlider.setValue(0)
        self.music = Wave_play.Wave_Player(fileName, lrcName)
        
        self.alubum_artwork.setStyleSheet("border-image: url(./data/" + imagePath + ");")
        self.label_2.setText(song+"\n"+singer)
        self.btnPlay.setStyleSheet("border-image: url(D:/Y3CUHK/T2/CSCI3280/Project/pyqt/finally/ui/images/pause.png);")

        thread = threading.Thread(target = self.displayLrc)
        thread.start()

    def displayLrc(self):
        last = ""
        self.label.setWordWrap(True)
        while 1:
            with open('temp.txt','r') as f:

                line = f.readline()
                
                # print(line)
                if last != line:
                    self.label.setText(line)

                last = line


    def showView(self, view):
        for x in self.view_controller:
            x.hide()
        view.show()

    def highlightTab(self, tab):
        for x in self.tab_controller:
            x.setStyleSheet(self.tab_default_style)
        if tab != None:
            tab.setStyleSheet(self.tab_highlight_style)
            self.addFav.hide()
        else:
            self.addFav.show()

    def closeEvent(self, event):
        if (self.music != 0):
            self.music.pause()
            self.t.pause()
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if (self.music != 0):
                self.music.stop()
            event.accept()
        else:
            if (self.music != 0):
                self.music.resume()
            event.ignore()

    def updateProgressBar(self, value):
        value = round(round(time.time() * 1) - value)
        # print(value, end=' ')
        value = int(value * 1000 // self.duration)
        # print(value)
        self.musicSlider.setValue(value)


class PopWindow(add.Ui_Dialog, QDialog):
    # def __init__(self, port):
    def __init__(self):
        super(PopWindow, self).__init__()
        self.setupUi(self)
        self.connect_btnbox.accepted.connect(self.connect_acc)
        self.connect_btnbox.rejected.connect(self.rej)
        self.add_file_btnbox.accepted.connect(self.add_file_acc)
        self.add_file_btnbox.rejected.connect(self.rej)

        self.select_file_btn.clicked.connect(self.select_file)
        self.select_artwork_btn.clicked.connect(self.select_artwork)
        self.select_lyrics_btn.clicked.connect(self.select_lyrics)

        self.ip_addr = ""
        self.port = ""
        self.tab = 0

        self.filename = ""
        self.artwork_filename = ""
        self.lyrics_filename = ""

    def connect_acc(self):
        self.ip_addr = self.lineEdit.text()
        self.port = self.lineEdit_2.text()
        self.tab = 1
        self.close()

    def add_file_acc(self):
        self.tab = 2
        self.close()

    def select_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(None, 'Open File', "","Wav files (*.wav)", options=QFileDialog.DontUseNativeDialog)
        # print(self.filename)
        self.input_file.setText(self.filename)

    def select_artwork(self):
        self.artwork_filename, _ = QFileDialog.getOpenFileName(None, 'Open File', "","Image Files (*.png *.jpg *.bmp)", options=QFileDialog.DontUseNativeDialog)
        self.input_artwork.setText(self.artwork_filename)
        # print("artword filename:" + self.artwork_filename)

    def select_lyrics(self):
        self.lyrics_filename, _ = QFileDialog.getOpenFileName(None, 'Open File', "","Lyrics Files (*.lrc)", options=QFileDialog.DontUseNativeDialog)
        self.input_lyrics.setText(self.lyrics_filename)
        # print("lrc filename:"+self.lyrics_filename)


    def rej(self):
        self.close()



class TimeControl:

    def __init__(self, duration, fn):
        self.startTime = 0
        self.duration = duration
        self.pauseTime = 0
        self.fn = fn
        self.timer = []

    def setDuration(self, duration):
        self.duration = duration

    def play(self):
        self.startTime = round(time.time() * 1)
        self.timer = [threading.Timer((i+1)/1, self.fn, [self.startTime - self.pauseTime]) for i in range(self.duration - self.pauseTime)] 
        for i in range(self.duration - self.pauseTime):
            self.timer[i].start()

    def pause(self):
        for i in range(self.duration - self.pauseTime):
            self.timer[i].cancel()
        self.pauseTime = round(round(time.time() * 1) - self.startTime + self.pauseTime)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    port = sys.argv[1]
    window = MainWindow(int(port))
    window.show()
    app.exec_()
    sys.exit(window.t.pause())