from flask import Flask, render_template, url_for, flash, redirect, request
from forms import Contact
# from datas import messages, add_message
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, engine

app = Flask(__name__)
app.config["SECRET_KEY"] = "5d50c38d0f12ca64cddd64b56c7baeab"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:tana9861751892%40@localhost:3306/portfolio"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Messages(db.Model):
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(50), primary_key = True)
    message = db.Column(db.Text)

with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About Me")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = Contact()
    if form.validate_on_submit():
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        message = request.form["message"]
        new_msg = Messages(firstname=firstname, lastname=lastname, email=email, message=message)
        db.session.add(new_msg)
        db.session.commit()
        flash("Your message has been successfully sent, Thank you!")
        return redirect(url_for("contact")) # PRG pattern (Post-Redirect-Get)
    return render_template("contact.html", title="Contact Me", form=form)


@app.route("/admin/<pas>")
def admin(pas):
    if pas == "mysecretpass":
        messages = Messages.query.all() 
        print(messages)
        return render_template("admin.html", messages=messages) 
    return redirect(url_for("home")) 

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

if __name__ == "__main__":
    app.run(debug=True)