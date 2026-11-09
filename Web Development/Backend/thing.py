from flask import Flask, Response, send_from_directory, request
import json

#make a new flask app
app = Flask(__name__)

print(app)

@app.route("/home")
def serve_home():
    return send_from_directory("static", "index.html")

@app.route("/plus")
def calculate_sum():
    try:
        arguments = request.args
        print(arguments)
        number1 = float(arguments.get("number1"))
        number2 = float(arguments.get("number2"))

        response_data = {
            "number1": number1,
            "number2": number2,
            "result": number1 + number2
        }

        return response_data
    except ValueError:
        response = {
            "message": "Argument(s) not a number",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response = json_response, status = 400, mimetype = "applications/json")
        return http_response

#error handler
@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }

    json_response = json.dumps(response)
    #mime type = what sort of data
    http_response = Response(response = json_response, status = 404, mimetype = "application/json")
    return http_response

app.run(host="127.0.0.1", port="3000", use_reloader=True)