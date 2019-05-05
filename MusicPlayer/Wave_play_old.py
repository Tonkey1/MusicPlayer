import wave
import pyaudio
import msvcrt
# import pygame
import threading
import time


import sys
import os

class Job1(threading.Thread):

    def __init__(self,filename):
        super(Job1, self).__init__()
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True
        self.filename = filename

    def run(self):

        while self.__running.isSet():
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            self.playwave(self.filename)


    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False

    def playwave(self, filename):
        CHUNK = 1024
        # 从目录中读取语音
        wf = wave.open(filename, 'rb')
        # read data
        data = wf.readframes(CHUNK)
        # 创建播放器
        p = pyaudio.PyAudio()

        # 获得语音文件的各个参数
        FORMAT = p.get_format_from_width(wf.getsampwidth())
        CHANNELS = wf.getnchannels()
        RATE = wf.getframerate()


        # print('FORMAT: {} \nCHANNELS: {} \nRATE: {}'.format(FORMAT, CHANNELS, RATE))
        # 打开音频流， output=True表示音频输出
        stream = p.open(format=FORMAT,

                        channels=CHANNELS,
                        rate=RATE,
                        frames_per_buffer=CHUNK,
                        output=True)
        # play stream (3) 按照1024的块读取音频数据到音频流，并播放
        while len(data) > 0 and self.__running.isSet():
            self.__flag.wait()
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()
        p.terminate()

class Job2(threading.Thread):

    def __init__(self,filename):
        super(Job2, self).__init__()
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True
        self.filename = filename

    def run(self):

        while self.__running.isSet():
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            self.play_lrc(self.filename)


    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False


    def play_lrc(self,filename):
        file = open(filename, "r", encoding="utf-8")

        musicLrc = file.read()
        lrcDict = {}  # 空字典
        musicLrcList = musicLrc.splitlines()
        # print(musicLrcList)

        for lrcLine in musicLrcList:
            lrcLineList = lrcLine.split("]")  # 切割时间
            # print(lrcLineList)
            if lrcLineList[1] != '':

                for index in range(len(lrcLineList) - 1):  # 多个时间，循环次数
                    #            00：03：45  》》  3：45
                    timeStr = lrcLineList[index][1:]  # 提取时间字符串
                    timeList = timeStr.split(":")  # 将时间分冒号前一个，后一个
                    # ：前面的乘60为一个浮点数，后面的为一个浮点数
                    time1 = float(timeList[0]) * 60 + float(timeList[1])
                    # 时间为key,歌词为value
                    lrcDict[time1] = lrcLineList[-1]  # 歌词时间存入字典

        #
        allTimeList = []
        for t in lrcDict:
            allTimeList.append(t)
        allTimeList.sort()
        # print(allTimeList)

        '''
        输入时间循环
        while 1:
            getTime = float(input("请输入时间"))
            for n in range(allTimeList):
                tempTime = allTimeList[n]
                if getTime < tempTime:
                    break
            if n == 0:
                print("时间小")
            else:
                print(lrcDict[allTimeList[n - 1]])

        '''
        # 自动循环播放歌词
        getTime = 0

        while self.__running.isSet():
            self.__flag.wait()
            for n in range(len(allTimeList)):
                tempTime = allTimeList[n]
                if getTime < tempTime:
                    break
            lrc = lrcDict.get(allTimeList[n - 1])
            if lrc == None:
                pass
            else:
                print(lrc)
            time.sleep(0.1)
            getTime += 0.1

class Wave_Player:
    def __init__(self, filename):

        self.filename = 'data/' + filename
        # self.lrc_file = "music/numb.lrc"

        threads = []
        self.t1 = Job1(self.filename)
        # self.t2 = Job2(self.lrc_file)

        threads.append(self.t1)
        self.t1.start()
        # self.t2.start()

    def pause(self):
        self.t1.pause()
        # self.t2.pause()

    def stop(self):
        self.t1.stop()
        # self.t2.stop()

    def resume(self):
        self.t1.resume()
        # self.t2.resume()
