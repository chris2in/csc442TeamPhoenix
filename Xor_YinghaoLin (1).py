######################################################################
#   Name:   Yinghao Lin
#   Date:   5 May 2020
#   USEAGE: python2 Xor_YinghaoLin.py < ciphertext
#           where cipher text include the message
#           and key is locally stored in same folder with this 
# 
#############################################################



import sys 

DEBUG = False 

#   perform the xor operation 
def xor(text,key):
    
    #   make sure the length of key is equal tothe length
    #   of text before continues to xor
    if (len(text) <len(key)):
        if(DEBUG):
            print("length of text is less than length of key")
        
        key = key[:len(text)]
    if(len(text)>len(key)):
        if(DEBUG):
            print("length of text is longer than length of key")
        
        key*(int(len(text)/len(key)))+key[:(len(text)%len(key))]
    
    
    return ([i ^ o for i,o in zip(text,key)])

#   read the text
text = sys.stdin.read()

#   define a dynamic key file name 
KEYFILENAME = "key"

#   read the key file
with open(KEYFILENAME,'rb')as file:
    key = file.read()
file.close()

#   created bytearray for the text and key 
key = bytearray(key)
text = bytearray(text)

#   get hte final result by xor
finalOutput = xor(text,key)

#   output the result 
for i in range(len(finalOutput)):
    sys.stdout.write(chr(int(finalOutput[i])))
