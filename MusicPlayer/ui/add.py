# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        Dialog.setMaximumSize(QtCore.QSize(400, 400))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(0, 12, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.add_file = QtWidgets.QWidget()
        self.add_file.setObjectName("add_file")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.add_file)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.add_file)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_13)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.song = QtWidgets.QLineEdit(self.frame_13)
        self.song.setMinimumSize(QtCore.QSize(200, 0))
        self.song.setMaximumSize(QtCore.QSize(200, 16777215))
        self.song.setObjectName("song")
        self.horizontalLayout_2.addWidget(self.song)
        self.verticalLayout.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_10)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_14)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.album = QtWidgets.QLineEdit(self.frame_14)
        self.album.setMinimumSize(QtCore.QSize(200, 0))
        self.album.setMaximumSize(QtCore.QSize(200, 16777215))
        self.album.setObjectName("album")
        self.horizontalLayout_6.addWidget(self.album)
        self.verticalLayout.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_10)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_15)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.singer = QtWidgets.QLineEdit(self.frame_15)
        self.singer.setMinimumSize(QtCore.QSize(200, 0))
        self.singer.setMaximumSize(QtCore.QSize(200, 16777215))
        self.singer.setObjectName("singer")
        self.horizontalLayout_5.addWidget(self.singer)
        self.verticalLayout.addWidget(self.frame_15)
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.input_artwork = QtWidgets.QLineEdit(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_artwork.sizePolicy().hasHeightForWidth())
        self.input_artwork.setSizePolicy(sizePolicy)
        self.input_artwork.setMinimumSize(QtCore.QSize(164, 0))
        self.input_artwork.setMaximumSize(QtCore.QSize(164, 16777215))
        self.input_artwork.setObjectName("input_artwork")
        self.horizontalLayout_7.addWidget(self.input_artwork)
        self.select_artwork_btn = QtWidgets.QToolButton(self.frame_11)
        self.select_artwork_btn.setObjectName("select_artwork_btn")
        self.horizontalLayout_7.addWidget(self.select_artwork_btn)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_12)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.input_lyrics = QtWidgets.QLineEdit(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_lyrics.sizePolicy().hasHeightForWidth())
        self.input_lyrics.setSizePolicy(sizePolicy)
        self.input_lyrics.setMinimumSize(QtCore.QSize(164, 0))
        self.input_lyrics.setMaximumSize(QtCore.QSize(164, 16777215))
        self.input_lyrics.setObjectName("input_lyrics")
        self.horizontalLayout_8.addWidget(self.input_lyrics)
        self.select_lyrics_btn = QtWidgets.QToolButton(self.frame_12)
        self.select_lyrics_btn.setObjectName("select_lyrics_btn")
        self.horizontalLayout_8.addWidget(self.select_lyrics_btn)
        self.verticalLayout.addWidget(self.frame_12)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_file_btnbox = QtWidgets.QDialogButtonBox(self.frame_9)
        self.add_file_btnbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.add_file_btnbox.setObjectName("add_file_btnbox")
        self.horizontalLayout_4.addWidget(self.add_file_btnbox)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.gridLayout_8.addWidget(self.frame_7, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_6, 1, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.add_file)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.frame_8)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.input_file = QtWidgets.QLineEdit(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_file.sizePolicy().hasHeightForWidth())
        self.input_file.setSizePolicy(sizePolicy)
        self.input_file.setMinimumSize(QtCore.QSize(164, 0))
        self.input_file.setMaximumSize(QtCore.QSize(164, 16777215))
        self.input_file.setObjectName("input_file")
        self.horizontalLayout.addWidget(self.input_file)
        self.select_file_btn = QtWidgets.QToolButton(self.frame_8)
        self.select_file_btn.setObjectName("select_file_btn")
        self.horizontalLayout.addWidget(self.select_file_btn)
        self.gridLayout_6.addWidget(self.frame_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.add_file, "")
        self.connect = QtWidgets.QWidget()
        self.connect.setObjectName("connect")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.connect)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.connect)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.connect_btnbox = QtWidgets.QDialogButtonBox(self.frame_5)
        self.connect_btnbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.connect_btnbox.setObjectName("connect_btnbox")
        self.horizontalLayout_3.addWidget(self.connect_btnbox)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.connect, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Song:"))
        self.label_5.setText(_translate("Dialog", "Album:"))
        self.label_6.setText(_translate("Dialog", "Singer:"))
        self.label_7.setText(_translate("Dialog", "Album Artwork:"))
        self.select_artwork_btn.setText(_translate("Dialog", "..."))
        self.label_8.setText(_translate("Dialog", "Lyrics:"))
        self.select_lyrics_btn.setText(_translate("Dialog", "..."))
        self.label_9.setText(_translate("Dialog", "File:"))
        self.select_file_btn.setText(_translate("Dialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_file), _translate("Dialog", "Add File"))
        self.label.setText(_translate("Dialog", "IP Address:"))
        self.label_2.setText(_translate("Dialog", "Port Number:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.connect), _translate("Dialog", "Connect"))


