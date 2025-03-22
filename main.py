from ultralytics import YOLO
import cv2
import serial
import time

model = YOLO("best.pt")

ser = serial.Serial('COM3', 9600)
time.sleep(2) 

# Create a video capture object
cap = cv2.VideoCapture(0)

last_x = 230  # Start with middle position (assuming 460 is max width)
last_send_time = time.time()

while True:
   ret, frame = cap.read()

   if not ret:
       break
   
   results = model(frame, device="cuda:0", conf=0.7)
   
   found_detection = False
   
   for r in results:
       for box in r.boxes:
           x1, y1, x2, y2 = box.xyxy[0].tolist()

           x = int(x1)
           
           last_x = x
           found_detection = True
           
           print("X val : ",x)
           break  
       
       if found_detection:
           break
   
   current_time = time.time()
   ser.write(f"{last_x}\n".encode())
   last_send_time = current_time
   
   frame_with_boxes = results[0].plot()
   cv2.imshow("YOLOv8 Detection", frame_with_boxes)
   
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
ser.close()

#end