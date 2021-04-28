# create a video capture
cap = cv2.VideoCapture(0)


def camera_input_color(cap):
    status = ""
    while True:
        # capture frame
        ret, frame = cap.read()

        font = cv2.FONT_HERSHEY_SIMPLEX

        # use putText() method for inserting text on video
        cv2.putText(frame, status, (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)

        color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        # display the frame
        cv2.imshow('frame', color)
        # save the image continuously on local disk
        cv2.imwrite('data/captured_images/c1.jpg', frame)
        # read the image
        captured_img = tf.io.read_file('data/captured_images/c1.jpg')
        # decode the image and store it in a numpy array
        captured_img = decode_img(captured_img).numpy()
        # create a batch
        captured_img = (np.expand_dims(captured_img, 0))
        # predict the image
        prob = model.predict(captured_img)
        # 0.9 can be tuned
        if prob[0][0] > 0.9:
            status = "With mask"
        else:
            status = "No mask"

        # turn off the camera on signal "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def release_camera(cap):
    # release the capture
    cap.release()
    cv2.destroyAllWindows()


camera_input_color(cap)
release_camera(cap)
