void setup() {
  Serial.begin(115200);           // Start serial communication at 115200 baud
  while (!Serial);                // Wait for serial port to connect (good for Leonardo-type boards)
  Serial.println("Serial test started...");
}

void loop() {
  Serial.println("Hello from Arduino!");
  delay(1000);  // wait for 1 second
}
