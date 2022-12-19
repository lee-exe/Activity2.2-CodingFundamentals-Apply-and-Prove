from flask import Flask, render_template
# render_template allows flask to load HTML files
app = Flask(__name__)
# Basic route that will give us info
# When it detects someone going to 0.0.0.0 do this thing
@app.route("/")  # Decoration / Annotation
def home():
    return "Is this working... "

@app.route("/hello/<name>")
def hello(name):
    return "Hello, %s" % name
# 127.0.0.1:5000/hello/Lee

@app.route("/random")
def random():
    return print(random(1, 10))

@app.route("/item/<id>")
def page_id(id):
    return "The id is %s" % id
# 127.0.0.1:5000/items/1

@app.route("/about")
def about():
    return "About us..."

@app.route("/about/<name>")
def about_name(name):
    return "%s's profile" % name


@app.route("/coolHtml")
def render_html():
    return render_template("index.html", user="Elon Musk")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
