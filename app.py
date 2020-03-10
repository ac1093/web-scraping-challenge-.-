from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")