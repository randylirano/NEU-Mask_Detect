from flask import Flask, render_template, Response, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

import cv2
import os

import tensorflow as tf
import numpy as np

app = Flask(__name__)
cors = CORS(app)


app.config['CORS_HEADERS'] = 'Content-Type'

camera = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

# convert an image file to an array
def decode_img(img):
    # https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg
    # please see the above link for the following function: tf.image.decode_jpeg
    img = tf.image.decode_jpeg(img, channels=3)
    # uniform the picture size, this parameter can be changed
    return tf.image.resize(img, [100, 100])

def process_frame():  # generate frame by frame from camera
    model = tf.keras.models.load_model("model_save")
    status = ""
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame

        if not success:
            break
        else:
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Use putText() method for
            # inserting text on video
            cv2.putText(frame, status,(50, 50),font, 1,(0, 255, 255),2, cv2.LINE_4)

            color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)


            # save the image continuously on local disk
            cv2.imwrite('data/captured_images/c1.jpg', frame)

            # read the image
            captured_img = tf.io.read_file('data/captured_images/c1.jpg')

            # decode the image and store in a numpy array
            captured_img = decode_img(captured_img).numpy()

            # Create a batch
            captured_img = (np.expand_dims(captured_img, 0))

            # predict the image
            prob = model.predict(captured_img)

            # 0.9 can be tuned
            if prob[0][0] > 0.9:
                status = "With mask"
            else:
                status = "No mask"

            ret, buffer = cv2.imencode('.jpg', frame)
            images = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + images + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def getVideo():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(process_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/uploader', methods = ['GET', 'POST'])
@cross_origin()
def upload_file():
    result = {}
    model = tf.keras.models.load_model("model_save")
    f = request.files['file']
    sfname = 'data/captured_images/'+str(secure_filename(f.filename))
    f.save(sfname)
    # filename = 'c1.jpg'
    tf_file = tf.io.read_file(os.path.join("data/captured_images", str(secure_filename(f.filename))))
    img = decode_img(tf_file).numpy()
    img = (np.expand_dims(img, 0))

    prob = model.predict(img)
    if prob[0][0] > 0.9:
        status = "With mask"
    else:
        status = "No mask"
    result["status"] = status
    return result

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(video_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

# This was to test api call with Flask and an html template
# @app.route('/upload')
# @cross_origin()
# def upload():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
