#!/bin/bash
#pi@raspberrypi:~ $ cat ./cpu_freq.sh
#BASH being used to print out temp and current CPU frequency 
 
temp='head -n 1 /sys/class/thermal/thermal_zone0/temp   |   xargs -I{} awk "BEGIN {printf\"%.2f\n\", {}/1000}"'
 
echo $(('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq'/1000)) MHz,  degrees
 
# the monitor interval: every 5 seconds
while : ; do ./cpu_freq.sh; sleep 5; done
