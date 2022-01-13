# Building Function that will read videos using opencv and save them as Dataframe on ##outs_dataFrames_Folder
#Importing Libraries


import numpy as np
import cv2
import os



def processing(file_path):
    '''
    Reading the videos from a certain folders and get the frames to store them in another
    folder.

    Parameters:
        videos_folder (str):The folder path that contains the videos.

    Returns:
        None : only reading the videos   
    '''
    dataset1=[]
    images1=[]
    limit1=0
    count1=0

    num_frames=10
    c1=0

    
    cap=cv2.VideoCapture(file_path)
            
    success=True
    while success:
        success,image=cap.read()
        if not success:
            break
               
        image=cv2.resize(image,(100,100))
                
        c1+=1
            
        if image is not None:
            images1.append(np.array(image))
            limit1+=1
            count1+=1
            if limit1==num_frames:
                limit1=0
                dataset1.append(np.array([images1,np.array([1,0])]))
                images1=[]
    X_train = np.array([i[0] for i in dataset1]).reshape(-1, 10, 100, 100, 3)
    print(c1)
    return X_train