#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DEVELOPED BY Di0nJ@ck - June 2018 - v1.0
__author__      = 'Di0nj@ck'
__version__     = 'v1.0'
__last_update__ = 'June 2018'


import requests
import time
    
def main():

   f_input = open("ips.txt", "r")
   f_output = open("results.txt", "w")
   
   num_lines = sum(1 for line in open("ips.txt"))
   
   print ("- " + str(num_lines) + " domains are going to be geolocated" + "\n")
   
   i = 1
   while (i <= num_lines):
      
      IP = f_input.readline().rstrip('\n')
      print ("- Geolocating the IP: " + IP + "\n")
      print ("    * Asking info..." + "\n")
      
      try:
         resp = requests.get('https://www.maxmind.com/geoip/v2.1/city/' + IP, timeout=5) #FREE GEOLOCATOR API FROM MAXMIND
         print ("    * Results retrieved" + "\n")
      except Exception as e:
         print (str(e))      
      
      if resp:
         print ("    * Result: OK" + "\n")
         f_output.write(IP)
         f_output.write(";")
         f_output.write(resp.content)
         f_output.write("\n")
         
      else:
         print ("    * ERROR. Location not found!" + "\n")
         f_output.write(IP)
         f_output.write(";")
         f_output.write("KO")
         f_output.write("\n")
         
      time.sleep(1.51)
      i = i + 1
      
   f_input.close()
   f_output.close()



main()    