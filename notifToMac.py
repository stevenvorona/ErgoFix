import os
import sys
total = len(sys.argv)

#mdargs = str(sys.argv)
#print ("The total numbers of args passed to the script: %d " % total)
#print ("Args list: %s " % cmdargs)
# Pharsing args one by one
scriptname = str(sys.argv[0])
arg1 = str(sys.argv[1])
arg2 = str(sys.argv[2])
title = "ErgoFix Alert"
subtitle = arg1
message = arg2
command = "\'display notification \"" + message + "\" with title \"" + title +"\" subtitle \""+ subtitle+"\"\'"
os.system('osascript -e ' + command)


ssh pi@ip 'python pirunner.py' | python macworker.py
