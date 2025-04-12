// Define LED pins
const int RED_PIN = 4;     // Red LED on pin 4
const int YELLOW_PIN = 3;  // Yellow LED on pin 3
const int GREEN_PIN = 2;   // Green LED on pin 2

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(YELLOW_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();

    // Turn off all LEDs as baseline
    digitalWrite(RED_PIN, LOW);
    digitalWrite(YELLOW_PIN, LOW);
    digitalWrite(GREEN_PIN, LOW);

    // Set LED states based on command
    switch (cmd) {
      case 'R':  // 1 Finger → Only Red LED ON
        digitalWrite(RED_PIN, HIGH);
        break;
      case 'Y':  // 2 Fingers → Only Yellow LED ON
        digitalWrite(YELLOW_PIN, HIGH);
        break;
      case 'G':  // 3 Fingers → Only Green LED ON
        digitalWrite(GREEN_PIN, HIGH);
        break;
      case 'A':  // Open Hand → All LEDs ON
        digitalWrite(RED_PIN, HIGH);
        digitalWrite(YELLOW_PIN, HIGH);
        digitalWrite(GREEN_PIN, HIGH);
        break;
      case 'O':  // Fist → All LEDs OFF
      default:
        // All LEDs remain off
        break;
    }
  }
}
