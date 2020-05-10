#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import cv2
import numpy as np
from sklearn.utils import shuffle
import os
from collections import deque
import copy
import matplotlib
import matplotlib.pyplot as plt
from keras.utils import np_utils

from config import Config

class ActionDataGenerator(object):
    
    def __init__(self,root_data_path,temporal_stride=1,temporal_length=16,resize=224):
        
        self.root_data_path = root_data_path
        self.temporal_length = temporal_length
        self.temporal_stride = temporal_stride
        self.resize=resize
    def file_generator(self,data_path,data_files):
        '''
        data_files - list of csv files to be read.
        '''
        for f in data_files:       
            tmp_df = pd.read_csv(os.path.join(data_path,f))
            label_list = list(tmp_df['Label'])
            total_images = len(label_list) 
            if total_images>=self.temporal_length:
                num_samples = int((total_images-self.temporal_length)/self.temporal_stride)+1
                print ('num of samples from vid seq-{}: {}'.format(f,num_samples))
                img_list = list(tmp_df['FileName'])
            else:
                print ('num of frames is less than temporal length; hence discarding this file-{}'.format(f))
                continue
            
            start_frame = 0
            samples = deque()
            samp_count=0
            for img in img_list:
                samples.append(img)
                if len(samples)==self.temporal_length:
                    samples_c=copy.deepcopy(samples)
                    samp_count+=1
                    for t in range(self.temporal_stride):
                        samples.popleft() 
                    yield samples_c,label_list[0]

    def load_samples(self,data_cat='train'):
        data_path = os.path.join(self.root_data_path,data_cat)
        csv_data_files = os.listdir(data_path)
        file_gen = self.file_generator(data_path,csv_data_files)
        iterator = True
        data_list = []
        while iterator:
            try:
                x,y = next(file_gen)
                x=list(x)
                data_list.append([x,y])
            except Exception as e:
                print ('the exception: ',e)
                iterator = False
                print ('end of data generator')
        return data_list
    
    def shuffle_data(self,samples):
        data = shuffle(samples,random_state=2)
        return data
    
    def preprocess_image(self,img):
        img = cv2.resize(img,(self.resize,self.resize))
        img = img/255
        return img
    
    def data_generator(self,data,batch_size=10,shuffle=True):              
        """
        Yields the next training batch.
        data is an array [[img1_filename,img2_filename...,img16_filename],label1], [image2_filename,label2],...].
        """
        num_samples = len(data)
        if shuffle:
            data = self.shuffle_data(data)
        while True:   
            for offset in range(0, num_samples, batch_size):
                #print ('startring index: ', offset) 
                # Get the samples you'll use in this batch
                batch_samples = data[offset:offset+batch_size]
                # Initialise X_train and y_train arrays for this batch
                X_train = []
                y_train = []
                # For each example
                for batch_sample in batch_samples:
                    # Load image (X)
                    x = batch_sample[0]
                    y = batch_sample[1]
                    temp_data_list = []
                    for img in x:
                        try:
                            img = cv2.imread(img)
                            #apply any kind of preprocessing here
                            #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            img = self.preprocess_image(img)
                            temp_data_list.append(img)
    
                        except Exception as e:
                            print (e)
                            print ('error reading file: ',img)  
    
                    # Read label (y)
                    #label = label_names[y]
                    # Add example to arrays
                    X_train.append(temp_data_list)
                    y_train.append(y)
        
                # Make sure they're numpy arrays (as opposed to lists)
                X_train = np.array(X_train)
                #X_train = np.rollaxis(X_train,1,4)
                y_train = np.array(y_train)
                y_train = np_utils.to_categorical(y_train, 3)

                # The generator-y part: yield the next training batch            
                yield X_train, y_train

if __name__=='__main__':
    
    root_data_path='data_files'
    
    data_gen_obj=ActionDataGenerator(root_data_path,temporal_stride=1,temporal_length=16)

    train_data = data_gen_obj.load_samples(data_cat='train')

    print('num of train_samples: {}'.format(len(train_data)))

    train_data[0]

    test_data = data_gen_obj.load_samples(data_cat='test')

    print('num of test_samples: {}'.format(len(test_data)))


    train_generator = data_gen_obj.data_generator(train_data,batch_size=6,shuffle=True)

    x,y = next(train_generator)
    print ('x shape: ',x.shape)
    print ('y shape: ',y.shape)
    
    # analyse the first sample
    x_0=x[0]
    y_0=y[0]
    print('x_0 shape: ',x_0.shape)
    print('y_0 shape: ',y_0.shape)
    
    print(Config.labels_to_class)
    activity = Config.labels_to_class[np.argmax(y_0)]
    print(activity)
    
    # plot the first sample
    num_of_images=16
    fig=plt.figure(figsize=(8,8))	
    plt.title("one sample with {} frames ; activity:{}".format(num_of_images,activity))
    subplot_num = int(np.ceil(np.sqrt(num_of_images)))
    for i in range(int(num_of_images)):
        ax = fig.add_subplot(subplot_num, subplot_num, i+1)
        #ax.imshow(output_image[0,:,:,i],interpolation='nearest' ) #to see the first filter
        ax.imshow(x_0[i,:,:,::-1])
        plt.xticks([])
        plt.yticks([])
        plt.tight_layout()
    plt.show()