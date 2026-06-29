#include <Encoder.h>

// first encoder constants
const int clk_pin1 = 2;
const int dt_pin1 = 3;
const int sw_pin1 = 4;

//second encoder constants

const int clk_pin2 = 5;
const int dt_pin2 = 6;

// third encoder constants

const int clk_pin3 = 7;
const int dt_pin3 = 8;

Encoder rotary1(clk_pin1, dt_pin1);
Encoder rotary2(clk_pin2, dt_pin2);
Encoder rotary3(clk_pin3, dt_pin3);

long last_position1 = 0;
long last_position2 = 0;
long last_position3 = 0;
const int counts_per_click = 4;
bool button_tracker = HIGH;

void encoder_tracker(Encoder &rotary_encoder, long &new_position, long &last_position, const char *cwmessage, const char *ccwmessage) {
  if (new_position >= last_position + counts_per_click) {
    Serial.println(ccwmessage);
    last_position += counts_per_click;
  }

  else if (new_position <= last_position - counts_per_click) {
    Serial.println(cwmessage);
    last_position -= counts_per_click;
  }
}

void setup() {
  Serial.begin(9600);

  pinMode(sw_pin1, INPUT_PULLUP);

  rotary1.write(0);
  rotary2.write(0);
  rotary3.write(0);
  last_position1 = 0;
  last_position2 = 0;
  last_position3 = 0;
}

void loop() {
  long new_position1 = rotary1.read();
  long new_position2 = rotary2.read();
  long new_position3 = rotary3.read();
  bool current_button_state = digitalRead(sw_pin1);
  encoder_tracker(rotary1, new_position1, last_position1, "ENC1_CW", "ENC1_CCW");
  encoder_tracker(rotary2, new_position2, last_position2, "ENC2_CW", "ENC2_CCW");
  encoder_tracker(rotary3, new_position3, last_position3, "ENC3_CW", "ENC3_CCW");

  if (current_button_state == LOW && button_tracker == HIGH) {
    Serial.println("ENC1_PRESS");
  }

  button_tracker = current_button_state;
}