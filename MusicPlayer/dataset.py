import pandas as pd
import os

class Dataset(object):
	"""docstring for Dataset"""
	def __init__(self):
		self._df = pd.read_csv('./data/dataset.csv',
			header = None,
			names = ['song', 'album', 'singer', 'length', 'filename','lrcfile','albumfile'])
		self._df['favorite'] = 0
		self._df['owner'] = 0



	def searchSong(self,keyword):
		subdf = self._df[self._df['song'].str.contains(keyword)]
		subdf = subdf.sort_values(by=['owner','song'])
		subdf.drop_duplicates(subset ='song',keep = 'first',inplace = True)
		# print(subdf)
		return subdf[['song','album','singer','length', 'owner']]

	def combine_other(self,servername):
		# print("im in update")

		others_df = pd.read_csv('./data/dataset_temp.csv',
			header = None,
			names = ['song', 'album', 'singer', 'length', 'filename','lrcfile','albumfile'])
		others_df['favorite'] = 0
		others_df['owner'] = servername
		# result = self._df.append(others_df)
		# print("this is foreign df")
		# print(others_df)
		result = pd.concat([self._df, others_df])
		self._df = result.sort_values(by=['owner','song'])
		# print(self._df)
		os.remove('./data/dataset_temp.csv')


	def searchAllFavSongs(self):
		result = self._df[self._df['favorite']== 1]
		print(result)
		_result = result[result['owner'] == 0]
		# print(subdf)
		return _result[['song','album','singer','length', 'owner']]

	def addRow(self,dataset):
		result = pd.concat([self._df,dataset])
		self._df = result.sort_values(by=['owner','song'])

	def getDataset(self):
		result = self._df[self._df['owner'] == 0]
		return self._df[['song','album','singer','length']]

	def getIp(self,songname):
		result = self._df[self._df['song']== songname]
		
		_result = result['owner'].values[0]
		print(_result)
		return _result

	def getSingerName(self,songname):
		result = self._df[self._df['song']== songname]
		_result = result[result['owner'] == 0]['singer'].values[0]
		return _result

	def getFavorite(self,songname):
		result = self._df[self._df['song']== songname]
		_result = result[result['owner'] == 0]['favorite'].values[0]
		return _result

	def setFavorite(self,songname,value):
		self._df.loc[self._df['song']== songname, 'favorite'] = value

	def searchFilename(self, songname):
		return self._df[self._df['song']== songname][['owner','filename']]
	

	def searchAlbumFilename(self,songname):
		return self._df[self._df['song']== songname][['owner','albumfile']]


	def searchLRCFilename(self, songname):
		return self._df[self._df['song']== songname][['owner','lrcfile']]