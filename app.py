from flask import Flask, redirect, url_for, render_template
import main as convert_to

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("home", lang="en"))

@app.route("/home/<lang>/")
def home(lang):
    if lang == "en":
        return render_template("index.html")
    elif lang == "id":
        return render_template("indexID.html")
    elif lang == "de":
        return render_template("indexDE.html")

@app.route("/convert=<input>/<lang>/")
def convert(lang, input):
    try:
        if lang == "en":
            return render_template("convert.html", number=input, fpr_binary=convert_to.gleitKommazahl(float(input))[0], fpr_hexa=convert_to.gleitKommazahl(float(input))[1])
        elif lang == "id":
            return render_template("convertID.html", number=input, fpr_binary=convert_to.gleitKommazahl(float(input))[0], fpr_hexa=convert_to.gleitKommazahl(float(input))[1])
        elif lang == "de":
            return render_template("convertDE.html", number=input, fpr_binary=convert_to.gleitKommazahl(float(input))[0], fpr_hexa=convert_to.gleitKommazahl(float(input))[1])
    except ValueError:
        return redirect(url_for("error", type="Invalid_Input", lang=lang))

@app.route("/error=<type>/<lang>/")
def error(lang, type):
    if lang == "en":
        return render_template("error.html", message=type)
    elif lang == "id":
        return render_template("errorID.html", message=type)
    elif lang == "de":
        return render_template("errorDE.html", message=type)

if __name__ == "__main__":
    app.run()