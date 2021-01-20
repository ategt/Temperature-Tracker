/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  int sensorValues[10] = {analogRead(A0),
                          analogRead(A0),
                          analogRead(A0),
                          analogRead(A0),
                          analogRead(A0),
                          analogRead(A0),
                          analogRead(A0),
                          analogRead(A0),
                          analogRead(A0),
                          analogRead(A0)};

  // print out the value you read:
  Serial.print(sensorValue);
  Serial.print(",");

  int cum = 0;

  for (int x=0;x<10;x=x+1) {
      Serial.print(sensorValues[x]);
      Serial.print(",");
      cum += sensorValues[x];
    }
  
  Serial.println(cum/10);
  
  delay(1000);        // delay in between reads for stability
}
