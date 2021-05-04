# app.py
from flask import Flask, request, jsonify
import script as sp
app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return sp.getscript()

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)