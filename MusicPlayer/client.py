from socket import *
import sys
import os
import time
import pandas as pd

class Client(object):
    """docstring for Client"""
    def __init__(self,servername,port):
        self._servername = servername
        self._port = port
        self._socket = socket(AF_INET, SOCK_STREAM)

    def start(self):
        self._socket.connect((self._servername, self._port))

    def loadDataset(self):
        operation = 'loaddata'
        self._socket.send(operation.encode())
        # print("im loading dataset")
        filesize = self._socket.recv(1024).decode()
        # print(filesize)
        with open("./data/dataset_temp.csv", "wb") as f:
            buffWrote = 0
            bytesRemaining = int(filesize)
            while bytesRemaining !=0:
                if(bytesRemaining >= 1024):
                    slab = self._socket.recv(1024)
                           
                else:
                    slab = self._socket.recv(bytesRemaining)
                f.write(slab)
                bytesRemaining = bytesRemaining -len(slab)

    def download(self,songname,dataset):
        operation = 'get '+songname
        isExists = 0
        ack = 1
        # print('my operation is', operation)
        self._socket.send(operation.encode())
        print("i will download file")
    
        album_filename = dataset.loc[(dataset['song'] == songname)]['albumfile'].values
        album_filepath= "./data/" + album_filename[0]

        if(os.path.exists(album_filepath)):
            isExists = 1
        self._socket.send(str(isExists).encode())

    #recv music
        filesize = self._socket.recv(1024).decode()
        # print(filesize)
        # print("type",type(dataset))
        filename = dataset.loc[(dataset['song'] == songname)]['filename'].values
        filepath= "./data/" + filename[0]
        # f = open("./data1/dataset.csv","a")
 
        with open(filepath, "wb") as f:
            buffWrote = 0
            bytesRemaining = int(filesize)
            while bytesRemaining !=0:
                if(bytesRemaining >= 1024):
                    slab = self._socket.recv(1024)
                           
                else:
                    slab = self._socket.recv(bytesRemaining)
                    # print(len(slab))
                f.write(slab)
                f.flush()
                bytesRemaining = bytesRemaining -len(slab)

    #recv lrc_file

        lrc_filesize = self._socket.recv(1024).decode()
        self._socket.send(str(ack).encode())

        if lrc_filesize != 0:
            print("lrc_filesize:",lrc_filesize)
            # print("type",type(dataset))
            lrc_filename = dataset.loc[(dataset['song'] == songname)]['lrcfile'].values
            lrc_filepath= "./data/" + lrc_filename[0]
        # f = open("./data1/dataset.csv","a")
 
            with open(lrc_filepath, "wb") as lrc_f:
                buffWrote = 0
                bytesRemaining = int(lrc_filesize)
                while bytesRemaining !=0:
                    if(bytesRemaining >= 1024):
                        slab = self._socket.recv(1024)
                               
                    else:
                        slab = self._socket.recv(bytesRemaining)
                        # print(len(slab))
                    lrc_f.write(slab)
                    bytesRemaining = bytesRemaining -len(slab)


    #recv album_file
        if(isExists == 0):
        # print(filesize)
        # print("type",type(dataset))
            album_filesize = self._socket.recv(1024).decode()
            self._socket.send(str(ack).encode())

            album_filename = dataset.loc[(dataset['song'] == songname)]['albumfile'].values
            album_filepath= "./data/" + album_filename[0]
            # f = open("./data1/dataset.csv","a")
     #todo 
            with open(album_filepath, "wb") as album_f:
                buffWrote = 0
                bytesRemaining = int(album_filesize)
                while bytesRemaining !=0:
                    if(bytesRemaining >= 1024):
                        slab = self._socket.recv(1024)
                               
                    else:
                        slab = self._socket.recv(bytesRemaining)
                        # print(len(slab))
                    album_f.write(slab)
                    bytesRemaining = bytesRemaining -len(slab)

    def combinePPM(self,filepath,offset,readsize):
        operation = "ppm"
        self._socket.send(operation.encode())
        self._socket.recv(1024)

        self._socket.send(filepath.encode())
        self._socket.recv(1024)

        self._socket.send(str(offset).encode())
        self._socket.recv(1024)

        self._socket.send(str(readsize).encode())

        slab = self._socket.recv(readsize)

        with open(filepath,"wb") as f:
            f.seek(offset)
            f.write(slab)
            f.flush()



