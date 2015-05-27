from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, redirect
import logging

import urllib2
import urllib
import json

SPOTLIGHT_URL = 'http://spotlight.sztaki.hu:2222/rest/annotate'
SPOTLIGHT_CONFIDENCE = 0.5

def index(request):

	if request.method == 'POST':
		text = request.POST['text']
		annotator = DBpediaAnnotator();
		annotations = annotator.annotate_text(text)
		
		obj = []
		
		if 'Resources' in annotations: 
			for resource in annotations['Resources']:
				obj.append(resource['@URI'])
			return render(request, 'index.html', {'annotations': obj, 'text': text})
		else:
			return render(request, 'index.html', {'annotations': [], 'text': text})
			
	return render(request, 'index.html', {'annotations': [""]})

class DBpediaAnnotator(object):

  def annotate_text(self, text):
		
		parameters = {'text':text, 'confidence':SPOTLIGHT_CONFIDENCE}
		request = urllib2.Request(SPOTLIGHT_URL, data=urllib.urlencode(parameters))
		request.add_header('Accept', 'application/json')

		response = urllib2.urlopen(request)
		annotations = json.load(response)

		return annotations
    
