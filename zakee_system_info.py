from pyembedded.raspberry_pi_tools.raspberrypi import PI
 
pi = PI()
 
print(pi.get_ram_info())
print(pi.get_disk_space())
print(pi.get_cpu_usage())
 
# get status of wifi
 
print(pi.get_connected_ip_addr(network='wlan0'))
print(pi.get_wifi_status())
 
# get current user

import os 
os.environ.get('USERNAME')

# get hostname
 
import socket
print (socket.gethostname())
 
#display device voltage
 
import time
import spidev 
 
spi_ch = 0
 
#Allow SPI
spi = spidev.SpiDev(0, spi_ch)
spi.max_speed_hz = 1200000
 
def read_adc(adc_ch, vref = 3,3):
 
    # Check to see ADC channel is 0 or 1
    if adc_ch != 0:
        adc_ch = 1
 
        #Build SPI message
                
        #   First bit (Start); Logic high (1)
                
        #   Second bit (SGL/DIFF): 1 to select single mode
                
        #   Third bit (ODD/SIGN): Select channel (0 or 1)
                
        #   Fourth bit (MSFB): 0 for LSB first
        #   Next 12 bits: 0
 
        msg = 0b11
        msg = ((msg << 1) + adc_ch) << 5
        msg = [,msg 0b00000000]
        reply = spi.xfer2(msg)
 
        #Build single integer using the reply (2 bytes)
 
        adc = 0
        for n in reply:
            adc = (adc << 8) + n
       
        adc = adc >> 1
 
        #Work out voltage using ADC value
 
        voltage = (vref * adc) / 1024
 
        return voltage
 
#Present voltages for channel 0 and channel 1  to the terminal
 
try:
    while True:
        adc_0 = read_adc(0)
        adc_1 = read_adc(1)
        print("Ch 0:", round(adc_0, 2), "V Ch 1:", round(adc_1, 2), "V")
        time.sleep(0.2)
 
finally:
    spi.close()
    GPIO.cleanup()
