#!/usr/bin/python3

import nmap

print()
print("  _____  _____                   ")
print(" |      |     /     /\    |\   |     ")
print(" |___   |____/     /__\   | \  |    ")
print(" |      |    \    /    \  |  \ |       ")
print(" |      |     \  /      \ |   \| ") 

print("[INFO] Herramienta para escanear puertos de una IP")


ip=input("[+] IP Objetivo ==> ")
nm = nmap.PortScanner()
open_ports="-p "
results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T4")
count=0
#print (results)
print("\nHost : %s" % ip)
print("Estado : %s" % nm[ip].state())
for proto in nm[ip].all_protocols():
	print("Protocolo : %s" % proto)
	print()
	lport = nm[ip][proto].keys()
	sorted(lport)
	for port in lport:
		print ("Puerto : %s\tEstado : %s" % (port, nm[ip][proto][port]["state"]))
		if count==0:
			open_ports=open_ports+str(port)
			count=1
		else:
			open_ports=open_ports+","+str(port)

print("\nPuertos abiertos: "+ open_ports +" IP: "+str(ip))
