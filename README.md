Hand Gesture Control with OpenCV and MediaPipe
This project enables volume control and mouse control using hand gestures captured via webcam. It uses MediaPipe for hand tracking, OpenCV for computer vision, pyautogui for controlling mouse/volume, and Tkinter for the UI.

Features
📢 Volume Control
Use the distance between your index finger and thumb to adjust system volume:

Increase Volume: Fingers far apart.

Decrease Volume: Fingers close together.

🖱️ Mouse Control
Use your index finger to move the mouse.
Tap your thumb and index finger together to click.

Requirements
Python 3.x

OpenCV

MediaPipe

PyAutoGUI

Tkinter (usually pre-installed with Python)

Install dependencies using:

bash
Copy
Edit
pip install opencv-python mediapipe pyautogui
How to Run
Save the script as hand_control.py.

Run the script:

bash
Copy
Edit
python hand_control.py
A simple GUI will appear with two options:

Start Volume Control

Start Mouse Control

Select the desired control mode. Press Esc to exit.

File Structure
bash
Copy
Edit
hand_control.py    # Main Python script
README.md          # Project documentation
How It Works
Uses MediaPipe Hands to detect and track hand landmarks in real-time.

Measures the distance between key landmarks (thumb and index finger) to trigger system actions.

Uses pyautogui to simulate keyboard and mouse events.

Known Limitations
Works best in good lighting conditions.

May not support all OS volume systems equally (optimized for Windows/macOS).

Gesture accuracy depends on webcam quality and hand visibility.
