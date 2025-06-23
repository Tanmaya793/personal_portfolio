from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About", desciption="This is the about us page!")

@app.route("/contact")
def contact():
    return render_template("contact.html",title="contact",description="Contact page, build in progress!!")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects", description="")

if __name__ == "__main__":
    app.run(debug=True)