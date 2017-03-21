import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
def read():
        NUM_CYCLES = 10000
        start=time.time()
        for impulse_count in range(NUM_CYCLES):
                GPIO.wait_for_edge(17, GPIO.FALLING)
        duration = time.time()-start
        freq = NUM_CYCLES/duration

        #print 'Frequency = %3.2f Hz' % (freq)
        hum = 1.2158e-8*freq**3-2.193e-4*freq**2+1.2094*freq-1.8698e3
        return hum

while True:
        hum = read()
        print time.time()
        print 'Humidity = %3.2f %%' % (hum)
        time.sleep(5)
