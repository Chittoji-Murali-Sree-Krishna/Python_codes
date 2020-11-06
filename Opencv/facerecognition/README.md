# faceRecog.py
>this is the file to recognize the person or photo
# trainFace.py
>this is file to train the model
# labels.pickle
>this is to save the labels for the pictures
# trainer.ynl
>this saves the trained data
## faceRecog.py
```python
# we use recognizer for recognizer to read the tainer
#! we have to give full path so that it wont show up any eroors
#! and this wont work great but if you have good training photos then it will run
#for face detection we use built predifined xml files 
face_cascade = cv2.CascadeClassifier('/home/wargun/Documents/python/opencv/facerecog/cascades/data/haarcascade_frontalface_alt2.xml')
#for the legth and width settings
for(x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        id_, conf = recognizer.predict(roi_gray)
#for accuracy in picture detection
if conf>=4 and conf <= 85:
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2 
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
```
![](images/pic1.jpg?raw=true)
