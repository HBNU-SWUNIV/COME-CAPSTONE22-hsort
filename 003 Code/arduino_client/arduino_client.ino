#include "ESP8266.h"
#include <SoftwareSerial.h>
#include <string.h>

#define SSID        "Asd"  
#define PASSWORD    "12qwaszx!"  
#define HOST_NAME   "192.168.43.241" 
#define HOST_PORT   5000

SoftwareSerial mySerial(7, 6);
ESP8266 wifi(mySerial);
bool flag = false;
bool APConnected = false;
bool TCPConnected = false;

int read_first_sensor() {
  float volt1 = analogRead(A0) * 5 / 1023;
  int distance1 = 65 * pow(volt1, -1.10);

  return distance1;
}

int read_second_sensor() {
  float volt2 = analogRead(A5) * 3.3 / 746;
  int distance2 = 65 * pow(volt2, -1.165);

  return distance2;
}

void send_pass_signal(int n) {
  if (n == 1) {  
    uint8_t buf[]="pass1";
    wifi.send(buf, strlen(buf));
  }
  else {
    uint8_t buf[]="pass2";
    wifi.send(buf, strlen(buf));
  }
}

void receive_id() {
  uint8_t buffer[128] = {0};
  int cnt = 0;

  while (true) {
    if (cnt == 1000) {
      uint8_t buf[]="pass1";
      wifi.send(buf, strlen(buf));
      Serial.print("cnt : ");
      Serial.println(cnt);
      cnt = 0;
    }

    uint32_t len = wifi.recv(buffer, sizeof(buffer), 32);
    if (len > 0) {
      Serial.print("Received:[");
      for(uint32_t i = 0; i < len; i++) {
        Serial.print((char)buffer[i]);
      }
      Serial.print("]\r\n");

      uint8_t buf[]="receive id";
      wifi.send(buf, strlen(buf));

      break;
    }
    else { cnt++; }

    delay(200);
  }
}

void connectAP() {
  Serial.print("FW Version:");
  Serial.println(wifi.getVersion().c_str());
    
  if (wifi.setOprToStationSoftAP()) {
      Serial.print("to station + softap ok\r\n");
  } else {
      Serial.print("to station + softap err\r\n");
  }

  while(APConnected == false) {
    if (wifi.joinAP(SSID, PASSWORD)) {
        Serial.print("Join AP success\r\n");
        Serial.print("IP:");
        Serial.println( wifi.getLocalIP().c_str());
        APConnected = true;       
    } else {
        Serial.print("Join AP failure\r\n");
    }
  }
  
  if (wifi.disableMUX()) {
      Serial.print("single ok\r\n");
  } else {
      Serial.print("single err\r\n");
  }
}

void connectTCP() {
  while(TCPConnected == false){
    if (wifi.createTCP(HOST_NAME, HOST_PORT)) {

      uint8_t buf[]="arduino";
      wifi.send(buf, strlen(buf));
      while(true) {
        uint8_t buffer[128] = {0};
        uint32_t len = wifi.recv(buffer, sizeof(buffer), 32);
        char* s;

        if (len > 0) {
          Serial.print("Received:[");
          for(uint32_t i = 0; i < len; i++) {
            Serial.print((char)buffer[i]);
            s[i] = (char)buffer[i];
          }
          Serial.print("]\r\n");
          s = (char*)buffer;

          if (strcmp(s, "check") == 0) {
            uint8_t buf[]="check";
            wifi.send(buf, strlen(buf));
            TCPConnected = true;
            Serial.print("create tcp ok\r\n");
            break;
          }
        }
      }
      
    } else {
      Serial.print("create tcp err\r\n");
    }
    delay(100);
  }
}

void setup(void)
{
  Serial.begin(9600);
  Serial.println();
  connectAP();
  connectTCP();
  Serial.println("start");
}

void loop(void)
{

  // measure distance sensor1
  int distance1 = read_first_sensor();
  if ((0 < distance1) and (distance1 < 75)) {
  // if (true) {
    Serial.println("pass1");
    send_pass_signal(1);
    flag = true;
    // waiting rfid reader
    receive_id();
  }

  // measure distance sensor2
  while (flag) {
    int distance2 = read_second_sensor();
    if ((0 < distance2) and (distance2 < 50)) {
      Serial.println("pass2");
      send_pass_signal(2);
      flag = false;
    }
  }
  
  // { // check release tcp
  //   if (wifi.releaseTCP()) {
  //       Serial.print("release tcp ok\r\n");
  //   } else {
  //       Serial.print("release tcp err\r\n");
  //       isConnected = false;
  //       connectTCP();
  //   }
  // }
  delay(500);
}