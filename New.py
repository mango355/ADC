import RPi.GPIO as GPIO
import time

dac = [8,11,7,1,0,5,12,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(14, GPIO.IN)

def binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]

def num2dac(value):
    signal = binary(value)
    GPIO.output(dac, signal)
    return signal

try:
    while True:
        for v in range(256):
            sign = num2dac (v)
            voltage = v*3.3/2**8
            time.sleep(0.01)

            compv = GPIO.input(14)
            if compv > 0:
                print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(v, sign, voltage))
                break

except KeyboardInterrupt:
    print('KeyboardInterruptt')
else:
    print('no exceptions')

finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup(dac)
    print ("GPIO cleanup completed")