#########################################################################################
# Name: Alyse Jones
# Date: Due 4/3/20
# Program: Program to extract a covert message from the file permissions of an FTP server
# Execution in command line: python3 ftp.py
#########################################################################################

from ftplib import FTP

# globals (FTP specifics)
# CHALLENGE CHANGE: changed port to 8008 and folder, added user and password
# for ftp.login(USER, PASSWORD)
IP = 'jeangourd.com'
PORT = 8008
FOLDER = "/.secretstorage/.folder2/.howaboutonemore/"
USER = 'valkyrie'
PASSWORD = 'chooseroftheslain'

# the FTP method
METHOD = 10

# the file/folder contents
contents = []
p = ""
permissions = ""

# connect to the FTP server on the specified IP address and port, navigate to the specified folder, and disconnect
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

# isolate the file permissions
for row in contents:
    p = row[0:10]
    # 7 bit method specifications (isolate last seven bits of permission string)
    if METHOD == 7:
        if p[0:3] == '---':
            p = p[3:10]
            for i in p:
                if i == '-':
                    permissions += '0'
                else:
                    permissions += '1'
    # 10 bit method
    elif METHOD == 10:
         for i in p:
                if i == '-':
                    permissions += '0'
                else:
                    permissions += '1'
# BINARY MESSAGE
print(permissions)
