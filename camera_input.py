import cv2

cap = cv2.VideoCapture(0)

def camera_input_gray(cap):
    while True:
        # Capture frame
        ret, frame = cap.read()
        # Convert the frame to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the frame
        cv2.imshow('frame', gray)
        # Turn off the camera on signal
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def camera_input_color(cap):
    while True:
        # Capture frame
        ret, frame = cap.read()
        # Convert the frame array
        color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        # Display the frame
        cv2.imshow('frame', color)
        # Turn off the camera on signal
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def release_camera(cap):
    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

camera_input_gray(cap)
release_camera(cap)
