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
    for data_dir in data_dir_list:
        data_path = os.path.join(root_dir,data_dir)
        dest_data_path = os.path.join(dest_dir,data_dir)
        if not os.path.exists(dest_data_path):
            os.mkdir(dest_data_path)
        
        activity_list = os.listdir(data_path)
        
        for activity in activity_list:
            activity_path = os.path.join(data_path,activity)
            dest_activity_path = os.path.join(dest_data_path,activity)
            if not os.path.exists(dest_activity_path):
                os.mkdir(dest_activity_path)
            write_frames(activity_path,dest_activity_path)
    
def write_frames(activity_path,dest_activity_path):
    vid_list = os.listdir(activity_path)
    for vid in vid_list:
        dest_folder_name = vid[:-4]
        dest_folder_path = os.path.join(dest_activity_path,dest_folder_name)
        if not os.path.exists(dest_folder_path):
            os.mkdir(dest_folder_path)
            
        vid_path = os.path.join(activity_path,vid)
        print ('video path: ', vid_path)
        cap = cv2.VideoCapture(vid_path)
        
        ret=True
        frame_num=0
        while ret:
            ret, img = cap.read()
            output_file_name = 'img_{:06d}'.format(frame_num) + '.png'
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
    
    
