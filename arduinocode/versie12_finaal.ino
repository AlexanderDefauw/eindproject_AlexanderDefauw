//bibliotheek functies 
#include <TinyGPS++.h>
#include "BluetoothSerial.h"
#include <Adafruit_NeoPixel.h>
//variabelen aanmaken
#define RXD2 16
#define TXD2 17
#define GPS_BAUD 9600
#define PIN 14
#define NUMPIXELS 8
TinyGPSPlus gps;
float snelheid;
float latitude;
float longitude;
float gelopen_afstand = 0;
int getal;
String datadoorsturen;
String device_name = "loopmodule1";
String apiKeyValue = "tPmAT5Ab3j7F9";

// checken of bluetooth mogelijk is
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

//check het serial port profiel
#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Port Profile for Bluetooth is not available or not enabled. It is only available for the ESP32 chip.
#endif

//bibliotheken activeren
BluetoothSerial SerialBT;
HardwareSerial gpsSerial(2);
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {


  //serial monitor activeren
  Serial.begin(115200);
  //de GPS module activeren
  gpsSerial.begin(GPS_BAUD, SERIAL_8N1, RXD2, TXD2);
  Serial.println("Serial 2 started at 9600 baud rate");
  //bluetooth activeren
  SerialBT.begin(device_name); 
  SerialBT.deleteAllBondedDevices(); 
  Serial.printf("The device with name \"%s\" is started.\nNow you can pair it with Bluetooth!\n", device_name.c_str());
  pixels.begin();
}

void loop() {
  pixels.clear();
  
  //de gps data opvragen
  KrijgGpsData();
  //de data doorsturen via bluetooth
  SerialBT.println(datadoorsturen);
  //data uitlezen indien nodig
  if (SerialBT.available()) {
    getal = SerialBT.read();
  }
  //de led instellen
  if (getal <=2){
    for(int i=0; i<getal; i++) 
    {    
    pixels.setPixelColor(i, pixels.Color(0, 0, 50));

    pixels.show();
    delay(10);}
  }else if(2 < getal < 6){
    for(int i=0; i<getal; i++) 
    {    
    pixels.setPixelColor(i, pixels.Color(0, 50, 0));

    pixels.show();
    delay(10);}
  }else if(getal == 15){
    gelopen_afstand = 0;
  }else{
    for(int i=0; i<getal; i++) 
    {    
    pixels.setPixelColor(i, pixels.Color(50, 0, 0));

    pixels.show();
    delay(10); }
  }
  pixels.show();
  //kleine delay
  delay(990);
}
void KrijgGpsData() {

  while (gpsSerial.available()) {

    
    if (gps.encode(gpsSerial.read())) {

      snelheid = (gps.speed.kmph());
      gelopen_afstand = gelopen_afstand + snelheid * 0.00027777777;
      latitude = (gps.location.lat());
      
      longitude = (gps.location.lng());
      datadoorsturen =  "&api_key=" + apiKeyValue + "&snelheid=" + snelheid
                          + "&longal=" + String(longitude,6) + "&lann=" + String(latitude,6) + "&afstand=" + gelopen_afstand
                           + "";
    
    }
  }
}
