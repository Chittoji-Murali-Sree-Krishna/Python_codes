# faceRecog.py
>this is the file to recognize the person or photo
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
# trainFace.py
>this is file to train the model
```python
# we take the entire folder byh using abspath
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")
# here we check the files ending with .jpg or .png and give them labels
if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root, file)
			label = os.path.basename(root).replace(" ", "-").lower()
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id_ = label_ids[label]
# and we have to change the resolution to same for all images if not issues might build up
pil_image = Image.open(path).convert("L")
			size = (550, 550)
			final_image = pil_image.resize(size, Image.ANTIALIAS)
			image_array = np.array(final_image, "uint8")
			#print(image_array)
			faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

# now we append the roi and id_ to train and label
for (x,y,w,h) in faces:
				roi = image_array[y:y+h, x:x+w]
				x_train.append(roi)
				y_labels.append(id_)
# now we use pickle for labels and dump them as file
with open("labels.pickle", 'wb') as f:
	pickle.dump(label_ids, f)
# we use numpy array of labels to train and save them
recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")
```
# labels.pickle
>this is to save the labels for the pictures
# trainer.ynl
>this saves the trained data
# output
![](images/pic1.jpg?raw=true)
