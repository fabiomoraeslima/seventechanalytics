from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("index.html")

@app.route('/home')
def home():
    return redirect(url_for('principal'))

@app.route('/databricks')
def databricks():
    return render_template("databricks.html")

@app.route('/pyspark')
def pyspark():
    return render_template("pyspark.html")

@app.route('/sql')
def sql():
    return render_template("sql.html")

@app.route('/python')
def python():
    return render_template("python.html")

@app.route('/linguagemweb')
def linguagemweb():
    return render_template("linguagemweb.html")


if __name__ == "__main__":
    app.run()