import os
from flask import (
    Flask,
    request,
    redirect,
    url_for,
    send_from_directory,
    jsonify,
    render_template,
)
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo


app = Flask(__name__, template_folder="static")
app.config["MONGO_URI"] = "mongodb://localhost:27017/cmmb-db"
mongo = PyMongo(app)

# Change it!
UPLOAD_FOLDER = r"D:\DSEN-2\AI\cmm-b\_backend\uploads"
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(["txt", "csv", "xsl"])
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app)
