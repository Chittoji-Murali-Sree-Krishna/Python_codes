> pip install cv2
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
# 2. Readvideo.py
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
 # 3. Basicfunctions.py
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
# to resize the image
imResize = cv2.resize(img,(250,250))
# to crop the image
imCropped = img[0:200,200:500]
# to draw shapes or to write text
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
# for text we have to use cv2 fonts
cv2.putText(img,"Hey Warlord",(300,150),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
```
# 4.Mask.py
>this has some some functions like saturation,hue,val to mask the image, we use trackbars to set the value
```python
# we have to define a empty function
def empty(a):
    pass
# ! check for spellings
# name for the window
cv2.namedWindow('TrackBars')
# size of the window
cv2.resizeWindow('TrackBars', 640, 240)
# hue will be upto 180 in opencv so we take 179, & we need 6 of them for hue_min,max,sat_min,max, val_min,max
cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
# we take this in a loop so that it keeps on updating without exit
while True:
# we need numpy for creating array for the mask
lower = np.array([h_min, s_min, v_min])
upper = np.array([h_max, s_max, v_max])
mask = cv2.inRange(imgHSV, lower, upper)
# for the color mask 
imgResult = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Result', imgResult)
```
# 5.facerecognition
>this is a basic face recognition, it wont be as accurate as ai based stuff but it can keep up if the training data is proper
>this just a basic stuff which takes the folder name as labels and images inside the folder for recognition


![facerecog](https://user-images.githubusercontent.com/62329524/104125097-7aee7580-534c-11eb-886c-0c10bd194399.jpg)
