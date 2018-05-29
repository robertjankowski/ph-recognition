# Class to load data from a files
import cv2
import numpy as np
import pandas as pd


class LoadData:
	def __init__(self, numbers_of_folders):
		self.files = 15
		self.numbers_of_folders = numbers_of_folders
		self.data_dir = r'C:\\Users\\asus\\Desktop\\data_science_python\\ph_project\\ph_datasets\\'
		self.images_list = []
	def load_data(self):
		for j in range(self.numbers_of_folders):
			for i in range(self.files):
				image = cv2.imread(self.data_dir + 'ph{}\\{}.jpg'.format(j+1, i))
				try :
					self.images_list.append([image[3][3][0],image[3][3][1],image[3][3][2],i])
				except Exception:
					print('no image')
		df = pd.DataFrame(np.asarray(self.images_list), columns=['blue','green','red','label'])
		return df 
	 