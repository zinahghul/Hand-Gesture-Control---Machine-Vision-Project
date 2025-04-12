import cv2
import mediapipe as mp
import serial
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize Serial Communication with Arduino (update COM port if needed)
arduino = serial.Serial('COM4', 9600)
time.sleep(2)  # Allow time for Arduino to reset

# Start Video Capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open camera.")
    exit()

def send_command(cmd):
    arduino.write(cmd.encode())

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Mirror the frame and convert to RGB for MediaPipe processing
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        # Default: Fist → All LEDs OFF ("O")
        command = "O"
        label = "Fist (All OFF)"
        label_color = (255, 255, 255)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = hand_landmarks.landmark

                # Finger tip landmarks for index, middle, ring, and pinky: indices 8, 12, 16, 20.
                # A finger is considered "extended" if its tip's y-value is greater than its PIP joint (tip index - 2)
                finger_tips = [8, 12, 16, 20]
                extended = 0
                for tip in finger_tips:
                    if landmarks[tip].y > landmarks[tip - 2].y:
                        extended += 1

                # Mapping based on the number of extended fingers:
                if extended == 4:
                    command = "O"
                    label = "Fist (All LEDS ON)"
                    label_color = (200, 200, 200)
                elif extended == 1:
                    command = "R"
                    label = "1 Finger (Red LED OFF)"
                    label_color = (0, 0, 255)
                elif extended == 2:
                    command = "Y"
                    label = "2 Fingers (Yellow LED OFF)"
                    label_color = (0, 255, 255)
                elif extended == 3:
                    command = "G"
                    label = "3 Fingers (Green LED OFF)"
                    label_color = (0, 255, 0)
                elif extended == 0:
                    command = "A"
                    label = "Open Hand (All LEDs OFF)"
                    label_color = (255, 255, 255)

                cv2.putText(frame, label, (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, label_color, 2)

        send_command(command)
        cv2.imshow("Hand Gesture LED Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted by user.")
finally:
    cap.release()
    cv2.destroyAllWindows()
    arduino.close()
