#include "Adafruit_VEML7700.h"

Adafruit_VEML7700 veml = Adafruit_VEML7700();

void setup() {
  Serial.begin(9600);
  while (!Serial) { delay(10); }

  if (!veml.begin()) {
    while (1);
  }

  // == OPTIONAL =====
  // Can set non-default gain and integration time to
  // adjust for different lighting conditions.
  // =================
  veml.setGain(VEML7700_GAIN_2);
  veml.setIntegrationTime(VEML7700_IT_800MS);

  veml.setLowThreshold(10000);
  veml.setHighThreshold(20000);
  veml.interruptEnable(true);
}

void loop() {
  Serial.println(veml.readWhite());
  delay(1000);
 }
