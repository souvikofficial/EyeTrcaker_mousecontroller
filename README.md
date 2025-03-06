# EyeTrcaker_mousecontroller
Eye-Controlled Mouse Using Python and MediaPipe
This project is an innovative eye-tracking mouse control system built with Python, OpenCV, MediaPipe, and PyAutoGUI. It uses your webcam to detect facial landmarks and allows you to control your mouse cursor by moving your eyes — and even click by blinking!

Requirements
Python (3.x)
OpenCV (cv2)
MediaPipe
PyAutoGUI

Install the required libraries with:
pip install opencv-python mediapipe pyautogui

How It Works
Camera Setup:
The script starts by accessing your webcam:
cam = cv2.VideoCapture(0)

Face Landmark Detection:
It uses MediaPipe's FaceMesh to detect facial landmarks:
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

Cursor Movement:
The landmarks around the eyes guide mouse movement. The cursor follows your gaze:
pyautogui.moveTo(screen_x, screen_y)

Blink to Click:
It monitors the vertical distance between two landmarks on the left eye (145 and 159). When you blink (i.e., the distance becomes very small), it simulates a mouse click:
if (left[0].y - left[1].y) < 0.004:
    pyautogui.click()
    pyautogui.sleep(1)

Visual Feedback:
The script displays a live video feed with circles around detected landmarks, helping you see what the program is tracking in real-time.
Usage
Save the script as eye_controlled_mouse.py.

Run the script:
python eye_controlled_mouse.py
Allow camera access when prompted.
Move your eyes to control the cursor.
Blink slowly to click.

Press Ctrl + C in the terminal to exit.

Troubleshooting
Cursor Not Moving: Ensure your face is well-lit and fully visible in the frame.
Click Not Registering: Adjust your blink duration or test with different lighting conditions.
High CPU Usage: Face tracking and video processing are intensive. Close unnecessary apps for better performance.

Future Improvements
Add support for double clicks and right clicks.
Implement scroll gestures.
Fine-tune blink detection for more accuracy
Add multi-face support for collaborative experiences.


