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
        smth = 0

        for i in range (7,-1,-1):
            smth= 2**i + smth
            sign = num2dac (smth)
            time.sleep(0.01)

            compv = GPIO.input(14)
        
            if compv > 0:
                smth -= 2**i

        voltage = smth*3.3/2**8
        print(voltage)


        # smth = int(0)
        # for i in range (7,0,-1):
            # if (compv>=2**i):
                # smth += 2**i
            # print(smth)
            # break


finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup(dac)
    print ("GPIO cleanup completed")