from flask import Flask, redirect, url_for, render_template
import main as convert_to

app = Flask(__name__)

@app.route("/<lang>/home/")
def home(lang):
    if lang == "en":
        return render_template("index.html")
    elif lang == "id":
        pass
    elif lang == "de":
        pass

@app.route("/<lang>/convert=<input>/")
def convert(lang, input):
    try:
        if lang == "en":
            return render_template("convert.html", number=input, fpr_binary=convert_to.gleitKommazahl(float(input))[0], fpr_hexa=convert_to.gleitKommazahl(float(input))[1])
        elif lang == "id":
            pass
        elif lang == "de":
            pass
    except ValueError:
        return redirect(url_for("error", type="Invalid_Input"), lang=lang)

@app.route("/<lang>/error=<type>")
def error(lang, type):
    if lang == "en":
        return render_template("error.html", message=type)
    elif lang == "id":
        pass
    elif lang == "de":
        pass
    
if __name__ == "__main__":
    app.run()