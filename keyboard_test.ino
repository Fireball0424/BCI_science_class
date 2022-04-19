#include <SoftwareSerial.h>
char t;

// 輪胎
// 4 左輪往前
// 5 左輪往後
// 6 右輪往前
// 7 右輪往後

void setup() {
  Serial.begin(9600);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop() {
  t = Serial.read();
  
  if (t == '1') {  // Forward        
    digitalWrite(4, HIGH);
    digitalWrite(6, HIGH);
  }

  else if (t == '2') {  // Backward
    digitalWrite(5, HIGH);
    digitalWrite(7, HIGH);
  }

  else if (t == '3') {  // Turn left  
    digitalWrite(6, HIGH);
  }

  else if (t == '4') {  // Turn right  
    digitalWrite(4, HIGH);
  }

  else if (t == '0') { // Stop
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    digitalWrite(7, LOW);
  }

  delay(100);

}
