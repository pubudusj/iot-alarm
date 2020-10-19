import greengrasssdk
import RPi.GPIO as GPIO
import time
import os


client = greengrasssdk.client("iot-data")

buzzerPin = int(os.getenv('BuzzerPin'))
ledPin = int(os.getenv('LedPin'))

def lambda_handler(event, context):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buzzerPin, GPIO.OUT)

    for x in range(5):
        GPIO.output(ledPin, GPIO.HIGH)
        GPIO.output(buzzerPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        GPIO.output(buzzerPin, GPIO.LOW)
        time.sleep(1)

    return
