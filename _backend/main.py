import os
from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from uuid import uuid4

from flask_pymongo import PyMongo

app = Flask(__name__, template_folder="static")
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
UPLOAD_FOLDER = r"D:\DSEN-2\cmm-b\_backend\_img"
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/downloader", methods=["GET", "POST"])
def download(filename="###"):
    if filename == "###":
        filename = request.args.get("filename")
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename)


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    print("ez", request.files)
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            print("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == "":
            print("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = str(uuid4()) + "." + file.filename.rsplit(".", 1)[1].lower()
            # filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            # return redirect(url_for("upload_file", filename=filename))
            return jsonify(url=f"http://127.0.0.1:5000/downloader?filename={filename}")
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
