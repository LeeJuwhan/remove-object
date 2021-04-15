import numpy as np
from PIL import Image
import cv2 as cv2
import os
def remove_obj(video_frame):
    # Load images

    # im0 = np.array(Image.open('1.jpg'))
    # im1 = np.array(Image.open('2.jpg'))
    # im2 = np.array(Image.open('3.jpg'))

    # Stack the 3 images into a 4d sequence
    sequence = video_frame[0]
    results = video_frame[0]
    for i in range(len(video_frame)-2):
        print(i)
        print(sequence.shape)
        print(video_frame[i+1].shape)
        sequence = np.stack((sequence, video_frame[i+1]), axis=3)
        result = np.median(sequence, axis=3).astype(np.uint8)
        sequence = result
        results = result
    

    # Save to disk
    Image.fromarray(results).save('result.png')




def video2image(input_path):
    count = 0
    
    list_dir = os.listdir(input_path)

    # vidcap = cv2.VideoCapture(input_path + list_dir[0])
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
            
            # cv2.imwrite("./output/" + "%d.png" % count, image)
            video_frame[count] = image            
            # print('Saved frame%d.jpg' % count)
            count += 1
            #for bandicam cut 4 sec
            # if(int(vidcap.get(1)) >= v_length -int(v_fps * 4)):
            if(int(vidcap.get(1)) >= v_length-1):
                vidcap.release()

    vidcap.release()
    print(len(video_frame))
    
    return video_frame
    
video_frame = video2image("./input/")

remove_obj(video_frame)

