from flask import Flask, render_template, request, redirect, url_for
import time


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        if "login" in request.form:

            user = request.form.get("user")
            password = request.form.get("password")

            if user == "julian" and password == "*****":
                return redirect(url_for("diary"))

    return render_template("login.html")


@app.route("/tagebuch", methods=["POST", "GET"])
def diary():

    data = []

    with open("static/tagebuch/data.txt", "r") as fr:
        for line in fr.readlines():
            split = line.strip("\n").split(" | ")

            data.append(
                {
                    "text": split[2],
                    "date": split[0],
                    "day": split[1]
                }
            )

    return render_template("diary.html", data=data)


@app.route("/tagebuch/neu", methods=["POST", "GET"])
def new():

    if request.method == "POST":
        if "add" in request.form:

            text = request.form.get("text")
            date = time.strftime("%d.%m.%Y %H:%M")
            day = time.strftime("%A")[:3].upper()

            with open("static/tagebuch/data.txt", "a") as fa:
                fa.write(date + " | " + day + " | " + text + "\n")

            return redirect(url_for("diary"))

    return render_template("new.html")


if __name__ == "__main__":
    app.run()
