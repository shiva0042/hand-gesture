# 🤚 Hand Gesture Control using OpenCV and MediaPipe

A Python project that allows you to control your **system volume** and **mouse pointer** using **hand gestures** via webcam. Built with **OpenCV**, **MediaPipe**, **PyAutoGUI**, and **Tkinter**.

## 🧠 Features

- 🎚️ **Volume Control**  
  Control system volume by measuring the distance between your **thumb** and **index finger**:
  - Fingers far apart → Volume Up 🔊
  - Fingers close together → Volume Down 🔉

- 🖱️ **Mouse Control**  
  Control the mouse using your **index finger** as a pointer:
  - Move the cursor by moving your finger
  - Click by bringing the **thumb and index finger** close together

## 🛠️ Tech Stack

- [OpenCV](https://opencv.org/) – for video capture and drawing
- [MediaPipe](https://mediapipe.dev/) – for hand tracking
- [PyAutoGUI](https://pyautogui.readthedocs.io/) – for automating keyboard/mouse
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – for simple GUI

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hand-gesture-control.git
   cd hand-gesture-control
2. Install dependencies:
  pip install opencv-python mediapipe pyautogui

3. How to Run:
   python hand_control.py
   
A GUI will appear with two buttons:
              Start Volume Control
              Start Mouse Control
              Press Esc to exit any mode.

