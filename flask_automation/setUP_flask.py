import os 
os.environ["FLASK_ENV"] = "development"

f=open("app.py","w")

f.write("""
from flask import Flask

app=Flask(__name__)

if __name__=="__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='127.0.0.1',port=8085)

import apps.routes
""")
f.close()
wd=os.getcwd()
os.mkdir("apps")
os.mkdir("templates")
os.mkdir("static")
os.mkdir(os.path.join(wd,"static","js"))
os.mkdir(os.path.join(wd,"static","css"))
f=open("apps/routes.py","w")
f.write("""
from app import app
from flask import Flask,request,render_template,redirect, url_for

# @app.route('/', methods=['POST', 'GET'])
#return redirect(url_for('function name'))
@app.route('/',methods=['GET'])
def mainPage():
    return "working"


""")
f.close()

f=open("apps/__init__.py","w")
f.write("")
f.close()

f=open("templates/homepage.html","w")
f.write("""
<html>
    <head>
        <title>Project Name {% block CustomTitle %} {% endblock %} </title>
        
        {% include "headercss.html" %}
        <link href="https://fonts.googleapis.com/css2?family=Acme&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{{url_for('static',filename='css/homepage.css')}}">
        {% block manualCSS %}
        {% endblock %}
    </head>

<body>
  <nav>
    <a href="/home">Home</a>
    <a href="/aboutus">About</a>
    <a href="/pricing">Pricing</a>
    <a href="/contactUs">Contact</a>
    <a href="/login">login</a>
    <a href="/signUp">Sign up</a>
    <div class="animation start-home"></div>
  </nav>
  <br>
    <!-- <nav>
        <div class="navicon">
          <div></div>
        </div>
      
        <a>This was</a>
        <a>Made using</a>
        <a>The clip-path property</a>
        <a>Transition in</a>
        <a>CSS only</a>
      
      </nav> -->
    {% block content %}
    {% endblock %}
{% block preJS %} 
{% endblock %}   
{% include "Staticjavascript.html" %}

{% block postJS %} 
{% endblock %}  
</body>

</html>
""")
f.close()


f=open("templates/StaticJavascript.html","w")
f.write("""
#       <script src=
# "https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.js"></script>

""")
f.close()

f=open("templates/headercss.html","w")
f.write("""
#<link rel="stylesheet" href="{{ url_for('static', filename='css/cssfilename.css') }}">
""")