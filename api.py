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

 # use 0 for web camera (or look at OpenCV documentation for cctv input)
camera = cv2.VideoCapture(0)

# Helper function for process_frame
def decode_img(img):
    # https://www.tensorflow.org/api_docs/python/tf/io/decode_jpeg
    # please see the above link for the following function: tf.image.decode_jpeg
    img = tf.image.decode_jpeg(img, channels=3)
    # uniform the picture size, this parameter can be changed
    return tf.image.resize(img, [100, 100])

# Helper function for video_feed that generate frame by frame from camera
def process_frame():

    #retrieve model from Python team
    model = tf.keras.models.load_model("model_save")
    status = ""
    while True:
        # Capture frame-by-frame from camera
        success, frame = camera.read()

        if not success:
            break
        else:
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Use putText() method for inserting text on video
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

            #convert image format to streaming data for network transmission
            ret, buffer = cv2.imencode('.jpg', frame)
            images = buffer.tobytes()

            #Keep generating the frame as image is sent to frontend
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + images + b'\r\n')  # concat frame one by one and show result

# Endpoint for livestream feature
@app.route('/video_feed')
def getVideo():
    #Returns a stream of images that can be displayed on a web page with multipart responses
    return Response(process_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Endpoint for upload image feature
@app.route('/uploader', methods = ['GET', 'POST'])
@cross_origin()
def upload_file():

    result = {}

    #retrieve model from Python team
    model = tf.keras.models.load_model("model_save")

    # Access uploaded file from files dictionary in request object
    f = request.files['file']

    # Save filename to local
    file_name = 'data/captured_images/'+str(secure_filename(f.filename))
    f.save(file_name)

    # read the image
    tf_file = tf.io.read_file(os.path.join("data/captured_images", str(secure_filename(f.filename))))

    # decode the image and store in a numpy array
    img = decode_img(tf_file).numpy()

    # Create a batch
    img = (np.expand_dims(img, 0))

    # predict the image and return prediction
    prob = model.predict(img)
    if prob[0][0] > 0.9:
        status = "With mask"
    else:
        status = "No mask"
    result["status"] = status

    return result

# This was to test api call with Flask and an html template in templates folder
# @app.route('/upload')
# @cross_origin()
# def upload():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
