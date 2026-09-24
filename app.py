from flask import Flask, redirect, url_for, render_template
import main as convert_to

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert=<input>/")
def convert(input):
    try:
        return render_template("convert.html", number=input, fpr_binary=convert_to.gleitKommazahl(float(input))[0], fpr_hexa=convert_to.gleitKommazahl(float(input))[1])
    except ValueError:
        return redirect(url_for("error", type="Invalid_Input"))

@app.route("/error=<type>")
def error(type):
    return render_template("error.html", message=type)

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("greet", text="Admin!"))

# @app.route("/<text>/")
# def greet(text):
#     return f"Hello {text}"

if __name__ == "__main__":
    app.run()