#Imports subprocess (used for async functionality)

import subprocess

 
#Asks user for input (can be dragged from desktop)

fields = ['IP', 'Response']

plist = input("Paste exact file path of ip list: ")

filename = input("What do you want the name of the output file to be?")

with open(plist, 'r') as fileobj:

    def ping(ip):

#Pings the ip once, change the "1" to "2" if MAC adress is not resolving, may make it slower

        ping_reply = subprocess.run(["ping","-n","1", ip],stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        result =""

        print (".", end='')

        if ping_reply.returncode == 0:

            #ping will return 0 success if destination is unreachable

            if ("unreachable" in str(ping_reply.stdout)):

                result = ("\n Offline%s" % ip)

            else:

                result= ("\n Online %s" % ip)

        elif ping_reply.returncode == 1:

            result= ("\n No response %s" % ip)

        return result

 
    for ip in fileobj:

        print(ping(ip.strip()))
