import os
import numpy as np
import cv2

root_dir = 'UCF-101'
dest_dir = 'activity_data'

if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

# To list what are the directories - train, test
data_dir_list = os.listdir(root_dir)

def vid_to_frames():
    for data_dir in data_dir_list: # read the train and test directory one by one
        data_path = os.path.join(root_dir,data_dir) # 'UCF-101/train'
        dest_data_path = os.path.join(dest_dir,data_dir) # 'activity_data/train'
        if not os.path.exists(dest_data_path):
            os.mkdir(dest_data_path)
        
        activity_list = os.listdir(data_path) # thre activity directories ['Archery', 'Basketball', 'Biking']
        
        for activity in activity_list: # loop over every activity folder
            activity_path = os.path.join(data_path,activity) # 'UCF-101/train/Archery'
            dest_activity_path = os.path.join(dest_data_path,activity) # 'activity_data/train/Archery'
            if not os.path.exists(dest_activity_path):
                os.mkdir(dest_activity_path)
            write_frames(activity_path,dest_activity_path)
    
def write_frames(activity_path,dest_activity_path):
    # read the list of video from 'UCF-101/train/Archery' - [v_Archery_g01_c01.avi,v_Archery_g01_c01.avi, ......]
    vid_list = os.listdir(activity_path) 
    for vid in vid_list: # v_Archery_g01_c01.avi
        dest_folder_name = vid[:-4] # v_Archery_g01_c01
        dest_folder_path = os.path.join(dest_activity_path,dest_folder_name) # 'activity_data/train/Archery/v_Archery_g01_c01'
        if not os.path.exists(dest_folder_path):
            os.mkdir(dest_folder_path)
            
        vid_path = os.path.join(activity_path,vid)  # 'UCF-101/train/Archery/v_Archery_g01_c01.avi'
        print ('video path: ', vid_path)
        cap = cv2.VideoCapture(vid_path) # initialize a cap object for reading the video
        
        ret=True
        frame_num=0
        while ret:
            ret, img = cap.read()
            output_file_name = 'img_{:06d}'.format(frame_num) + '.png' # img_000001.png
            # output frame to write 'activity_data/train/Archery/v_Archery_g01_c01/img_000001.png'
            output_file_path = os.path.join(dest_folder_path, output_file_name)
            frame_num += 1
            print("Frame no. ", frame_num)
            try:
                cv2.imshow('img',img)
                cv2.waitKey(5)
                cv2.imwrite(output_file_path, img) # writing frames to defined location
            except Exception as e:
                print(e)
            if ret==False:
                cv2.destroyAllWindows()
                cap.release()
if __name__ == '__main__':
    vid_to_frames()
    
    
