import cv2
import mediapipe as mp
import pyautogui
import tkinter as tk

def start_volume_control():
    x1 = y1 = x2 = y2 = 0
    webcam = cv2.VideoCapture(0)
    my_hands = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils

    while True:
        _, image = webcam.read()
        image = cv2.flip(image, 1)
        frame_height, frame_width, _ = image.shape
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        output = my_hands.process(rgb_image)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(image, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                        x1 = x
                        y1 = y
                        print(f"Index finger - X: {x}, Y: {y}")
                    if id == 4:
                        cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                        x2 = x
                        y2 = y
                        print(f"Thumb - X: {x}, Y: {y}")
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)

            if dist > 10:
                print(f"Distance: {dist}")
                pyautogui.press("volumeup")
            else:
                print(f"Distance: {dist}")
                pyautogui.press("volumedown")
        cv2.imshow("Hand Control using Python", image)
        key = cv2.waitKey(10)
        if key == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()

def start_mouse_control():
    capture_hands = mp.solutions.hands.Hands(
        min_detection_confidence=0.5, min_tracking_confidence=0.5)
    drawing_option = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    camera = cv2.VideoCapture(0)
    x1 = y1 = x2 = y2 = 0

    while True:
        _, image = camera.read()
        image_height, image_width, _ = image.shape
        image = cv2.flip(image, 1)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        output_hands = capture_hands.process(rgb_image)
        all_hands = output_hands.multi_hand_landmarks

        if all_hands:
            for hand in all_hands:
                drawing_option.draw_landmarks(image, hand)
                one_hand_landmarks = hand.landmark
                for id, lm in enumerate(one_hand_landmarks):
                    x = int(lm.x * image_width)
                    y = int(lm.y * image_height)
                    if id == 8:
                        mouse_x = int(screen_width / image_width * x)
                        mouse_y = int(screen_height / image_height * y)
                        cv2.circle(image, (x, y), 10, (0, 255, 255))
                        pyautogui.moveTo(mouse_x, mouse_y, duration=0.1)
                        x1 = x
                        y1 = y
                    if id == 4:
                        x2 = x
                        y2 = y
                        cv2.circle(image, (x, y), 10, (0, 255, 255))

            dist = y2 - y1
            if dist < 20:
                pyautogui.click()

        cv2.imshow("Hand movement video capture", image)
        key = cv2.waitKey(1)
        if key == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

def start_program(selected_program):
    if selected_program == "Volume Control":
        start_volume_control()
    elif selected_program == "Mouse Control":
        start_mouse_control()

# Create a simple tkinter window
root = tk.Tk()
root.title("Hand Gesture Control")
root.geometry("300x150")

# Function to start the program
def start_program_button(selected_program):
    start_program(selected_program)

# Create buttons to start different programs
volume_button = tk.Button(root, text="Start Volume Control", command=lambda: start_program_button("Volume Control"))
volume_button.pack()

mouse_button = tk.Button(root, text="Start Mouse Control", command=lambda: start_program_button("Mouse Control"))
mouse_button.pack()

root.mainloop()
