#include <Encoder.h>
#include <TinyGPSPlus.h>
#include <SoftwareSerial.h>

void setup() {
  Serial.begin(9600);

  setupEncoders();
  setupGPS();
}

void loop() {
  updateEncoders();
  updateGPS();
}