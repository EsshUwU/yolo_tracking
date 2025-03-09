#include <Servo.h>

Servo myServo;

char inChar;
int xValue = 0;
int servoPosition = 90; 
int frameWidth = 640;    

void setup() {
  Serial.begin(9600);
  
  myServo.attach(3);
  
  myServo.write(servoPosition);
}

void loop() {
  if (Serial.available() > 0) {
    inChar = Serial.read();
    
    if (inChar == '\n') {
      xValue = Serial.parseInt();
      
      servoPosition = map(xValue, 0, frameWidth, 0, 180);
      
      servoPosition = constrain(servoPosition, 0, 180);
      
      myServo.write(servoPosition);
      
      while (Serial.available() > 0) {
        Serial.read();
      }
    }
  }
}