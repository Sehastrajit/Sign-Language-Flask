# YOLO Sign Language Detection

## Overview
This project implements a real-time sign language detection system using the YOLO (You Only Look Once) object detection algorithm. It can accurately recognize and interpret American Sign Language (ASL) alphabet signs through a live video feed. The system is built with a web interface for easy interaction and accessibility.

## Features
- Real-time ASL alphabet sign detection using a webcam
- Custom-trained YOLO model for accurate sign recognition
- Web-based interface built with Flask
- Secure login system
- Responsive design for cross-device compatibility

## Prerequisites
- Python 3.7+
- OpenCV
- PyTorch
- Flask
- Ultralytics YOLO

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/yolo-sign-language-detection.git
   cd yolo-sign-language-detection
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Download the pre-trained YOLO model:
   - Place the `best.pt` file in the `models` directory.

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`.

3. Log in using the default credentials:
   - Username: admin
   - Password: password

4. Allow access to your webcam when prompted.

5. Start signing using ASL alphabet signs in front of your webcam. The system will detect and display the recognized signs in real-time.

## Project Structure
```
Sign-Language-Flask/
├── assets/
│   └── image.jpg
├── models/
│   └── best.pt
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   └── login.html
├── app.py
├── requirements.txt
└── README.md
```

## Model Training
The YOLO model (best.pt) used in this project was custom-trained on a dataset of ASL alphabet signs. The training process involved:
1. Collecting and annotating images of ASL alphabet signs
2. Configuring the YOLO model for the specific detection task
3. Training the model using the Ultralytics YOLO implementation
4. Fine-tuning the model for optimal performance

## Contributing
Contributions to improve the project are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements
- [Ultralytics YOLO](https://github.com/ultralytics/yolov5)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [PyTorch](https://pytorch.org/)

## Contact
Sehastrajit - sehastrajit@gmail.com

Project Link: [(https://github.com/Sehastrajit/Sign-Language-Flask)](https://github.com/Sehastrajit/Sign-Language-Flask)
