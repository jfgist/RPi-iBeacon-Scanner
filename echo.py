#!/usr/bin/env python2.7
import sys

# conditionally echoing the piped input
for line in sys.stdin:
	if "tweet" in line:
		print line
		
		
		
		
# Do the setup stuff from sendtweet
# - Read 
		
# for line in sys.stdin:
	# if iBeaconID in line:
		# send tweet