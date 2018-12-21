from flask import Flask, request, render_template
from flask_cors import CORS
import simplejson as json
from xmlParse import getSO

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Welcome to AnyObject. The AnyObject Web-API is implemented by Python3 Flask!"

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
#@crossdomain(origin='*')
def signUpUser():
    print("data received")
    #ddata = request.json['data']
    so="service_Object_name"
    so=getSO()
    
    return json.dumps({'status':'OK','serviceObject':so});

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0')
