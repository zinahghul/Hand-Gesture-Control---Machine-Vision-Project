🤖 Hand Gesture LED Controller


https://github.com/user-attachments/assets/8458acad-9c12-46c1-903a-9236b5aad50c

Control Arduino LEDs using real-time hand gesture detection with MediaPipe and OpenCV.

🔧 Hardware
Arduino Uno

LEDs: Red (Pin 4), Yellow (Pin 3), Green (Pin 2)

Resistors (220–330Ω), Breadboard, Jumper Wires

Webcam

✋ Gesture Mapping
Gesture	LED Action
Fist	All LEDs OFF
1 Finger	Red LED ON
2 Fingers	Yellow LED ON
3 Fingers	Green LED ON
Open Hand	All LEDs ON
🖥️ Setup
Install dependencies:

bash
Copy code
pip install opencv-python mediapipe pyserial
Upload the Arduino sketch.

Update the COM port in handgesturecontrol.py.

Run the Python script:

bash
Copy code
python handgesturecontrol.py
📂 Files
handgesturecontrol.py — Python script for gesture recognition

arduino_code.ino — Arduino sketch for LED control
