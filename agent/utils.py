import socket
import fcntl
import struct

def get_hostname():
    return socket.gethostname()

def get_ip_by_nic(nic_name):
    all_nics = get_all_nics()
    if nic_name not in all_nics:
	raise Exception("The nic name(%s) is not correct, please select from %s." %(nic_name, ', '.join(all_nics)))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
	       s.fileno(),
	       0x8915, 
	       struct.pack('256s', nic_name)
           )[20:24]) 

def get_all_nics():
    nics = []
    with open("/proc/net/dev") as f:
	for line in f:
	    line = line.rstrip().split(":")
            if len(line) == 2:
		nics.append(line[0].lstrip())
    return nics
