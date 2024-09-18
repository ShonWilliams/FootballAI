from ultralytics import YOLO
import cv2

model = YOLO('best (1).pt')

video_path = '1minSegment.mp4'
cap = cv2.VideoCapture(video_path)

def resize_frame(frame, percent=50):
    width = int(frame.shape[1] * 50 /100)
    height = int(frame.shape[0] * 50/100)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation= cv2.INTER_AREA)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        frame50 = resize_frame(annotated_frame,percent=50)
        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", frame50)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()