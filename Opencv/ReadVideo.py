import cv2

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

capture = cv2.VideoCapture('full path.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv2.imshow('Video', frame)
    cv2.imshow('Video Resized', frame_resized)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
