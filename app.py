from flask import Flask, request, render_template
from flask_cors import CORS
import shortenURL


app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        shorten_URL = shortenURL.id_generator()
        return render_template('home.html', shorten_URL = shorten_URL),200
    
    else:
        return render_template('home.html'), 200

    
if __name__=="__main__":
    app.run(debug=True)
