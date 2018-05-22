from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
import json

def getData(request):
	fname = settings.BASE_DIR+"/Logs_04_01_2018.log"
	with open(fname) as f:
		content = f.readlines()
	context = {'content':content}
	return render(request, "polling.html", context)

def pollData(request):
	fname = settings.BASE_DIR+"/Logs_04_01_2018.log"
	with open(fname) as f:
		content = f.readlines()
		print (content)

	return HttpResponse(json.dumps({'content': content}), content_type="application/json")

