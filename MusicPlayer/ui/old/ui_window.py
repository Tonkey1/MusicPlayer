# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 656)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(100, 120))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_3.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_14.setContentsMargins(12, 0, 30, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pkq = QtWidgets.QGraphicsView(self.frame_3)
        self.pkq.setMinimumSize(QtCore.QSize(100, 100))
        self.pkq.setMaximumSize(QtCore.QSize(100, 100))
        self.pkq.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-image: url(:/images/pi.png);")
        self.pkq.setObjectName("pkq")
        self.horizontalLayout_14.addWidget(self.pkq)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(700, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(700, 16777215))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"font: 15pt, \"Arial\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnSearch = QtWidgets.QPushButton(self.frame_6)
        self.btnSearch.setMinimumSize(QtCore.QSize(30, 30))
        self.btnSearch.setMaximumSize(QtCore.QSize(30, 30))
        self.btnSearch.setStyleSheet("border-image: url(:/images/fangdajing.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.btnSearch.setText("")
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout_3.addWidget(self.btnSearch)
        spacerItem1 = QtWidgets.QSpacerItem(54, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnAlbum = QtWidgets.QPushButton(self.frame_7)
        self.btnAlbum.setStyleSheet("font: Bold 15pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.btnAlbum.setObjectName("btnAlbum")
        self.horizontalLayout_4.addWidget(self.btnAlbum)
        self.btnMusic = QtWidgets.QPushButton(self.frame_7)
        self.btnMusic.setStyleSheet("font: Bold 15pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.btnMusic.setObjectName("btnMusic")
        self.horizontalLayout_4.addWidget(self.btnMusic)
        self.btnFavorite = QtWidgets.QPushButton(self.frame_7)
        self.btnFavorite.setStyleSheet("font: Bold 15pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.btnFavorite.setObjectName("btnFavorite")
        self.horizontalLayout_4.addWidget(self.btnFavorite)
        spacerItem2 = QtWidgets.QSpacerItem(611, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_7)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.frame_5)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.btnNet = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNet.sizePolicy().hasHeightForWidth())
        self.btnNet.setSizePolicy(sizePolicy)
        self.btnNet.setMinimumSize(QtCore.QSize(50, 50))
        self.btnNet.setMaximumSize(QtCore.QSize(50, 50))
        self.btnNet.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-image: url(:/images/+.png);")
        self.btnNet.setText("")
        self.btnNet.setObjectName("btnNet")
        self.horizontalLayout_14.addWidget(self.btnNet)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.main_frame = QtWidgets.QFrame(self.frame)
        self.main_frame.setStyleSheet("background-color: rgb(89, 91, 96);")
        self.main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.song_view = QtWidgets.QFrame(self.main_frame)
        self.song_view.setMinimumSize(QtCore.QSize(1000, 0))
        self.song_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.song_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.song_view.setObjectName("song_view")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.song_view)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.song_info = QtWidgets.QFrame(self.song_view)
        self.song_info.setMinimumSize(QtCore.QSize(300, 0))
        self.song_info.setMaximumSize(QtCore.QSize(0, 16777215))
        self.song_info.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.song_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.song_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.song_info.setObjectName("song_info")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.song_info)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.song_info)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.alubum_artwork = QtWidgets.QLabel(self.song_info)
        self.alubum_artwork.setMinimumSize(QtCore.QSize(100, 100))
        self.alubum_artwork.setMaximumSize(QtCore.QSize(200, 200))
        self.alubum_artwork.setStyleSheet("image: url(:/images/hcy.jpg);")
        self.alubum_artwork.setText("")
        self.alubum_artwork.setObjectName("alubum_artwork")
        self.gridLayout_4.addWidget(self.alubum_artwork, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.song_info, 0, 0, 1, 1)
        self.lyrics_frame = QtWidgets.QFrame(self.song_view)
        self.lyrics_frame.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.lyrics_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lyrics_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lyrics_frame.setObjectName("lyrics_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.lyrics_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.lyrics_frame)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont("Arial")
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.lyrics_frame, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.song_view)
        self.list_view = QtWidgets.QFrame(self.main_frame)
        self.list_view.setMinimumSize(QtCore.QSize(10, 0))
        self.list_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_view.setObjectName("list_view")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.list_view)
        self.gridLayout_7.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.treeWidget = QtWidgets.QTreeWidget(self.list_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.treeWidget.setFont(font)
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.treeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.treeWidget.setLineWidth(0)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(19)
        self.treeWidget.headerItem().setFont(0, font)
        self.treeWidget.headerItem().setBackground(0, QtGui.QColor(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.treeWidget.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.treeWidget.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.treeWidget.headerItem().setFont(3, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setDefaultSectionSize(200)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(24)
        self.gridLayout_7.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.list_view)
        self.verticalLayout_4.addWidget(self.main_frame)
        self.bottom_frame = QtWidgets.QFrame(self.frame)
        self.bottom_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.bottom_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.bottom_frame.setStyleSheet("background-color: rgb(186, 190, 190);")
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnLast = QtWidgets.QPushButton(self.bottom_frame)
        self.btnLast.setMinimumSize(QtCore.QSize(50, 50))
        self.btnLast.setMaximumSize(QtCore.QSize(50, 50))
        self.btnLast.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-image: url(:/images/last.png);")
        self.btnLast.setText("")
        self.btnLast.setObjectName("btnLast")
        self.horizontalLayout_2.addWidget(self.btnLast)
        self.btnPlay = QtWidgets.QPushButton(self.bottom_frame)
        self.btnPlay.setMinimumSize(QtCore.QSize(70, 70))
        self.btnPlay.setMaximumSize(QtCore.QSize(70, 70))
        self.btnPlay.setStyleSheet("border-image: url(:/images/bofang.png);")
        self.btnPlay.setText("")
        self.btnPlay.setAutoDefault(False)
        self.btnPlay.setObjectName("btnPlay")
        self.horizontalLayout_2.addWidget(self.btnPlay)
        self.btnNext = QtWidgets.QPushButton(self.bottom_frame)
        self.btnNext.setMinimumSize(QtCore.QSize(50, 50))
        self.btnNext.setMaximumSize(QtCore.QSize(50, 50))
        self.btnNext.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-image: url(:/images/next.png);")
        self.btnNext.setText("")
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout_2.addWidget(self.btnNext)
        self.frame_4 = QtWidgets.QFrame(self.bottom_frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.musicSlider = QtWidgets.QSlider(self.frame_4)
        self.musicSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid;\n"
"height: 8px;\n"
"border-radius: 4px;\n"
"margin-left: 1.5px;\n"
"margin-right: 5px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background-color: rgb(132, 132, 132);\n"
"border: 0px solid;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-image: url(:images/pkq.png);\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 35px;\n"
"margin-top: -8px;\n"
"margin-bottom: -8px;\n"
"margin-left: -10px;\n"
"margin-right: -10px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 255, 255, 0);\n"
"}")
        self.musicSlider.setTracking(False)
        self.musicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.musicSlider.setObjectName("musicSlider")
        self.gridLayout_5.addWidget(self.musicSlider, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.btnVol = QtWidgets.QPushButton(self.bottom_frame)
        self.btnVol.setMaximumSize(QtCore.QSize(30, 50))
        self.btnVol.setStyleSheet("border-image: url(:/images/laba.png);")
        self.btnVol.setText("")
        self.btnVol.setObjectName("btnVol")
        self.horizontalLayout_2.addWidget(self.btnVol)
        self.volSlider = QtWidgets.QSlider(self.bottom_frame)
        self.volSlider.setMinimumSize(QtCore.QSize(70, 0))
        self.volSlider.setMaximumSize(QtCore.QSize(70, 16777215))
        self.volSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid;\n"
"height: 8px;\n"
"border-radius: 4px;\n"
"margin-left: 1.5px;\n"
"margin-right: 5px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background-color: rgb(132, 132, 132);\n"
"border: 0px solid;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-image: url(:images/pkq.png);\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 35px;\n"
"margin-top: -8px;\n"
"margin-bottom: -8px;\n"
"margin-left: -10px;\n"
"margin-right: -10px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 255, 255, 0);\n"
"}\n"
"QSlider{\n"
"\n"
"}")
        self.volSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volSlider.setObjectName("volSlider")
        self.horizontalLayout_2.addWidget(self.volSlider)
        self.verticalLayout_4.addWidget(self.bottom_frame)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAlbum.setText(_translate("MainWindow", "Album"))
        self.btnMusic.setText(_translate("MainWindow", "Music"))
        self.btnFavorite.setText(_translate("MainWindow", "Favorite"))
        self.label_2.setText(_translate("MainWindow", "I\'m Boring"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Song"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Singer"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Album"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Time"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Tik Tok"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "I\'m Boring"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


import resources_rc
