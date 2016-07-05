from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from app.models import Application, Version
from app.forms import DeployForm

from ping.views import get_available_hosts
import zmq
import json

import logging
log = logging.getLogger(__name__)

def index(request):
    applications = Application.objects.all()
    return render_to_response('app/index.html', {"applications": applications}, context_instance=RequestContext(request))

def deploy(request, application_id):
    application = Application.objects.get(id=application_id)

    info = {
	"name": application.name,
	"description": application.description,
	"repo": application.repo,
	"path": application.path
    } 

    ips = get_available_hosts()
    for ip in ips:
	context = zmq.Context()
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://%s:10000" % (ip))
	socket.send(json.dumps(info))
        msg = socket.recv()
	log.info(msg)
        socket.close()

    return HttpResponse("success")
