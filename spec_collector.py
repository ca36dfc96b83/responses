#!/usr/bin/env python

#  spec_collector.py - collect metadata on localhost and write repsonses to file output.txt
#  Author: Brendan M. 2/2015

from subprocess import Popen, PIPE
import sys

def run_cmd(command):
    sb = Popen(command,stdout=PIPE,stderr=PIPE, shell=True)
    result = sb.communicate()[0].strip() 
    if sb.returncode != 0:
        result = "Metric could not be obtained due to error: " + str(sys.exc_info()[1])
    return result

f = open("output_specs", "w")
f.write('The distribution name and/or ' + run_cmd('lsb_release -i') + '\n')
f.write('The kernel version: '  + run_cmd('uname -v') + ', and kernel release: ' + run_cmd('uname -r') + '\n')
f.write('The total RAM: ' + run_cmd('cat /proc/meminfo | grep -i memtotal | awk \'{print $2 " " $3}\'') + '\n')
f.write('The IP address of eth0: ' + run_cmd('if ifconfig eth0 2>&1 >/dev/null; \
         then ifconfig eth0 | grep \'inet addr:\' | cut -d: -f2 | awk \'{ print $1}\'; fi') + '\n')
f.write('The version of perl: ' + run_cmd('if dperl -v  >/dev/null 2>&1; \
         then perl -v | head -2 | tail -1 | grep -o \'([^)]*)\'; else echo "Perl not found"; fi') + '\n')
f.close()
