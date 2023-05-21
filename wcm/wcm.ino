char command;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    command = Serial.read();

    switch (command) {
      case 'w':
        Serial.println("Moving forward");
        // Forward command logic
        break;

      case 'a':
        Serial.println("Moving left");
        // Left command logic
        break;

      case 'd':
        Serial.println("Moving right");
        // Right command logic
        break;

      case 's':
        Serial.println("Moving backward");
        // Backward command logic
        break;

      default:
        Serial.println("Invalid command");
        // Invalid command logic
        break;
    }

  }

  Serial.println("waiting");
}
