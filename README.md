🤖 Hand Gesture LED Controller
Control Arduino LEDs using real-time hand gesture detection with MediaPipe and OpenCV.

🔧 Hardware
Arduino Uno

LEDs: Red (Pin 4), Yellow (Pin 3), Green (Pin 2)

Resistors (220–330Ω), Breadboard, Jumper Wires

Webcam

✋ Gesture Mapping
Gesture	Action
Fist	All LEDs OFF
1 Finger	Red LED ON
2 Fingers	Yellow LED ON
3 Fingers	Green LED ON
Open Hand	All LEDs ON
🖥️ Setup
bash
Copy code
pip install opencv-python mediapipe pyserial
Upload Arduino sketch

Update COM port in script.py

Run the Python script

bash
Copy code
python handgesturecontrol.py
📂 Files
handgesturecontrol.py: Python gesture controller

arduino_code.ino: Arduino LED handler
