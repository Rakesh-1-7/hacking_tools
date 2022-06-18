

import socket
import termcolor


def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		# sock.timeout(0.5)
		print(termcolor.colored("[+] Port Opened " + str(port) ,'red' ) )
		sock.close()
	except:
		# pass
		# 192.168.43.230 
		print(termcolor.colored("[+] Port Closed " + str(port) ,'blue' ) )


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
