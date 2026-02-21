from flask import Flask, request, jsonify, Response

app = Flask(__name__)

def load_full_page():
    # read html
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # read css
    with open("style.css", "r", encoding="utf-8") as f:
        css = f.read()

    # read js
    with open("script.js", "r", encoding="utf-8") as f:
        js = f.read()

    # inject css before </head>
    html = html.replace("</head>", f"<style>{css}</style></head>")

    # inject js before </body>
    html = html.replace("</body>", f"<script>{js}</script></body>")

    return html

@app.route("/")
def home():
    page = load_full_page()
    return Response(page, mimetype="text/html")

@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    response = data.get("response")

    with open("responses.txt", "a") as f:
        f.write(response + "\n")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
