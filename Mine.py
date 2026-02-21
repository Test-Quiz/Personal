from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    response = data.get("response")

    # save response in file
    with open("responses.txt", "a") as f:
        f.write(response + "\n")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
