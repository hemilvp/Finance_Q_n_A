from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///us.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CREATE TABLE
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    En_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(250),nullable=False) 

with app.app_context():
        db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/req")
def reques():
    return render_template("requestform.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        new_user = User(
                name = request.form["name"],
                En_no = request.form["en_no"],
                email = request.form["email"],
                mobile_no = request.form["moblie_no"],
                password = request.form["password"],
            )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html")



if __name__ == "__main__":
    app.run(debug=True)
