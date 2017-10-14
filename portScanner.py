#!/usr/bin/env python

import socket, threading, time

def portScanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = sock.connect_ex((ip,port))
    if sock == 0:
        print ("[*] Port %i is open" % port) 
   
def main():
	ip = input('Please enter IP address: ')
	for i in range(1,1024): 
		t = threading.Thread(target=portScanner, args=(ip, i))
		t.start()
		time.sleep(0.01)
if __name__ == "__main__":
    main()
