# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 11:16:50 2022

@author: praveen_babu
"""

from flask import Flask ,request,flash
import flask
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)


    


@cross_origin()
@app.route("/")
def index():
    return "Home!"




if __name__ == "__main__":
    app.run() 