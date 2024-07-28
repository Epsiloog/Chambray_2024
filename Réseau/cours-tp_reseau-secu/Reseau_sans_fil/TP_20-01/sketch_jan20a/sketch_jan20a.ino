#include <SPI.h>
#include <RH_RF22.h>
#define SET_RX 1
#define RECEPTION 2
#define PRINT_FRAME 3
#define REPLY 4
#define canal 0
RH_RF22 rf22(SS,9);
uint8_t state;
uint8_t rxbuf[RH_RF22_MAX_MESSAGE_LEN];
uint8_t rxbuflen = RH_RF22_MAX_MESSAGE_LEN;
uint8_t rxlen = RH_RF22_MAX_MESSAGE_LEN;
int rxf = 0;
// the setup routine runs once when you press reset:
void setup() {
Serial.begin(11200);
delay(5000);
SPI.setSCK(14);
if(!rf22.init()){
Serial.println("init failed");
while(1);
}else
Serial.println("init OK");
rf22.setTxPower(RH_RF22_TXPOW_8DBM);
rf22.setModemConfig(RH_RF22::GFSK_Rb125Fd125);
rf22.setFrequency(433.1+canal*0.1, 0.05);
state = SET_RX;
delay(3000);
Serial.println("On to the main loop...");
}
// the loop routine runs over and over again forever:
void loop() {
int j;
rxlen = sizeof(rxbuf);
switch(state){
case SET_RX:
Serial.println("Activating RX mode...");
rf22.setModeRx();
state = RECEPTION;
break;
case RECEPTION:
if(rf22.available()){
state = PRINT_FRAME;
}
break;
case PRINT_FRAME:
if(rf22.recv(rxbuf, &rxlen)){
rxf++;
Serial.printf("[%d]", rxf);
for(j=0; j<rxlen; j++)
Serial.printf("%02x|",rxbuf[j]);
Serial.println();
}
state = SET_RX;
break;
default:
break;
}
}
