#include "DFRobot_PH.h"
#include <EEPROM.h>

#define PH_PIN A1
float voltage, phValue, temperature = 25;
DFRobot_PH ph;

void setup()
{
    Serial.begin(115200);  
    ph.begin();
}

void loop()
{
    static unsigned long timepoint = millis();
    if (millis() - timepoint > 10000U) {
        timepoint = millis();
        voltage = analogRead(PH_PIN) / 1024.0 * 5000;  // Read analog voltage
        phValue = ph.readPH(voltage, temperature);     // Convert to pH
        Serial.print("temperature:");
        Serial.print(temperature, 1);
        Serial.print("^C  pH:");
        Serial.println(phValue, 2);
    }
    ph.calibration(voltage, temperature);              // Optional: serial calibration
}
