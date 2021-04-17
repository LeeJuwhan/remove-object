import numpy as np
from PIL import Image
import cv2 as cv2
import os
from matcher import stackImagesKeypointMatching
def remove_obj(video_frame):
    
    sequence = video_frame[0]
    results = video_frame[0]
    
    
    
    for i in range(len(video_frame)-2):        
        sequence = np.stack((sequence, video_frame[i+1]), axis=3)
        result = np.median(sequence, axis=3).astype(np.uint8)
        sequence = result
        results = result
    
    # Save to disk
    Image.fromarray(results).save('result.png')




def video2image(input_path):
    count = 0
    
    list_dir = os.listdir(input_path)

    
    fname = list_dir[0]
    vidcap = cv2.VideoCapture(input_path + fname)

    # FPS you want
    fps = 30
    
    # to get fps of video
    v_fps = vidcap.get(cv2.CAP_PROP_FPS)
    v_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    video_frame = [0 for i in range(v_length)]

    r = int(v_fps)/fps
    print(v_fps)
    
    #print(r)
    # s_time = time.time()
    print(v_length)
    
    while (vidcap.isOpened()):
        ret, image = vidcap.read()        
        
        
        # if (int(vidcap.get(1)) % int(v_fps) == 0):
        if (int(vidcap.get(1))):
            # l_time = time.time()
            
            
            video_frame[count] = image            
            
            count += 1
            
            #for bandicam cut 4 sec
            # if(int(vidcap.get(1)) >= v_length -int(v_fps * 4)):
            if(int(vidcap.get(1)) >= v_length-1):
                vidcap.release()

    vidcap.release()
    print(len(video_frame))
    
    return video_frame


def main():
    video_frame = video2image("./input/")    
    remove_obj(video_frame)

if __name__ == "__main__":    
    main()

