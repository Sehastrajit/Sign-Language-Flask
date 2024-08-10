from flask import Flask, Response, render_template, request, redirect, url_for, session, jsonify, send_file
import cv2
import numpy as np
from ultralytics import YOLO
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

model = YOLO(r'D:\Projects\fast-api-yolo\models\best.pt')
class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

latest_prediction = ""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/background-image')
def serve_image():
    image_path = os.path.join(app.root_path, 'assets', 'image.jpg')
    return send_file(image_path, mimetype='image/jpeg')


def generate_frames():
    global latest_prediction
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        predictions = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                conf = box.conf[0]
                cls = box.cls[0]
                label = class_names[int(cls)]
                predictions.append({
                    "label": label,
                    "confidence": float(conf),
                    "bbox": [float(x1), float(y1), float(x2), float(y2)]
                })
        if predictions:
            latest_prediction = predictions[0]["label"]
        for pred in predictions:
            x1, y1, x2, y2 = map(int, pred["bbox"])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{pred['label']} {pred['confidence']:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_prediction')
def get_prediction():
    global latest_prediction
    return jsonify({"prediction": latest_prediction})

if __name__ == '__main__':
    app.run(debug=True)