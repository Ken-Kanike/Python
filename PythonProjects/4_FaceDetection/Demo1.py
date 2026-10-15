import cv2

# Load the pre-trained face detection model
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize the video capture device (default camera)
video_cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture device
    ret, frame = video_cap.read()

    # Convert the frame to grayscale for face detection
    gray_col = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    face = face_cap.detectMultiScale(
        gray_col,
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30)
    )
    
    # Draw a green box around each detected face in the original frame
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y),(x+w, y+h),(0, 255, 0), 2)
        
    # Convert the original frame to grayscale, but keep the green box
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  # Convert back to BGR for display
    
    # Draw the green box again in the grayscale frame
    for (x, y, w, h) in face:
        cv2.rectangle(gray_frame, (x, y),(x+w, y+h),(0, 255, 0), 2)
    
    # Display the grayscale frame with the green box
    cv2.imshow("video_live", gray_frame)
    
    # Check for the 'a' key press to exit the loop
    if cv2.waitKey(10) == ord("a"):
        break

# Release the video capture device
video_cap.release()









#to on and close camera
# video_cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = video_cap.read()
#     cv2.imshow("video_live",frame)
#     if cv2.waitKey(10) == ord("a"):
#         break
# video_cap.release()