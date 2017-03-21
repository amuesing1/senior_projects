import smbus
import time

def read():
        bus = smbus.SMBus(1)
        data = bus.read_i2c_block_data(0x48, 0)
        msb = data[0]
        lsb = data[1]
        return msb, lsb

while True:
        msb,lsb = read()
        print (((msb << 8) | lsb) >> 4) * 0.0625      #printing the temperature value in Celsius.
        time.sleep(1)
