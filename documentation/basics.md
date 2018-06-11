The Mindflextoy lets you read different ranges of concentration. Basically, We take advantage of the EEG module od the toy. Of we open it, we can easily see the GND (ground) and TX pins, so our job here is to welding a couple of wires, ones to the GND and another one to the TX. Next is to take our arduino (Only works for me in Arduino Uno, Nano even tho has TX/RX pins, gets very hot).

![](https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fmarkjobes.com%2Fwp-content%2Fuploads%2F2012%2F11%2FMFHackDetail0.jpg&f=1)

We connect the GND to the Arduino namesake pin, and the TX to the RX, be careful tho, connect it AFTER uploading the program with the Arduino IDE, otherwise it will give an error. On the other hand, we must connect the heart-rate arduino devide. In my case I'm using this one providad to me by DFROBOT for experimenting https://www.dfrobot.com/product-1540.html .

This is the code for the heart rate monitor connected to the analog pin A1:

```
//THE ANALOG PIN FOR HEART RATE
const int heartPin = A1;

void setup() {
 Serial.begin(115200);
 pinMode(vib, OUTPUT);
}

void loop() {
 int heartValue = analogRead(heartPin);
//printing for seeing the values at the computer, can be erased afterwards
 Serial.println(heartValue);
 delay(500);

//I use 800 for my own alarm, set your heart-rate alarm as you wish
 if (heartValue < 300){
    //send command for sleeping alert
     delay (1000);
 }
}
```
