from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/submit-data/")
def data_feed():
    return render_template('submit-data.html')

@app.route("/talk/")
def talk():
    return render_template('talk.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)