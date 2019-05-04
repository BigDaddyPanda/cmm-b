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
from uuid import uuid4
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder="static")
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# Change it!
UPLOAD_FOLDER = r"D:\DSEN-2\cmm-b\_backend\uploads"
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(["txt", "csv", "xsl"])
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
        if "uploaded_file" not in request.files:
            print("No file part")
            return redirect(request.url)
        file = request.files["uploaded_file"]
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == "":
            print("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = str(uuid4()) + "." + file.filename.rsplit(".", 1)[1].lower()
            filename = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filename)
            x = []
            with open(filename) as f:
                x = f.readlines()
                # data_prep
                # send chainage_av
                # return chainage_av
            return jsonify(
                url=f"http://127.0.0.1:5000/downloader?filename={filename}", sent_data=x
            )
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    """


@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html", online_users=online_users)


@app.route("/user/<username>")
def user_profile(username):
    user = mongo.db.users.find_one_or_404({"_id": username})
    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
