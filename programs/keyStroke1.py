##################################################
#


from pynput.keyboard import Key,Controller
from time import sleep
from termios import tcflush, TCIFLUSH
from sys import stdin,stdout

keyboard = Controller()


password = ['M', 'y', ' ', 'p', 'a', 's', 's', 'w', 'o', 'r', 'd', ' ', 'i', 's', ' ', 'i', 'n', 'c', 'o', 'r', 'r', 'e', 'c', 't', '.', 'My', 'y ', ' p', 'pa', 'as', 'ss', 'sw', 'wo', 'or', 'rd', 'd ', ' i', 'is', 's ', ' i', 'in', 'nc', 'co', 'or', 'rr', 're', 'ec', 'ct', 't.']

password = password[:len(password)/2+1]
password = "".join(password)

#timing 
# timngs = "0.64,0.55,0.74,0.69,0.91,0.38,0.66,0.28,0.97"

# timings = timings.split(",")
timings= ['0.68', '0.29', '0.39', '0.34', '0.27', '0.43', '0.79', '0.49', '0.49', '0.51', '0.95', '0.96', '0.54', '0.25', '0.92', '0.83', '0.34', '0.93', '0.93', '0.32', '0.49', '0.37', '0.16', '0.80', '0.79', '0.16', '0.92', '0.29', '0.35', '0.85', '0.34', '0.56', '0.23', '0.58', '0.85', '0.58', '0.64', '0.22', '0.94', '0.47', '0.22', '0.95', '0.35', '0.10', '0.23', '0.85', '0.11', '0.80', '0.14']

timings = [float(a) for a in timings]
keypress = timings[:len(timings)/2+1]
keyintervals = timings [ len(timings)/2+1:]
# print len(password)
# print len(keypress)
# print(len(keyintervals))
sleep(5)
for i in range(len(password)):
    keyboard.press(password[i])
    sleep(keypress[i])
    keyboard.release(password[i])
    if(i != (len(password)-1)):
        # print("ABBB",i)
        sleep(keyintervals[i])
        # print("AAAA",i)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
tcflush(stdin,TCIFLUSH)
    # print(i)
print("DONE")