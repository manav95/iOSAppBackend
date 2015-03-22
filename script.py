from flask import Flask, render_template, jsonify, request, redirect, url_for, send_from_directory, current_app, Response
import sys
import json
import csv
import platform
import numpy
from flask import send_file
from numpy import genfromtxt

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_CONFIRMABLE'] = False

@app.route("/recordData", methods=['GET','POST'])

def record():
    if request.method == 'POST':
       dataDict = request.get_json(force=True)
       filename = "output.csv"
       csvfile = open(filename, 'w+')
       writer = csv.writer(csvfile, delimiter=',')
       for array in dataDict:
           for dictionary in array:
               writer.writerow(dictionary.values())
       return "OK"
    if request.method == 'GET':
       return jsonify(username="success")

@app.route("/trainingData", methods=['GET','POST'])

def train():
    if request.method == 'GET':
       my_data = genfromtxt('output.csv', delimiter=',')
       return json.dumps(my_data.tolist())
    if request.method == 'POST':
        data = request.get_json(force=True)
        return combine(data)

@app.route("/sendPicture", methods=['GET'])

def sendBack():
    if request.method == 'GET':
        return send_file("accel.png", mimetype="image/png")

@app.route("/sendPictureTwo", methods=['GET'])

def sendBackTwo():
    if request.method == 'GET':
        return send_file("angle.png", mimetype="image/png")

@app.route("/gatherData", methods=['GET','POST'])

def compare():
    if request.method == 'POST':
        data = request.get_json(force=True)
        return compare(data)
if __name__ == "__main__":
    app.run(debug=True, threaded = True, port=9875)
