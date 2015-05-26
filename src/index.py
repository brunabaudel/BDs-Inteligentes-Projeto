from dbpedia_annotator import DBpediaAnnotator

def index(req):
  title = 'BDs inteligentes'

  site = header(title)
  site += body(req)
  site += footer()

  return site

def header(title):
  site = """<!DOCTYPE html>
            <html >
              <head>
                <meta charset="UTF-8">
                <title>""" + title + """</title>
                <link rel='stylesheet prefetch' href='http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css'>
              <link rel="stylesheet" href="css/style.css">
             </head>"""
  return site

def body(req):
  text = ''

  if req.form:
    text = req.form['text']

  site = """<body>
              <div class="login-card">
                <h1>Enter the text in the box below</h1><br>
                <form method="post">
                  <textarea name="text" placeholder="Text">""" + text + """</textarea>
                  <input type="submit" name="send" class="login login-submit" value="Annotate">
                </form>"""

  if text:
    annotator = DBpediaAnnotator();
    annotations = annotator.annotate_text(text)

    if 'Resources' in annotations:
      site += 'DBpedia resources: <br />'
      for resource in annotations['Resources']:
        site += '<a href="' + resource['@URI'] + '"/>' + resource['@URI'] + '</a> <br />'
    else:
      site += 'No DBpedia resources.'
  

  site += """</div>
             <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
             <script src='http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js'></script>
          </body>"""
  return site

def footer():
  site = '</html>'
  return site