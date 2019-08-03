#include "HX711.h"

// HX711.DOUT  - pin #A1
// HX711.PD_SCK - pin #A0
String buttValue;
String backValue;
HX711 scale(A1, A0);           //setting Arduino Pins
HX711 scale1(A3, A2);
void setup() {
  Serial.begin(38400);
  scale.set_scale(2280.f);              
  scale.tare();               // reset the scale to 0
  scale.read();                // print a raw reading from the ADC
  scale1.set_scale(2280.f);
  scale1.tare();               // reset the scale to 0
  scale1.read();                // print a raw reading from the ADC
}

void loop() {
  //Serial.print(scale.get_units(10), 1);
  buttValue=scale.get_units(10);
  backValue=scale1.get_units(10);
  Serial.println(buttValue+","+backValue);
  scale.power_down();             // put the ADC in sleep mode
  scale1.power_down();
  delay(100);
  scale.power_up();
  scale1.power_up();
}
