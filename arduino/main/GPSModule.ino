#include <TinyGPSPlus.h>
#include <SoftwareSerial.h> 

static const int GPS_TX_Pin = A0, GPS_RX_Pin = A1;

static const uint32_t GPSBaud = 9600;   

TinyGPSPlus gps;

SoftwareSerial GPS(GPS_TX_Pin, GPS_RX_Pin);    
void setupGPS() {
  GPS.begin(9600);
}

void updateGPS() {
  while (GPS.available() > 0) {
    gps.encode(GPS.read());
  }

  static unsigned long lastPrintTime = 0;

  if (millis() - lastPrintTime >= 1000) {
    lastPrintTime = millis();

    if (gps.location.isValid()) {
      Serial.print("LOCATION_DATA:");
      Serial.print("(");
      Serial.print(gps.location.lat(), 6);

      Serial.print(",");
      Serial.print(gps.location.lng(), 6);
      Serial.print(")");

      Serial.println();
    }
    else {
      Serial.println("NO_SIGNAL");
    }
  }
}