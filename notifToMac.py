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
'''
print ("Script name: %s" % str(sys.argv[0]))
print ("First argument: %s" % str(sys.argv[1]))
print ("Second argument: %s" % str(sys.argv[2]))
'''
#Dynamic fields for what to display in the notifcation
'''
title = "Title"
subtitle = "Subtitle"
message = "Message"
'''

title = "ErgoFix Alert"
subtitle = arg1
message = arg2
command = "\'display notification \"" + message + "\" with title \"" + title +"\" subtitle \""+ subtitle+"\"\'"
os.system('osascript -e ' + command)
