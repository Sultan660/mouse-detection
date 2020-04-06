from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("home.html", msg="from the methon")