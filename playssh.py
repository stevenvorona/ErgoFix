"""
import os
def run(cmd,*args):
    file = open('/Users/steven/Desktop/password.txt')
    password = str(file.readlines()[0])
    pid, fd = os.forkpty()
    if pid==0: # child
        os.execlp(cmd,*args)
    while True:
        data = os.read(fd,1024)
        print data
        if "password:" in data:    # ssh prompt
            os.write(fd,password +"\n")

run("ssh", "ssh", "pi@172.20.10.6")
os.system('echo hello')
"""
