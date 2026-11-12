from flask import Flask, app

app=Flask(__name__)

@app.route("/api/grades")
def get_grades():
    return [0,1]

@app.route("/api/people")
def get_people():
    return [
        {"name": "Lynee", "age": 18},
        {"name": "Olive", "age": 22}
    ]

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, use_reloader=True)