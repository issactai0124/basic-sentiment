from flask import Flask, request, render_template
from model import predict
import json

# create the flask object
app = Flask(__name__)

# home: display a simple page for query
@app.route('/', methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        query = request.form.get('query')
        result = predict.predict(query)
    print(f"before rendering: result = {result}")
    return render_template("home.html", feedback=result)

@app.route('/number/<int:number>')
def number(number):
    return f"number = {number}"

# an end-point for query
@app.route('/run', methods=['GET'])
def run():
    query = request.args.get('query')
    if query == None:
        return json.dumps({"error": "Please specify query!"})
    else:
        prediction = predict.predict(query)
    return json.dumps(prediction)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)