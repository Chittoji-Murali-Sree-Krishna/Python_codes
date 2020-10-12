# opencv 
>we have to import particular frameworks to make it run properly
1. import os
2. import numpy as np
3. import cv2

## to set the video filename and frames and resolution
```python
filename = 'video.avi'
frames_per_seconds = 24.0
resol = '720p'
```
## for different resolutions
```python
STD_DIMENSIONS = {
    "480p":(640, 480),
    "720p":(1280, 720),
    "1080p":(1920, 1080),
}
```
## for video types
```python 
VIDEO_TYPE ={
    'avi':cv2.VideoWriter_fourcc(*'XVID'),
    'mp4':cv2.VideoWriter_fourcc(*'XVID'),
}
```
## for greyscale video types
```python
grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey', grey)
if cv2.waitKey(20) & 0xFF == ord('q'): #this for ending the frame if not it keeps on recording
        break
```
## for RGB
```python
cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'): #this for ending the frame if not it keeps on recording
        break
```
### now we have to destroy all windows after pressing q
cv2.destroyAllWindows()
