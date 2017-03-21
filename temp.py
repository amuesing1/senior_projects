import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor_1 = '/sys/bus/w1/drivers/w1_slave_driver/28-0000075f85ba/w1_slave'
temp_sensor_2 = '/sys/bus/w1/drivers/w1_slave_driver/10-000803362138/w1_slave'
temp_sensor_3 = '/sys/bus/w1/drivers/w1_slave_driver/28-00000620a9b2/w1_slave'

def temp_raw(temp_sensor):
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(temp_sensor):
    lines = temp_raw(temp_sensor)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

while True:
        start=time.time()
        print "Sensor 1: %3.2f C, Sensor 2: %3.2f C, Sensor 3: %3.2f C" % (read_temp(temp_sensor_1),read_temp(temp_sensor_2),read_temp($
        final=time.time()-start
        print final
