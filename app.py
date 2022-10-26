from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
    return render_template("home.html"),200

    
if __name__=="__main__":
    app.run(debug=True)
