#include "HX711.h"

String x;
String y;
HX711 scale(A1, A0);    // parameter "gain" is ommited; the default value 128 is used by the library
HX711 scale1(A3, A2);
void setup() {
  Serial.begin(38400);
  scale.set_scale(2280.f);                     // this value is obtained by calibrating the scale with known weights; see the README for details
  scale.tare();               // reset the scale to 0
  scale.read();                // print a raw reading from the ADC
  scale1.set_scale(2280.f);
  scale1.tare();
  scale1.read();
}

void loop() {
  x=scale.get_units(10);
  y=scale1.get_units(10);
  Serial.println(x+","+y);
  scale.power_down();             // put the ADC in sleep mode
  scale1.power_down();
  delay(100);
  scale.power_up();
  scale1.power_up();
}
