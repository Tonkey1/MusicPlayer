from server import Server
from client import Client
from dataset import Dataset
import pandas as pd
from threading import Thread
import os, wave
class Test(object):
    """docstring for Test"""
    def __init__(self,serverport):
        self._dataset = Dataset()
        self._server = Server(serverport)
        self._clients = []
        self._client_num = 0
        server_thread = Thread(target=self.serverStart)
        server_thread.start()


    def serverStart(self):
        self._server.start()

    def setClient(self,servername,clientport):      
        self._clients.append(Client(servername,clientport))
        self._clients[self._client_num].start()
        self._clients[self._client_num].loadDataset()
        self._dataset.combine_other(self._clients[self._client_num]._servername)
        self._client_num +=1

    def findClient(self,servername):
        for obj in self._clients:
            if obj._servername == servername:
                return obj

    def getSong(self,song):
        _result = self._dataset._df[self._dataset._df['song'] == song]
        result = _result[_result['owner'] != 0]
        if result.shape[0] == 0:
            print("I cannot find this file")
        else:
            client = self.findClient(result['owner'].values[0])
            client_thread = Thread(target=client.download,args =(song,self._dataset._df))
            client_thread.start()
            # client.download(song, self._dataset._df)
            result['favorite'] = 0
            result['owner'] = 0
            self._dataset.addRow(result)
    
    def wav_time(self,filename):
        fname = wave.open(filename,'r')
        frames = fname.getnframes()
        rate = fname.getframerate()
        duration = frames / float(rate)
        return duration

    def addSong(self,song,album,singer,length,filename,lrcfile,albumfile):
        _filename = ''
        count = 0
        for x in filename.split('/'):
            if count == 0:
                _filename = x
                count += 1
            else:
                _filename += ("\\"+x)

        # print(filename, _filename)
        os.system("copy"+ " \""+_filename+"\""+" .\\data >nul")
        final_filename = filename.split('/')[-1]
        length = self.wav_time("./data/"+final_filename)
        length = str(int(int(length)/ 60)) + ":" + str(int(length)%60)
        final_lrcfilename = ''
        if (lrcfile != ""):
            _lrcfilename = ''
            count = 0
            for y in lrcfilename.split('/'):
                if count == 0:
                    _lrcfilename = y
                    count += 1
                else:
                    _lrcfilename += ("\\"+y)
            final_lrcfilename = lrcfile.split('/')[-1]
        # print(filename, _filename)
            os.system("copy"+ " \""+_lrcfilename+"\""+" .\\data >nul")

        final_albumfile = "default.jpg"
        if(albumfile != ""):
            _albumfilename = ''
            count = 0
            for z in albumfile.split('/'):
                if count == 0:
                    _albumfilename = z
                    count += 1
                else:
                    _albumfilename += ("\\"+z)
            final_albumfile = albumfile.split('/')[-1]
        df = pd.DataFrame(columns=['song', 'album', 'singer', 'length', 'filename','lrcfile','albumfile'])
        df.loc[0] = [song,album,singer,length,final_filename,final_lrcfilename,final_albumfile]
        df['favorite'] = 0
        df['owner'] = 0
        # print(df)
        self._dataset.addRow(df)

    def selectSong(self,songname):
        return self._dataset.searchSong(songname).values


    def displaySong(self):
        result = self._dataset.getDataset()
        return result.values

    def setFav(self,songname,value):
        self._dataset.setFavorite(songname,value)

    def getFav(self,songname):
        return self._dataset.getFavorite(songname)

    def getIpAddress(self,songname):
        return self._dataset.getIp(songname)

    def getFilename(self,songname):
        fileset = self._dataset.searchFilename(songname)
        # self._dataset[self._dataset['song']== songname]['ow']
        filename = fileset[fileset['owner'] == 0]['filename'].values[0]
        return filename

    def getAlbumFilename(self,songname):
        fileset = self._dataset.searchAlbumFilename(songname)
        # self._dataset[self._dataset['song']== songname]['ow']
        filename = fileset[fileset['owner'] == 0]['albumfile'].values[0]
        return filename   

    def getLRCFilename(self,songname):
        fileset = self._dataset.searchLRCFilename(songname)
        # self._dataset[self._dataset['song']== songname]['ow']
        filename = fileset[fileset['owner'] == 0]['lrcfile'].values[0]
        return filename       

    def displayDataFrame(self):
        print("")
        print("HERE IS DATAFRAME")
        print(self._dataset._df)
        print("")

    def getSinger(self,songname):
        return self._dataset.getSingerName(songname)

    def getFavSongs(self):
        print(self._dataset.searchAllFavSongs().values)
        return self._dataset.searchAllFavSongs().values

    def downloadPPM(self,filename):
        filepath = './data/'+filename
        filesize = os.path.getsize(filepath)
        remainSize = filesize
        readedSize = 0
        while remainSize != 0:
            for obj in self._clients:
                if remainSize >= 128:
                    obj.combinePPM(filepath,readedSize,128)
                    remainSize -=128
                    readedSize +=128
                else:
                    obj.combinePPM(filepath,readedSize,remainSize)
                    remainSize -=remainSize
                    readedSize += remainSize
            if remainSize >= 128:
                remainSize -=128
                readedSize +=128
            else:
                remainSize -=remainSize
                readedSize += remainSize


# if __name__ == "__main__":
#     port = input("enter an port: ")
#     test = Test(int(port))
    

#     operation = input("your operation:(end or get song)")
#     while(operation != 'end'):

#         if(operation == 'add'):
#             song = input("song:")
#             singer = input("singer: ")
#             album = input("album: ")
#             length = input("length: ")
#             filename = input("filename: ")
#             test.addSong(song,singer,album,length,filename)
        
#         elif operation == 'get':
#             songname = input("songname: ")
#             test.getSong(songname)

        
#         elif operation == 'connect':
#             servername = input("servername: ")
#             clientport = int(input("clientport: "))
#             test.setClient(servername,clientport)
        
#         elif operation == 'select':
#             songname = input("songname: ")
#             print(test.selectSong(songname))
#         elif operation == 'show':
#             print(test.displaySong())

#         test.displayDataFrame()
#         operation = input("your operation:(end or get song)")
