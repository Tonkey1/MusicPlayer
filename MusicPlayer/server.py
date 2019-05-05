import socket
import sys
import os
import select
import re
import time

import pandas as pd
from threading import Thread, Lock
# from dataset import Dataset

class Server(object):
    """docstring for tcp_server"""
    mutex = Lock()
    def __init__(self,port):
        self._port = port
        self._host = self.get_host_ip()

    def get_host_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    def getHost(self):
        return self._host

    def start(self):
        while True:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # print("binding")
            server_socket.bind((self._host,self._port))
            print("listening!!!!")
            server_socket.listen(10)
            (sock,addr) = server_socket.accept() 
            thread = Thread(target=self.recvRequest,args =((sock,addr)))
            thread.start()
            # print("im end while")

    def recvRequest(self,conn,addr):
        while True:
            print(addr)
            _data = conn.recv(1024)
            data = _data.decode()
            # print('here',data)
            print(addr,"waiting lock")
            Server.mutex.acquire()


            if(data == 'loaddata'):
                print("loaded")
                filepath = './data/dataset.csv'
                filesize = os.path.getsize(filepath)
                conn.sendall(str(filesize).encode())
                # print("filesize is ",filesize)
                f = open(filepath,"rb")
                buffRead = 0
                bytesRemaining = filesize
                while bytesRemaining != 0:
                    if(bytesRemaining >= 1024):
                        buffRead = f.read(1024)
                        
                    else:
                        buffRead = f.read(bytesRemaining)

                    conn.sendall(buffRead)
                    # print("i have send")
                    bytesRemaining = bytesRemaining - len(buffRead)

            elif(data == 'ppm'):
                ack = 1
                conn.sendall(str(ack).encode())

                filepath = conn.recv(1024).decode()
                conn.sendall(str(ack).encode())

                offset = int(conn.recv(1024).decode())
                conn.sendall(str(ack).encode())

                readsize = int(conn.recv(1024).decode())

                with open(filepath,"rb") as f:
                    f.seek(offset)
                    buffRead = f.read(readsize)
                    conn.sendall(buffRead)

            else:
                print("Send file!")
                songname = data.split(" ",1)

                isExists = int(conn.recv(1024).decode())
                # print(songname[1])
                dataset = pd.read_csv('./data/dataset.csv', 
                    header = None,
                    names =['song', 'album', 'singer', 'length', 'filename','lrcfile','albumfile','favorite', 'owner'])
                
                # & (dataset['owner'] == self._host)
                filename = dataset.loc[(dataset['song'] == songname[1])]['filename'].values[0]
                # print(filename[0]) #todo 
                filepath= "./data/" + filename
                filesize = os.path.getsize(filepath)
                # print(filename,filesize)
                conn.sendall(str(filesize).encode())
                with open(filepath, "rb") as f:
                    buffRead = 0
                    bytesRemaining = filesize
                    # time.sleep(2)
                    while bytesRemaining != 0:
                        if(bytesRemaining >= 1024):
                            buffRead = f.read(1024)
                            
                        else:
                            buffRead = f.read(bytesRemaining)
                            # print(len(buffRead))
                        conn.sendall(buffRead)
                        bytesRemaining = bytesRemaining - len(buffRead)
                

                #send lrc file
                lrc_filename = dataset.loc[(dataset['song'] == songname[1])]['lrcfile'].values[0]
                if lrc_filename == "":
                    lrc_filesize = 0
                else:

                # print(filename[0]) #todo 
                    lrc_filepath= "./data/" + lrc_filename
                    lrc_filesize = os.path.getsize(lrc_filepath)
                # print(filename,filesize)
                conn.sendall(str(lrc_filesize).encode())
                ack = int(conn.recv(1024).decode())
                if lrc_filesize != 0:

                    with open(lrc_filepath, "rb") as lrc_f:
                        buffRead = 0
                        bytesRemaining = lrc_filesize
                        # time.sleep(2)
                        while bytesRemaining != 0:
                            if(bytesRemaining >= 1024):
                                buffRead = lrc_f.read(1024)
                                
                            else:
                                buffRead = lrc_f.read(bytesRemaining)
                                # print(len(buffRead))
                            conn.sendall(buffRead)
                            bytesRemaining = bytesRemaining - len(buffRead)

                #send album file
                if(isExists == 0):
                    album_filename = dataset.loc[(dataset['song'] == songname[1])]['albumfile'].values[0]
                    # print(filename[0]) #todo 
                    album_filepath= "./data/" + album_filename
                
                    album_filesize = os.path.getsize(album_filepath)
                    conn.sendall(str(album_filesize).encode())
                    ack = int(conn.recv(1024).decode())

                    if(album_filesize != 0):
                        with open(album_filepath, "rb") as album_f:
                            buffRead = 0
                            bytesRemaining = album_filesize
                            while bytesRemaining != 0:
                                if(bytesRemaining >= 1024):
                                    buffRead = album_f.read(1024)                            
                                else:
                                    buffRead = album_f.read(bytesRemaining)
                                    # print(len(buffRead))
                                conn.sendall(buffRead)
                                bytesRemaining = bytesRemaining - len(buffRead)


            Server.mutex.release()
            print("released lock")

