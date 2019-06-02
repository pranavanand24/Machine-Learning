# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 23:31:20 2019

@author: pranav anand
"""

import time
import webbrowser
total_breaks = 3
break_count = 0
print ("this program started on "+time.ctime())
while ( break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://youtu.be/96n2gRDPWyM")
    break_count = break_count + 1 
     
     