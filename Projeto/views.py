from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, redirect
import logging

import urllib2
import urllib
import json

from dbpedia_sparql_endpoint import DBpediaSPARQLEndpoint

SPOTLIGHT_URL = 'http://spotlight.dbpedia.org/rest/annotate'
SPOTLIGHT_CONFIDENCE = 0.5

def index(request):
    return render(request, 'index.html', {})

def consult(request):

    if request.method == 'POST':
        text = request.POST['text']
        annotator = DBpediaAnnotator();
        annotations = annotator.annotate_text(text)

        enriched_annotations = []

        sparql_endpoint = DBpediaSPARQLEndpoint()

        if 'Resources' in annotations: 
            for resource in annotations['Resources']:
                resource_attribute_values = sparql_endpoint.query_attributes(resource['@URI'], ['owl:Thing'] + resource['@types'].split(','))

                for name, value in resource_attribute_values.items():
                    resource_attribute_values[name] = ", ".join(value)

                resource_annotation = {
                    'URI': resource['@URI'], 
                    'surfaceForm':resource['@surfaceForm'], 
                    'offset':resource['@offset'], 
                    'attributeValues':resource_attribute_values
                }

                enriched_annotations.append(resource_annotation)

            return render(request, 'consult.html', {'annotations': enriched_annotations, 'text': text})
        else:
            return render(request, 'consult.html', {'annotations': [], 'text': text})

    return render(request, 'consult.html', {'annotations': []})

class DBpediaAnnotator(object):

    def annotate_text(self, text):

        parameters = {'text':text, 'confidence':SPOTLIGHT_CONFIDENCE}
        request = urllib2.Request(SPOTLIGHT_URL, data=urllib.urlencode(parameters))
        request.add_header('Accept', 'application/json')

        response = urllib2.urlopen(request)
        annotations = json.load(response)

        return annotations
