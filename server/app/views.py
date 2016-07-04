from django.shortcuts import render_to_response
from django.template import RequestContext

from app.models import Application, Version
from app.forms import DeployForm

def index(request):
    applications = Application.objects.all()
    return render_to_response('app/index.html', {"applications": applications}, context_instance=RequestContext(request))

def deploy(application_id):
    application = Application.objects.get(id=application_id)
    if request.method == "POST":
        form = DeployForm(request.POST)
	if form.is_valid():
	    pass

    return render_to_response('app/deploy.html', {"application": application}, context_instance=RequestContext(request))
