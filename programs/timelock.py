##########################################################################################
# Name: Alyse Jones
# Date: Due 5/8/20
# Program: This program implements the Timelock algorithm for encryption
# Execution in command line: python3 timelock.py
#                            press [Enter]
#                            type epoch in the form YYYY MM DD HH mm SS
#                            then [CtrlD] to see output
##########################################################################################

from sys import stdin
from datetime import datetime, timedelta
import pytz
from hashlib import md5
import calendar
from time import gmtime

# debug mode?
DEBUG = False
DEBUG2 = False

# set to True if on the challenge server
ON_SERVER = False

# valid time interval
INTERVAL = 60
# manual current datatime
MANUAL_DATETIME = "2017 03 23 18 02 06"

# function that retrieves current system time and converts to appropriate format
def getCurrentTime():
    if MANUAL_DATETIME == "":
        now = datetime.now()
        date_time = now.strftime("%Y %m %d %H %M %S")
        date_time = datetime.strptime(date_time, "%Y %m %d %H %M %S")
        if(DEBUG2):
            print(date_time)
    # for debugging
    else:
        date_time = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")
        if(DEBUG2):
            print((date_time))
    return date_time

# convert Epoch string to Epoch datetime
def convertEpoch(epoch):
    epoch_time = datetime.strptime(epoch, "%Y %m %d %H %M %S")
    seconds_since_epoch = epoch_time.timestamp()
    if(DEBUG2):
        print(epoch_time)
        print(seconds_since_epoch)
    return epoch_time

# convert datetimes to UTC
def convertUTC(datetime):
    local_time = pytz.timezone("America/Chicago")
    local_datetime = local_time.localize(datetime, is_dst=None)
    utc_datetime = local_datetime.astimezone(pytz.utc)
    return utc_datetime

# extraction of letters and numbers from hash
def findFirstLetters(h):
    a = "abcdef"
    num = "0123456789"
    counter1 = 0
    counter2 = 0
    L2 = ""
    # extract and concatenate the first two letters of the hash from left-to-right
    for i in h:
        if counter1 < 2:
            for x in a:
                if i == x:
                    counter1 += 1
                    L2 += i
    # extract and concatenate the first two single-digit integers of the hash from right-to-left
    for j in reversed(h):
        if counter2 < 2:
            for x in num:
                if j == x:
                    counter2 += 1
                    L2 += j
    return L2

# read epoch input and convert times to UTC (which accounts for DST)
text = stdin.read().rstrip("\n")
current_time = getCurrentTime()
epoch_time = convertEpoch(text)
utc_current = convertUTC(current_time)
utc_epoch = convertUTC(epoch_time)
# compute time elasped (in seconds) of the current system since an epoch time
duration = utc_current - utc_epoch
duration_seconds = int(duration.total_seconds())
time_elasped = int(duration_seconds - duration_seconds % INTERVAL)

# generate hash
h1 = md5(str(time_elasped).encode()).hexdigest()
h2 = md5(h1.encode()).hexdigest()
L2 = findFirstLetters(h2)

if(DEBUG):
    print("Current (UTC): " + str(utc_current))
    print("Epoch (UTC): " + str(utc_epoch))
    print("Duration (sec): " + str(duration_seconds))
    print("Time Elasped (sec): " + str(time_elasped))
    print("MD5 #1: " + str(h1))
    print("MD5 #2: " + str(h2))

# print result
print("Code: " + str(L2))
