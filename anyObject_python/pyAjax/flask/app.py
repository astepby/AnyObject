from flask import Flask, request, render_template
from flask_cors import CORS
import simplejson as json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
#@crossdomain(origin='*')
def signUpUser():
    print("data received")
    #ddata = request.json['data']
    so="service_Object_name"
    return json.dumps({'status':'OK','serviceObject':so});

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0')
