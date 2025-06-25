from flask import Flask, render_template, url_for, flash, redirect
from forms import Contact
from datas import messages, add_message

app = Flask(__name__)
app.config["SECRET_KEY"] = "5d50c38d0f12ca64cddd64b56c7baeab"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About Me")

@app.route("/contact", methods=["GET","POST"])
def contact():
    form = Contact()
    if form.validate_on_submit():
        add_message(form.firstname.data, form.lastname.data, form.email.data, form.message.data)
        flash("Your message has been succesfully sent, Thanks you!")
        return render_template("contact.html",title="Contact Me", form=form)
    return render_template("contact.html",title="Contact Me", form=form)

@app.route("/admin/<pas>")
def admin(pas):
    if pas=="mysecretpass":
        return render_template("admin.html", messages=messages)
    return redirect(url_for("home"))

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

if __name__ == "__main__":
    app.run(debug=True)