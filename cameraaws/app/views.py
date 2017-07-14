from __future__ import division
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf 
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.context_processors import csrf
# Create your views here.

def index(request):	
	args = {}	
	args.update(csrf(request))	
	return render(request, 'index.html')
