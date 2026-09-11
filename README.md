# 🪄 Invisible Cloak using Python & OpenCV

A real-time computer vision project that creates an invisible cloak effect using a webcam, Python, and OpenCV.

## 📌 About the Project

The Invisible Cloak is a computer vision project inspired by the invisibility effect seen in movies.

The program captures the background first and then detects a white-colored cloth in the live webcam feed. The detected area is replaced with the previously captured background, creating the illusion that the cloth has become invisible.

## ✨ Features

- Real-time webcam processing
- White cloth detection
- Automatic background capture
- HSV color-based segmentation
- Image masking
- Noise removal and mask cleaning
- Background replacement
- Real-time invisible effect

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy

## 📁 Project Structure

```text
invisible-cloak/
│
├── main.py
├── requirements.txt
│
├── assets/
│   └── background.jpg
│
└── screenshots
```
## ⚙️ How It Works

The project works in the following steps:

1. The webcam starts and captures the background.
2. The live video is converted from BGR to HSV color space.
3. The white cloak is detected using color segmentation.
4. A mask is created for the detected area.
5. The mask is cleaned to reduce unwanted noise.
6. The detected cloak region is replaced with the captured background.
7. The final invisible cloak effect is displayed in real time.

## ▶️ How to Run

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```
## Run the project

python main.py

## Author

** Sakshi Verma **

Built using Python, OpenCV, and NumPy