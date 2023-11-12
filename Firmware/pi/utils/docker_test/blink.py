import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin as an output
led_pin = 21
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        
        # Wait for a short duration
        time.sleep(1)
        
        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        
        # Wait again
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO configuration on Ctrl+C
    GPIO.cleanup()