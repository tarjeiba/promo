"""
A module to provide real-time logging of physical properties based on equipment
connected to an Arduino board.


The Arduino should be running the following code:
`
int trigPin = 13; //Sensor Trig pin connected to Arduino pin 13
int echoPin = 11;  //Sensor Echo pin connected to Arduino pin 11
unsigned long pingTime;  //time for ping to travel from sensor to target and return
int chosenInt, delayTime, totalTime;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.println("Arduino ready."); 
} 

void loop() {
	delayTime = totalTime = chosenInt = -1;

	getValue(&delayTime, "Received delay time.");
	getValue(&totalTime, "Received total time.");
	getValue(&chosenInt, "Received chosen program.");

	delay(delayTime);

	switch(chosenInt) {
	case 1 :
		pingTimer();
		break;
	default:
		Serial.println("Not a valid program choice.");
	}
	

	if (chosenInt == 1) {
    pingTimer();
  } else {
    Serial.println("Not a valid program choice.");
  }
}

void getValue(int *configVar, String printConfirmation) {
	while (*configVar == -1) {
		while (!Serial.available()) {}
		*configVar = Serial.readString().toInt();
		Serial.println(printConfirmation);
	}
}
	
void pingTimer() {
  unsigned long startTime = millis();
  unsigned long elapsedTime = 0;

  while (elapsedTime < totalTime) {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    pingTime = pulseIn(echoPin, HIGH, 3E4);
    if (pingTime > 0) {
      Serial.print(elapsedTime);
      Serial.print(",");
      Serial.println(pingTime);
    }
    elapsedTime = millis() - startTime;
    delay(100);
  }
  Serial.println("Done.");
  chosenInt = 0;
}

`

A simple example could be:

`


`


Created by Tarjei Bærland
November 2019
"""

from datetime import datetime
import time

import matplotlib.pyplot as plt
import numpy as np

import serial
import serial.tools.list_ports as prts


class Arduino(serial.Serial):
    def send_value(self, value):
        self.write(str(value).encode('ASCII'))

    def get_message(self, wait_time=0.1):
        print("Waiting for Arduino.", end="")
        while self.inWaiting == 0:
            time.sleep(wait_time)
            print(".", end="")
        print()
        message = self.readline().decode()
        print(f"Got message: {message}")


def collect_data(choice=1, runtime=5000, delay=3000, measure_period=50, comport=None):
    """Run the chosen Arduino function and return the data.

    Choices:
    1) Pingtimer: returns a tuple of times and pingtimes. Arduino connected with
                  trigger at ping 13 and echo at pin 11.

    """
    if comport == None:
        com_arduino = prts.comports()[0]
        com_name = com_arduino.device

    times = []
    echos = []

    with Arduino(com_name, 9600, timeout=3) as arduino:
        print(f"Connected to: {com_name}")
        arduino.flushInput()
        arduino.get_message()

        for value in [delay, runtime, choice, measure_period]:
            arduino.send_value(value)
            arduino.get_message()

        while True:
            if arduino.inWaiting() > 0:
                data = arduino.readline().decode().strip()
                print(data)
                if data.lower().startswith('done'):
                    break
                time, echo = data.split(",")
                times.append( float(time) )
                echos.append( float(echo) )

    times = np.array(times)
    echos = np.array(echos)
    print("Ferdig.")
    return times, echos


if __name__ == "__main__":     
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y%m%d%H%M%S")
    FIGNAME = f"test-{timestamp}.png"
    times, echos = collect_data(choice=1, delay=300, runtime=5000)
    plt.plot(times, echos)
    plt.savefig(FIGNAME)
