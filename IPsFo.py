#!/usr/bin/python
# -*- coding: utf-8 -*-

########################
# Script: IPsFo,V1.0
# Jab: Scanning For [ IPs | IPs Geoip Info | Reverse IP Lookup ]
# CodedBy: Oseid Aldary :)
#
#
## Import Libraryies

try:
  import dns.resolver
except:
     print("\033[1;33m[\033[1;31m!\033[1;33m][ERROR] \033[1;37m[\033[1;32mdnspython\033[1;37m] Library Is Not Exist \033[1;31m !!!")
     print("\033[1;32m[\033[1;37m*\033[1;32m] Please Install It Using This Command: \033[1;37mpip install dnspython")
     exit(1)
try:
   import urllib2
except:
   print("\033[1;33m[\033[1;31m!\033[1;33m][ERROR] \033[1;37m[\033[1;32murllib2\033[1;37m] Library Is Not Exist \033[1;31m !!!")
   print("\033[1;32m[\033[1;37m*\033[1;32m] Please Reinstall Your Python To Install It :)")
   exit(1)
try:
   import json
except:
     print("\033[1;33m[\033[1;31m!\033[1;33m][ERROR] \033[1;37m[\033[1;32mjson\033[1;37m] Library Is Not Exist \033[1;31m !!!")
     print("\033[1;32m[\033[1;37m*\033[1;32m] Please Install It Using This Command:\033[1;37m pip install simplejson")
     exit(1)
from time import sleep
from os import system as sy
from copy import copy
import socket

## Check Internet Connection
server = "www.google.com"
def check():
  try:
     ip = socket.gethostbyname(server)
     con = socket.create_connection((ip, 80), 2)
     return True
  except:
	pass
  return False
##################

def GetIPs(target):
	TARGET = target
	IPs = []
	loop = 1
	print("\033[1;37m="*10+"> \033[1;32mConfig \033[1;37m<"+"="*10)
	print("\033[1;37m[\033[1;32m TARGET \033[1;37m]     : \033[0;36m {}".format(TARGET))
	print("\033[1;37m[\033[1;32m Job\033[1;37m ]        : \033[1;0;36m Find All Target Ip Addr Status Up")
	print("\n\033[1;31m[\033[1;32m+\033[1;31m] \033[1;36mScanning For Ips\033[1;33m......\n")
	sleep(1.3)
        for address_type in ['A', 'AAAA']:
           try:
              answers = dns.resolver.query(TARGET, address_type)
              for rdata in answers:
		 IPs.append(rdata)
	   except dns.resolver.NoAnswer:
			pass
	   except dns.resolver.NXDOMAIN:
		 print("\n\033[1;33m[\033[1;31m!\033[1;33m]\033[1;37m Please Input Domain Or Site Or Url \033[1;33m!!")
		 print("\n\033[1;36m Backing.....")
		 sleep(1.3)
		 Main()
	   except:
		print("\033[1;33m[\033[1;31m!\033[1;33m]\033[1;37m Plese Check Your Target \033[1;31m !!!")
		print("\033[1;35m Backing.....")
		sleep(1.3)
		Main()
	if len(IPs) > 0:
		print("\033[1;32m[+]\033[1;34m Found\033[1;31m:\n")
		loop = 1
		for i in IPs:
		    print("\033[1;37mTARGET[\033[1;32m{}\033[1;37m] IP[\033[1;32m{}\033[1;37m] : \033[1;32m {}   \033[1;37mSTATUS[ \033[1;32mUP\033[1;37m ]".format(target,loop,i))
		    loop+=1
		loop = loop -1
		print("\n\033[1;37m[\033[1;32m*\033[1;37m] This Target Has [\033[1;32m{}\033[1;37m] IP Servers \033[1;32m Status[\033[1;37mUP\033[1;32m]".format(loop))
	else:
	    pass
	    exit(1)
        ask = raw_input("\n\033[1;36m [b]\033[1;37mack \033[1;36m[e]\033[1;37mxit :\033[1;31m ")
        while ask == "" or ask is None or ask not in 'be':
                   ask = raw_input("\n\033[1;31m[!]\033[1;33m[b]\033[1;37mack\033[1;33m [e]\033[1;37mxit :\033[1;31m ")
        if ask == "b":
                Main()
        else:
             exit(1)

def revdom(target):
    if check() == True:
	 print("\033[1;31m="*10+"\033[1;36m>\033[1;32m Config \033[1;36m<\033[1;31m"+"="*10)
	 print("\033[1;37m[\033[1;32m TARGET \033[1;37m]     :\033[1;32m {}".format(target))
	 print("\033[1;37m[\033[1;32m Job \033[1;37m]        : \033[1;32mLookUp Domains")
	 print("\n\033[1;34m[\033[;31m+\033[1;34m] \033[1;36m Scanning For Domains\033[1;33m......")
	 sleep(1.3)
         rev   = urllib2.urlopen('http://api.hackertarget.com/reverseiplookup/?q='
                +target).read().rstrip()
	 print("\033[1;37m[\033[1;32m+\033[1;37m] Found:\n")
	 sleep(1)
	 print(rev)
    else:
	print("\033[1;31m[!]\033[1;32m Please Check Your Internet Connection \033[1;31m !!!")

    ask = raw_input("\n\033[1;36m [b]\033[1;37mack \033[1;36m[e]\033[1;37mxit :\033[1;31m ")
    while ask == "" or ask is None or ask not in 'be':
            ask = raw_input("\n\033[1;31m[!]\033[1;33m[b]\033[1;37mack\033[1;33m [e]\033[1;37mxit : \033[1;31m")
    if ask == "b":
             Main()
    else:
        exit(1)

def IPsFo(target):
	TARGET = target
	domains = []
	loop = 1
        for address_type in ['A', 'AAAA']:
           try:
              answers = dns.resolver.query(TARGET, address_type)
              for rdata in answers:
		 domains.append(rdata)
		 loop+=1
	   except dns.resolver.NoAnswer:
			pass
	   except dns.resolver.NXDOMAIN:
		 print("\n\033[1;33m[\033[1;31m!\033[1;33m]\033[1;37m Please Input Domain Or Site Or Url \033[1;33m!!")
		 print("\n\033[1;36m Backing.....")
		 sleep(1.3)
		 Main()
	   except:
		print("\033[1;33m[\033[1;31m!\033[1;33m]\033[1;37m Plese Check Your Target \033[1;31m !!!")
		print("\033[1;35m Backing.....")
		sleep(1.3)
		Main()
	url = "http://ip-api.com/json/"
	result = loop - 1
	print("\n\033[1;32m[*]\033[1;37m Found[\033[1;32m{}\033[1;37m] Server(s) IPs".format(result))
	print("\033[1;32m[\033[1;37m*\033[1;32m]\033[1;37m Scanning All IPs Found!....")
	sleep(1.5)
	result = 1
	for i in domains:
	 reponse = urllib2.urlopen(url + str(i) )
	 name = reponse.read()
	 labs = json.loads(name)
	 print("\n\033[1;32mTARGET[\033[1;37m{}\033[1;32m][\033[1;37m{}\033[1;32m] \n\033[1;31mINFO\033[1;32m:=================================\033[1;37m".format(result,i))
	 result +=1
	 print("\033[1;92m" + "\n IP: " +"\033[1;37m"+ labs['query'])
	 print("\033[1;92m" + " Status: " +"\033[1;37m"+ labs['status'])
	 print("\033[1;92m" + " Region: " +"\033[1;37m"+ labs['regionName'])
	 print("\033[1;92m" + " Country: " +"\033[1;37m"+ labs['country'])
	 print("\033[1;92m" + " City: " +"\033[1;37m"+ labs['city'])
	 print("\033[1;92m" + " ISP: "+"\033[1;37m" + labs['isp'])
	 print("\033[1;92m" + " Lat,Lon: "+"\033[1;37m" + str(labs['lat']) + "," + str(labs['lon']))
	 print("\033[1;92m" + " ZIPCODE: "+"\033[1;37m" + labs['zip'])
	 print("\033[1;92m" + " TimeZone: " +"\033[1;37m"+ labs['timezone'])
	 print("\033[1;92m" + " AS: " +"\033[1;37m"+ labs['as'] + "\n")
	 print("\033[1;35m======================================")
	ask = raw_input("\n\033[1;36m [b]\033[1;37mack \033[1;36m[e]\033[1;37mxit :\033[1;31m ")
	while ask == "" or ask is None or ask not in 'be':
	           ask = raw_input("\n\033[1;31m[!]\033[1;33m[b]\033[1;37mack\033[1;33m [e]\033[1;37mxit :\033[1;31m ") 
	if ask == "b":
		Main()
	else:
	     exit(1)
def Main():
 try:
  sy("clear || cls")
  print("""\033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                   Welcome TO \033[1;31mIPsFo Script                    █
█                                                              █
|══════════════════════════════════════════════════════════════┘ \033[1;32m
|\033[1;37m[>] Script:\033[1;32m IPsFo
|\033[1;37m[>] Jab:\033[1;32m Scanning For [ IPs | IPs Geoip Info | Reverse IP Lookup ]
|\033[1;37m[>] Version:\033[1;32m 1.0 
|\033[1;37m[>] CodedBy: \033[1;32mOseid Aldary
""")
  target = raw_input("\n\033[1;37m[\033[1;32mTARGET\033[0;36m/Domain/Site/url\033[1;37m]\033[1;33m==>\033[1;31m ")
  while target == "" or target is None:
   target = raw_input("[!]\033[1;37m[\033[1;32mTARGET??\033[1;37m]\033[1;33m==>\033[1;31m ")
 except EOFError:
	Main()
 except KeyboardInterrupt:
	print("\n\033[1;31m[CTRL+C]\033[1;37m Exiting....")
	sleep(1)
	print("\033[1;32mGoodBye :)")
	exit(1)

 if target[:8] == "https://":
    tar = target[8:]
 elif target[:7] == "http://":
    tar = target[7:]
 else:
    tar = target
## Check If Target Exist
 def checker():
  if check() == True:
   try:
     ip = socket.gethostbyname(tar)
     con = socket.create_connection((ip, 80), 2)
     return True
   except:
	pass
   return False
  else:
     print("\n\033[1;33m[!] \033[1;37mPlease Check Your Internet Connection \033[1;31m !!!")
     exit(1)
 if checker() == True:
  try:
     print("""\n
\033[1;37m[\033[1;32m1\033[1;37m]> Find All TARGET[\033[1;32m{}\033[1;37m] IP Addresses
\033[1;37m[\033[1;32m2\033[1;37m]> Find All TARGET[\033[1;32m{}\033[1;37m] IP Addresses With Geoip Info
\033[1;37m[\033[1;32m3\033[1;37m]> Find All TARGET[\033[1;32m{}\033[1;37m] Reverse Domains""".format(target,copy(target),copy(target)))
     askd = raw_input("\n\033[1;32m[\033[1;32mIPsFo\033[1;37m]=> \033[1;31m")
     while askd == "" or askd is None or askd not in '123':
	     askd = raw_input("\033[1;33m[Enter Your Choice]\033[1;37m=> \033[1;31m")
     if askd == "1":
	  GetIPs(tar)
     elif askd == "2":
        IPsFo(tar)
     else:
	 revdom(tar)
  except KeyboardInterrupt:
        print("\n\033[1;31m[CTRL+C]\033[1;37m Exiting....")
        sleep(1)
        print("\033[1;32mGoodBye :)")
        exit(1)
 else:
    print("\n\033[1;33m[!]\033[1;31m Error:\033[1;33m404\033[1;37m Server Not Found \033[1;31m!!!")
    print("\033[1;33mBacking......")
    sleep(1.3)
    Main()
if __name__=="__main__":
      Main()
##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
