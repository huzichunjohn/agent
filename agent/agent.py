#!/usr/bin/python
import logging

log = logging.getLogger(__name__)
logging.basicConfig(filename="agent.log", level=logging.DEBUG)

import json
import time
import socket
import requests
import threading
import zmq

from utils import get_hostname, get_ip_by_nic

class Heartbeat(threading.Thread):
    def __init__(self, api_url, interval):
	self.api_url = api_url
	self.interval = interval
	self.stop = False
   
        self.hostname = get_hostname()
	self.ip = get_ip_by_nic("eth0")

        super(Heartbeat, self).__init__()

    def run(self):
	while not self.stop:
	    self.report_state()
	    time.sleep(self.interval)
	
    def shutdown(self):
	self.stop = True

    def report_state(self):
	
        payload = {
	    "hostname": self.hostname, 
	    "ip": self.ip, 
	    "current": time.strftime("%Y-%m-%d %H:%M:%S")
	}
	
	headers = {'Content-Type': "application/json"}

	try:
	    r = requests.post(self.api_url, data=json.dumps(payload), headers=headers, timeout=5)
            if r.status_code == requests.codes.ok:
	        log.debug("report heartbeat successful.")
	    else:
		log.debug("the status code({0}) is not correct.".format(r.status_code))
	except requests.ConnectionError as e:
	    log.debug("the network connection abnormal.")
	except requests.exceptions.Timeout as e:
	    log.debug("the heartbeat server response timeout.")


class Deployer(threading.Thread):
    def __init__(self, name, port):
        super(Deployer, self).__init__()
	self.name = name
	self.port = port	
        self.stop = False
	self.initialize_socket()

    def initialize_socket(self):
	context = zmq.Context()
	self.socket = context.socket(zmq.REP)
	self.socket.bind("tcp://*:%d" % (self.port))

    def run(self):
	while not self.stop:
	    self.process_msg()

    def shutdown(self):
	self.stop = True	

    def process_msg(self):
	msg = self.socket.recv()
	log.info("receive message: %s" % (msg))
        time.sleep(2)
        self.socket.send("ok")
	
if __name__ == "__main__":
    try:
        heartbeat = Heartbeat("http://172.16.16.199:8000/ping/", 5)
        heartbeat.setDaemon(True)
        heartbeat.start()

	deployer = Deployer("deploy", 10000)
	deployer.setDaemon(True)
	deployer.start()
        
	while True:
	    time.sleep(5)
    except:
        raise
	heartbeat.shutdown()
        deployer.shutdown()
