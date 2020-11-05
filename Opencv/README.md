# 1.CaptureVideo.py
>this for recording video
```python 
# to set the video filename and frames and resolution
filename = 'video.avi'
frames_per_seconds = 24.0
resol = '720p'
# for frame height and width
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# for different resolutions
STD_DIMENSIONS = {
    "480p":(640, 480),
    "720p":(1280, 720),
    "1080p":(1920, 1080),
}
# for video types 
VIDEO_TYPE ={
    'avi':cv2.VideoWriter_fourcc(*'XVID'),
    'mp4':cv2.VideoWriter_fourcc(*'XVID'),
}
# for greyscale video types
grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey', grey)
if cv2.waitKey(20) & 0xFF == ord('q'): #this for ending the frame if not it keeps on recording
        break
# for RGB
cv2.imshow('frame', frame)
if cv2.waitKey(20) & 0xFF == ord('q'): #this for ending the frame if not it keeps on recording
break
# now we have to destroy all windows after pressing q
cv2.destroyAllWindows()
```
# 2.ReadImages.py
>for reading the images 
```python
cv2.imread('full path of image')
cv2.imshow('Image', img)
```
# 3. Readvideo.py
>for reading the video
```python
# for rescaling the video
def rescaleFrame(frame, scale=0.75): # 0.75 means video will be 75% of its resolution
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

# for reading the videos we use VideoCapture
capture = cv2.VideoCapture('full path for the image') 
while True:
    #checking the frames to read
    isTrue, frame = capture.read()
    # for the resized frame
    frame_resized = rescaleFrame(frame)
    # this is to show the video
    cv2.imshow('Video', frame)
    # this is to show resized frame
    cv2.imshow('Video Resized', frame_resized)
    # we wait 20sec or exit by pressing q
    if cv2.waitKey(20) & 0xFF==ord('q'): 
        break
 #we have to release the frames
 capture.release() 
 ```
 # 4. Basicfunctions.py
 >these are few basic functions of opencv
 ```python
 # kernel for uint8
 kernel = np.ones((5,5),np.uint8)
 # will convert it to greyscale
imGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# will convert to blur
imBlur = cv2.GaussianBlur(imGrey,(11,11),0)
# for canny image
imCanny = cv2.Canny(img, 150, 200)
# here we need numpy for special readings
# for dilate image
imDialation = cv2.dilate(imCanny, kernel, iterations=1)
# for erode image
imEroded = cv2.erode(imDialation, kernel, iterations=1)
