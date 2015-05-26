import urllib2
import urllib
import json

SPOTLIGHT_URL = 'http://spotlight.sztaki.hu:2222/rest/annotate'
SPOTLIGHT_CONFIDENCE = 0.5

class DBpediaAnnotator(object):

  def annotate_text(self, text):
    parameters = {'text':text, 'confidence':SPOTLIGHT_CONFIDENCE}
    request = urllib2.Request(SPOTLIGHT_URL, data=urllib.urlencode(parameters))
    request.add_header('Accept', 'application/json')

    response = urllib2.urlopen(request)
    annotations = json.load(response)

    return annotations