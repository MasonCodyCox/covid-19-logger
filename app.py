import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_documents")
def get_documents():
    documents = list(mongo.db.documents.find())
    return render_template("documents.html", documents=documents)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already chosen. Please select something new.")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("username").lower()
        flash("Account Created!")
        return redirect(url_for("my_profile", username=session["user"]))

    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hello, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "my_profile", username=session["user"]))
            else:
                flash("Username and/or Password is incorrect.")
                return redirect(url_for("login"))

        else:
            flash("Username and/or Password is incorrect..")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def my_profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("my_profile.html", username=username)

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("User logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_document", methods=["GET", "POST"])
def create_document():
    if request.method == "POST":
        self_isolating = "on" if request.form.get("self_isolating") else "off"
        document = {
            "symptom_type": request.form.get("symptom_type"),
            "symptom_description": request.form.get(
                "symptom_description"),
            "started_experiencing": request.form.get(
                "started_experiencing"),
            "self_isolating": self_isolating,
            "created_by": session["user"]
        }
        mongo.db.documents.insert_one(document)
        flash("Document Added")
        return redirect(url_for("get_categories"))
    
    return render_template("create_document.html")


@app.route("/edit_document/<document_id>", methods=["GET", "POST"])
def edit_document(document_id):
    if request.method == "POST":
        self_isolating = "on" if request.form.get("self_isolating") else "off"
        update = {
            "symptom_type": request.form.get("symptom_type"),
            "symptom_description": request.form.get(
                "symptom_description"),
            "started_experiencing": request.form.get(
                "started_experiencing"),
            "self_isolating": self_isolating,
            "created_by": session["user"]
        }
        mongo.db.documents.update({"_id": ObjectId(document_id)}, update)
        flash("Document Updated")
        return redirect(url_for("get_categories"))

    document = mongo.db.documents.find_one({"_id": ObjectId(document_id)})
    return render_template("edit_document.html", document=document)


@app.route("/remove_document/<document_id>")
def remove_document(document_id):
    mongo.db.documents.remove({"_id": ObjectId(document_id)})
    flash("Document Removed")
    return redirect(url_for("get_categories"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.documents.find().sort("symptom_type", 1))
    return render_template("categories.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
