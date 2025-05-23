from ultralytics import YOLO
import cv2

#load yolo8 model
model = YOLO('yolov8n.pt')

#Load video
video_path = "C:/Users/goyal/Downloads/video.mp4.mp4"
cap = cv2.VideoCapture(video_path)

ret = True

#Read Frames
while ret:
  ret, frame = cap.read()

  if ret:
      # detect objects
      # track objects
      results = model.track(frame, persist=True)

      # plot results
      # cv2.rectangle
      # cv2.putText
      frame_ = results[0].plot()

      # visualize
      cv2.imshow('frame',frame_)
      if cv2.waitKey(25) & 0xFF == ord('q'):
          break
  else:
      break

cap.release()
cv2.destroyAllWindows()