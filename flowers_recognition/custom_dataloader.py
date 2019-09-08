import os

import numpy as np
import pandas as pd

from PIL import Image

import cv2
from sklearn.utils import shuffle
from keras.utils import np_utils

import matplotlib.pyplot as plt

from config import Config

class FlowerRecognition(object):
    
    def __init__(self,root_dir=None):     
        self.root_dir = root_dir
        
    def load_samples(self,csv_file):
        # Read the csv file
        data = pd.read_csv(os.path.join(self.root_dir,'data_files',csv_file))
        data = data[['FileName', 'Label', 'ClassName']]
        # Get the filename contained in the first column
        file_names = list(data.iloc[:,0])
        # Get the labels present in the second column
        labels = list(data.iloc[:,1])
        samples=[]
        for samp,lab in zip(file_names,labels):
            samples.append([samp,lab])
        return samples
        
    def shuffle_data(self,data):
        data = shuffle(data)#,random_state=2)
        return data
    
    def preprocessing(self,img,label):
        img = cv2.resize(img,(Config.resize,Config.resize))
        img = img/255
        label = np_utils.to_categorical(label, Config.num_classes)
        return img,label
    
    def data_generator(self,data,batch_size=10,shuffle=True):              
        """
        Yields the next training batch.
        Suppose `samples` is an array [[image1_filename,label1], [image2_filename,label2],...].
        """
        num_samples = len(data)
        if shuffle:
            data = self.shuffle_data(data)
        while True:   
            for offset in range(0, num_samples, batch_size):
#                print ('startring index: ', offset) 
                # Get the samples you'll use in this batch
                batch_samples = data[offset:offset+batch_size]
                # Initialise X_train and y_train arrays for this batch
                X_train = []
                y_train = []
                # For each example
                for batch_sample in batch_samples:
#                    print (batch_sample)
                    # Load image (X)
#                    x = batch_sample[0]
                    img_name = batch_sample[0]
                    label = batch_sample[1]

                    img = cv2.imread(os.path.join(self.root_dir,img_name))
#                    print (img.shape)
#                    img = cv2.resize(img,(224,224))
                    # Preprocessing
                    img,label = self.preprocessing(img,label)
#                    print (img.shape)
                    X_train.append(img)
                    y_train.append(label)
        
                # Make sure they're numpy arrays (as opposed to lists)
                X_train = np.array(X_train)
#                X_train = np.rollaxis(X_train,1,4)
                y_train = np.array(y_train)
        
                # The generator-y part: yield the next training batch            
                yield X_train, y_train
    
if __name__=='__main__':

   dataloader = FlowerRecognition(root_dir=r'D:\Trainings-2019\custom_data_generator\flowers_recognition')
   
   train_data_path = 'flowers_recognition_train.csv'
   test_data_path = 'flowers_recognition_test.csv'

   train_samples = dataloader.load_samples(train_data_path)
   test_samples = dataloader.load_samples(test_data_path)

   num_train_samples = len(train_samples)
   num_test_samples = len(test_samples)

   print ('number of train samples: ', num_train_samples)
   print ('number of test samples: ', num_test_samples) 
   
   # Create generator
   batch_size = Config.batch_size
   train_datagen = dataloader.data_generator(train_samples, batch_size=batch_size)
   test_datagen = dataloader.data_generator(test_samples, batch_size=batch_size)
   
   
   for k in range(1):
       x,y = next(train_datagen)
       print ('x shape: ', x.shape)
       print ('label shape: ', y.shape)
       print ('the label is: ',y)
        
    #train_samples[-15:-10]
    
    
   #### we can plot the data and see by ourselves
   fig = plt.figure(1,figsize=(12,12))
   for i in range(8):
      plt.subplot(4,4,i+1)
      plt.tight_layout()
      #x[i] = x[i][:,:,::-1] # converting BGR to RGB
      plt.imshow(x[i][:,:,::-1], interpolation='none')
      plt.title("class_label: {}".format(y[i]))
      plt.xticks([])
      plt.yticks([])
   plt