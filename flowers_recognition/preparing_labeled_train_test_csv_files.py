#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
import random

import cv2
import os


# ### 1. Preparing training and test csv files

# In[5]:


root_dir = r'D:\Trainings-2019\custom_data_generator\flowers_recognition' #The r means that the string is to be treated as a raw string, which means all escape codes will be ignored.

data_folder = 'flowers_renamed'
data_path = os.path.join(root_dir,data_folder)
data_dir_list = os.listdir(data_path)
print ('the data list is: ',data_dir_list)


# In[6]:


# Assigning labels to each flower category
num_classes = 5
labels_name={'daisy':0,'dandelion':1,'rose':2,'sunflower':3,'tulip':4}


# In[7]:


# create two dataframes one for train and other for test with 3 columns as filename,label and classname
train_df = pd.DataFrame(columns=['FileName', 'Label', 'ClassName'])
test_df = pd.DataFrame(columns=['FileName', 'Label', 'ClassName'])

#number of images to take for test data from each flower category
num_images_for_test = 60

# Here data_dir_list = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
# Loop over every flower category
for dataset in data_dir_list:
    # load the list of image names in each of the flower category
    img_list = os.listdir(os.path.join(data_path,dataset))
    print ('Loading the images of dataset-'+'{}\n'.format(dataset))
    label = labels_name[dataset]
    num_img_files = len(img_list)
    num_corrupted_files=0
    test_list_index = random.sample(range(1, num_img_files-1), num_images_for_test)
    
    # read each file and if it is corrupted exclude it , if not include it in either train or test data frames
    for i in range(num_img_files):
        img_name = img_list[i]
        img_filename = os.path.join(data_path,dataset,img_name)
        try:
            input_img = cv2.imread(img_filename)
            img_shape=input_img.shape
            if i in test_list_index:
                test_df = test_df.append({'FileName': img_filename, 'Label': label,'ClassName': dataset},ignore_index=True)
            else:
                train_df = train_df.append({'FileName': img_filename, 'Label': label,'ClassName': dataset},ignore_index=True)       
        except:
            print ('{} is corrupted\n'.format(img_filename))
            num_corrupted_files+=1
    
    
    
    print ('Read {0} images out of {1} images from data dir {2}\n'.format(num_img_files-num_corrupted_files,num_img_files,dataset))

print ('completed reading all the image files and assigned labels accordingly')


# In[8]:


if not os.path.exists('data_files'):
    os.mkdir('data_files')

train_df.to_csv('data_files/flowers_recognition_train.csv')
test_df.to_csv('data_files/flowers_recognition_test.csv')
print('The train and test csv files are saved')


# ### save the labels in a file as well

# In[10]:


import pickle as pkl

with open('data_files/label_map.pkl', 'wb') as handle:
    pkl.dump(labels_name, handle, protocol=pkl.HIGHEST_PROTOCOL)

#with open('filename.pickle', 'rb') as handle:
#    b = pickle.load(handle)

#print a == b


# In[ ]:




