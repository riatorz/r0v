import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
ROLE1 = 18
A1=0
GPIO.setup(ROLE1, GPIO.OUT)
GPIO.output(ROLE1, A1)
# read data using pin 14
instance = dht11.DHT11(pin=25)

try:
    while True:
        
        result = instance.read()
        if result.is_valid():
            print(result.temperature)
            print(result.humidity)
            if(result.humidity >= 70):
                GPIO.output(ROLE1,0)
            else:
                GPIO.output(ROLE1,1)
        time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()