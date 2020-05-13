#!/usr/bin/python
# coding-utf-8
#   import the library needed 
import socket
from sys import stdout
from time import time
from binascii import unhexlify

#   some Constants
DEBUG =False 
ZERO= 0.100
ONE =0.175


#   specify the ip and port 
ip = "138.47.102.67"
port = 33333

#   create server, connect, recv first bit data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
data = s.recv(4096)

#   intialize the covert binary string
covert_bin=""

#   continue until receive EOF signal
while(data.rstrip("\n") != "EOF"):
    
    #   print it if in DEBUG mode
    
    stdout.write(data)
    stdout.flush()

    #   save the time before receive next message
    t0   = time()

    #   receive 
    data = s.recv(4096)
    
    # t1 = time()
    #   compare the time since receive last message 
    delta = round(time()-t0,3)

    #   print the delay if in DEBUG mode
    if(DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

    #   adding 1's and 0's to the covert binary based on the delay 
    if(delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin +="0"

covert = ""
i = 0 




#   go over everything in covert_bin
while(i < len(covert_bin)):
    b = covert_bin[i:i+8]

    n = int("0b{}".format(b),2)

    #   try decode, if failed, add "?"
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i += 8


    
result = "Covert message:" + covert
print (result)
s.close()
