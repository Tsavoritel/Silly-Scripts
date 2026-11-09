from flask import Flask, Response, send_from_directory

#make a new flask app
app = Flask(__name__)

print(app)

@app.route("/home")
def serve_home():
    return send_from_directory("static", "index.html")

@app.route("/plus")
def calculate_sum():
    print("hi")

app.run(host="127.0.0.1", port="3000", use_reloader=True)