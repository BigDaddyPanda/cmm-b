import os
from config import app, ALLOWED_EXTENSIONS, UPLOAD_FOLDER, mongo
from flask import request, jsonify, send_from_directory, render_template
from data_prep import normalizer
from chainage_av import ChainageAvantHandler
from uuid import uuid4


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/downloader", methods=["GET", "POST"])
def download(filename="###"):
    if filename == "###":
        filename = request.args.get("filename")
    return send_from_directory(directory=UPLOAD_FOLDER, filename=filename)


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        manual_conclusion_base = request.form.get("manual_conclusion_base")
        manual_fact_base = request.form.get("manual_fact_base")
        manual_rules_base = request.form.get("manual_rules_base")
        mode_auto_activated = request.form.get("mode_auto_activated") == "true"
        uploaded_file = []
        message = "Could not do anything!"
        status = "failure"

        # check if the post request has the file part
        if not mode_auto_activated:
            if "uploaded_file" not in request.files:
                print("No file part")
            else:
                file = request.files["uploaded_file"]

                # if user does not select file, browser also
                # submit a empty part without filename
                if file.filename == "":
                    message = "No selected file"
                    status = "failure"
                    # return redirect(request.url)
                elif file and allowed_file(file.filename):
                    filename = (
                        str(uuid4()) + "." + file.filename.rsplit(".", 1)[1].lower()
                    )
                    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                    file.save(file_path)
                    with open(file_path,encoding="utf-8") as f:
                        uploaded_file = f.readlines()
                    message = "File successfully uploaded!"
                    status = "success"
                    link = f"http://127.0.0.1:5000/downloader?filename={filename}"
                elif allowed_file(file.filename):
                    message = "Only Text,CSV,JSON are allowed"
                    status = "failure"
                print(message)

            but, base_fait, base_regle = normalizer(
                manual_conclusion_base,
                manual_fact_base,
                manual_rules_base,
                uploaded_file,
            )
            ch = ChainageAvantHandler()
            ch.run_it_baaaaaaaaaaaaaabe(base_regle, base_fait, but)
            out = {
                "deduction": ch.deduction,
                "status": ch.status,
                "saturation_b_f": ch.saturation_b_f,
                "saturation_b_r": ch.saturation_b_r,
            }
            print("Saving New Regles!")
            mongo.db.REGLES.insert_many([{"premisse": i[0], "conclusion": i[1]} for i in base_regle])
            # for i in base_regle:
            #     try:
            #     except Exception as e:
            #         print("i>>",i)
            #         print(e)
                    
        else:

            but, base_fait, base_regle = normalizer(
                manual_conclusion_base,
                manual_fact_base,
                manual_rules_base,
                uploaded_file,
            )
            best_case = mongo.db.REGLES.find_one(
                {
                    "$and": [
                        {"premisse": {"$in": base_fait}},
                        {"conclusion": {"$in": but}},
                    ]
                },
                {"_id": 0},
            )
            out = {
                "deduction": [best_case] if best_case else [],
                "status": "Success" if best_case else "Unsuccess",
                "saturation_b_f": (best_case != None),
                "saturation_b_r": (best_case != None),
            }
            print("best case",(best_case),base_fait,but)

            # tries = 0
            if not best_case:
                base_regle = list(
                    mongo.db.REGLES.find(
                        {
                            "$or": [
                                {"premisse": {"$in": base_fait}},
                                {"conclusion": {"$in": but}},
                            ]
                        },
                        {"_id": 0},
                    )
                )
                base_regle = [(i["premisse"],i["conclusion"]) for i in base_regle]
                print("not best case",base_regle)
                ch = ChainageAvantHandler()
                ch.run_it_baaaaaaaaaaaaaabe(base_regle, base_fait, but)
                out = {
                    "deduction": ch.deduction,
                    "status": ch.status,
                    "saturation_b_f": ch.saturation_b_f,
                    "saturation_b_r": ch.saturation_b_r,
                }
            
            print("Regles:")
            print(base_regle)
            print("Fait")
            print(base_fait)
            print("But:")
            print(but)

        return jsonify(data=out), 200
    return jsonify({"message": message, "status": status}), 407


# @app.route("/")
# def home_page():
#     online_users = mongo.db.users.find({"online": True})
#     return render_template("index.html", online_users=online_users)


# @app.route("/user/<username>")
# def user_profile(username):
#     user = mongo.db.users.find_one_or_404({"_id": username})
#     return render_template("user.html", user=user)


if __name__ == "__main__":
    # mongo.db.REGLES.delete_many({})
    db_entry = mongo.db.REGLES.find_one()
    print(db_entry)
    if not db_entry:
        mongo.db.REGLES.insert_one(
            {"premisse": ["says woof", "it is cute"], "conclusion": ["it is a Dog"]}
        )
        mongo.db.REGLES.insert_one(
            {"premisse": ["says woof", "it is a Dog"], "conclusion": ["it is the goodest boy!"]}
        )
        mongo.db.REGLES.insert_one(
            {"premisse": ["says miaw", "it is evil"], "conclusion": ["it is a Cat"]}
        )
    app.run(debug=True)
