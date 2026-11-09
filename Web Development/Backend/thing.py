from flask import Flask, Response

#make a new flask app
app = Flask(__name__)

print(app)

app.run(host="127.0.0.1", port="3000", use_reloader=True)