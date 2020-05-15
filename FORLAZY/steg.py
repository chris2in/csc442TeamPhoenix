############################################################################################
# Name: Alyse Jones
# Date: Due 5/8/20
# Program: This program implements the bit and byte methods of storing and retrieving hidden
#          data
# Execution in command line: python3 steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]
############################################################################################

from sys import stdin, stdout, argv

# variables
DEBUG = False
SENTINEL = bytearray([0x0,0xff,0x0,0x0,0xff,0x0])
if(DEBUG):
    print(len(SENTINEL))

# function to read input data from file (either wrapper or hidden) as binary data
def convert_to_ByteArray(some_file):
    with open(some_file, "rb") as binary_file:
        data = bytearray(binary_file.read())
        #print(data)
    if(DEBUG):
        print(type(data))
    return data

# function to store hidden data and sentinel using the Byte method
def store_Bytes(W,H,offset,interval):
    i = 0
    while i < len(H):
        W[offset] = H[i]
        offset += interval
        i += 1

    i = 0
    while i < len(SENTINEL):
        W[offset] == SENTINEL[i]
        offset += interval
        i += 1

    return W

# function to extract hidden data byte-by-byte until the sentinel is reached
# by using the Byte method
def retrieve_Bytes(W,offset,interval):
    H = bytearray()
    end = len(SENTINEL)
    
    while offset < len(W):
        b = W[offset]

        # if last 6 items in the hidden array (H) are equal to the sentinel, break out of loop
        if H[-end:] == SENTINEL:
            break

        H.append(b)
        offset += interval
        
    return H

# function to store hidden data and sentinel using the Bit method
def store_Bits(W,H,offset,interval):
    i = 0
    j = 0
    length = 8

    while i < len(H):
        for j in range(length):
            # 11111110 = 254
            W[offset] &= 254
            # 10000000 = 128
            W[offset] |= ((H[i]&128) >> (length-1))
            H[i] = (H[i]<<1)&(2**length-1)
            offset += interval
        i += 1

    while j < len(SENTINEL):
        for k in range(8):
            W[offset] &= 254
            W[offset] |= ((SENTINEL[i] & 128) >> (length-1))
            SENTINEL[i] = (SENTINEL[i]<<1)&(2**length-1)
            offset += interval
        j += 1

    return W

# function to extract hidden data bit-by-bit until the sentinel is reached
# by using the Bit method
def retrieve_Bits(W,offset,interval):
    H = bytearray()
    end = len(SENTINEL)
    length = 8
    
    while offset < len(W):
        b = 0

        for j in range(length):
            b |= (W[offset]&1)
            if (j < length-1):
                b = (b<<1)&(2**length - 1)
                offset += interval

        # if last 6 items in the hidden array (H) are equal to the sentinel, break out of loop
        if H[-end:] == SENTINEL:
            break

        H.append(b)
        offset += interval
        
    return H

try:
    # defaults
    f = ""
    i = 0
    interval = 1
    wrapper = ""
    hidden = ""
    
    # retrieve and filter through command line input
    for args in argv[1:]:
        # filter out the commands from the files or text
        c = args[:2]
        if len(args) > 2:
            f = args[2:]
        # argv[1] = -s or -r
        if (args == argv[1]):
            mode = c
            # force user to input -s or -r
            if (c != "-s" and c != "-r"):
                raise Exception("Error: only -s or -r allowed")
        # argv[2] = -b or -B
        if (args == argv[2]):
            method = c
            # force user to input -b or -B
            if (c != "-b" and c != "-B"):
                raise Exception("Error: only -b or -B allowed")
        # argv[3] = -o<var>
        if (args == argv[3]):
            # force user to input -o<var>
            if (c != "-o"):
                raise Exception("Error: -o<val> required")
            # if -o<var> input there, extract offset from argument
            else:
                if len(args) <= 2:
                    # default offset
                    offset = 0
                else:
                    offset = int(f)
        # argv[4] = [-i<val>] (optional)
        # if -i<var> input there, extract interval from argument, otherwise interval = 1
        if (c == "-i"):
            interval = int(f)
        # -w<val> either equals argv[4] or argv[5], depending on if [-i<val>] is given
        if (c == "-w"):
            if (args == argv[4] or args == argv[5]):
                if len(args) <= 2:
                    raise Exception("Error: must supply wrapper file, such as '-wfile' ")
                else:
                    wrapper = convert_to_ByteArray(f)
        # optional hidden file
        if (c == "-h"):
            if len(args) <= 2:
                raise Exception("Error: must supply hidden file, such as '-hfile' ")
            else:
                hidden = convert_to_ByteArray(f)

    # BIT METHOD - STORE  
    if (mode == "-s" and method == "-b"):
        # force user to input -w and -h
        if (wrapper == "" and hidden == ""):
            raise Exception("Error: must supply wrapper and hidden file, such as '-wfile -hfile2'")
        if (wrapper == ""):
            raise Exception("Error: must supply wrapper file, such as '-wfile' ")
        if (hidden == ""):
            raise Exception("Error: must supply hidden file, such as '-hfile' ")
        # store using bit method
        result = store_Bits(wrapper,hidden,offset,interval)
        stdout.buffer.write(result)

    # BIT METHOD - RETRIEVE
    if (mode == "-r" and method == "-b"):
        # force user to input -w
        if (wrapper == ""):
            raise Exception("Error: must supply wrapper file, such as '-wfile' ")
        # retrieve using bit method
        result = retrieve_Bits(wrapper,offset,interval)
        stdout.buffer.write(result)

    # BYTE METHOD - STORE
    if (mode == "-s" and method == "-B"):
        # force user to input -w and -h
        if (wrapper == "" and hidden == ""):
            raise Exception("Error: must supply wrapper and hidden file, such as '-wfile -hfile2'")
        if (wrapper == ""):
            raise Exception("Error: must supply wrapper file, such as '-wfile' ")
        if (hidden == ""):
            raise Exception("Error: must supply hidden file, such as '-hfile' ")
        # store using byte method
        result = store_Bytes(wrapper,hidden,offset,interval)
        stdout.buffer.write(result)

    # BYTE METHOD - RETRIEVE
    if (mode == "-r" and method == "-B"):
        # force user to input -w
        if (wrapper == ""):
            raise Exception("Error: must supply wrapper file, such as '-wfile' ")
        # retrieve using byte method
        result = retrieve_Bytes(wrapper,offset,interval)
        stdout.buffer.write(result)
        
except Exception as inst:
    print(inst)
