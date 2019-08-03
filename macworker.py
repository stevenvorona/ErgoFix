import time
import os
"""
def sshin(cmd,*args):
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

sshin("ssh", "ssh", "pi@172.20.10.6")
os.system('echo hello')
"""

def calibrate():
    midbutt = 0
    midback = 0
    print "Sit in good posture"
    collectbutt = 0.0
    collectback = 0.0
    currentval = raw_input()

    for i in range(0,2):
        vals = currentval.split(',')
        collectbutt = collectbutt + float(vals[0])
        collectback = collectback + float(vals[1])
    midbutt = collectbutt/10
    midback = collectback/10
    calibrated = []
    calibrated.append(midbutt)
    calibrated.append(midback)
    print "Calibration complete."
    return calibrated

worker = 0
calibrations = calibrate()
print "Calibrated at:" + str(calibrations)
midbutt = calibrations[0]
midback = calibrations[1]
while True:
    inputted = raw_input()
    if len(inputted) == 0:
        continue
    worker = inputted.split(',')
    print worker
    workerbutt = float(worker[0])
    workerback = float(worker[1])
    if (workerbutt - midbutt < -8):
        os.system('python ~/Desktop/Projects/ErgoFix/notifToMac.py \'Move\' \'Left\'')
    elif (workerbutt - midbutt > 8):
        os.system('python ~/Desktop/Projects/ErgoFix/notifToMac.py \'Move\' \'Right\'')
    #elif (workerback < midback - 6):
    #    os.system('python ~/Desktop/Projects/ErgoFix/notifToMac.py \'Lean\' \'Forwards\'')
    elif (workerback - midback <-10):
        os.system('python ~/Desktop/Projects/ErgoFix/notifToMac.py \'Lean\' \'Back\'')
