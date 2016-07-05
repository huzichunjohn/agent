from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from deploy.config import REDIS_SERVER, REDIS_PORT, REDIS_DB

import time
import json
from utils import get_timestamp_by_string

import redis
conn = redis.StrictRedis(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)

@csrf_exempt
def index(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ip = data["ip"]
        last_updated = data["current"]
        conn.sadd("iplist", ip)
	conn.set(ip, last_updated)
        return HttpResponse("pong") 
    else:
	return HttpResponse("pong")

def status(request):
    status = []
    ip_list = conn.smembers("iplist") 
    for ip in ip_list:
	last_updated = conn.get(ip)
        last_updated_timestamp = get_timestamp_by_string(last_updated, "%Y-%m-%d %H:%M:%S") 
        now = int(time.time())
        if now - last_updated_timestamp > 10:
            status.append({"ip": ip, "status": "critical"})
	elif now - last_updated_timestamp > 5:
	    status.append({"ip": ip, "status": "warning"})
        else:
	    status.append({"ip": ip, "status": "ok"})
    return HttpResponse(json.dumps(status), content_type="application/json")

def get_available_hosts():
    ips = []
    ip_list = conn.smembers("iplist")
    for ip in ip_list:
	last_updated = conn.get(ip)
        last_updated_timestamp = get_timestamp_by_string(last_updated, "%Y-%m-%d %H:%M:%S")
        now = int(time.time())
        
        if now - last_updated_timestamp <= 5:
	    ips.append(ip)

    return ips
