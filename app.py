from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("harshu1.html")

@app.route("/love-dove")
def dove():
    return render_template("love-dove.html")

@app.route("/mistake")
def mistake():
    return render_template("mistake.html")

@app.route("/tease-it")
def tease():
    return render_template("tease.html")

@app.route("/vertex")
def vertex():
    return render_template("vertex.html")

@app.route("/sd")
def sd():
    return render_template("sd.html")

@app.route("/sd1")
def sd1():
    return render_template("sd1.html")

@app.route("/text")
def text():
    return render_template("text.html")

@app.route("/close")
def close():
    return render_template("close.html")

@app.route("/exams")
def exams():
    return render_template("exams.html")

@app.route("/goodday")
def goodday():
    return render_template("propose.html")

@app.route("/propose")
def propose():
    return render_template("propose1.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/fastforward")
def fastforward():
    return render_template("fastforward.html")

@app.route("/nottheend")
def begin():
    return render_template("nottheend.html")

@app.route("/mvj-days")
def mvj():
    return render_template("mvj.html")

@app.route("/piggy")
def piggy():
    return render_template("piggy.html")

@app.route("/plannings")
def plan():
    return render_template("plannings.html")

@app.route("/goa")
def goa():
    return render_template("goa.html")

@app.route("/classroom")
def classroom():
    return render_template("classroom.html")

@app.route("/final")
def final():
    return render_template("end.html")

if __name__ == "__main__":
    app.run("0.0.0.0",debug=True)
