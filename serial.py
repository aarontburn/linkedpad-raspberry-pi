import RPi.GPIO as GPIO
import time

pin = 7
pin1 = 37

def setup():
    GPIO.setmode(GPIO.BOARD)       
  
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pin1, GPIO.OUT)
  
  
    GPIO.output(pin1, GPIO.LOW)
  

def loop():
    while True:
        if (GPIO.input(pin) == 0):
            print("pressed")
        
        time.sleep(0.2)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()