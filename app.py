import os
import psycopg2
from flask import Flask, render_template, request
from dotenv import load_dotenv
#from extensions import db
from config import Config


load_dotenv()

app = Flask(__name__)
url = os.environ.get("DATABASE_URL")  # gets variables from environment
connection = psycopg2.connect(url)

headline = "test"

@app.route("/")
def index():
    return render_template("index.html", headline=headline)
@app.route("/more")
def more():
    return render_template("more.html", headline=headline)
@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name, headline=headline)


app.config.from_pyfile("config.py")
