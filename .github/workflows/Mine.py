from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>For Someone Special ❤️</title>
    <style>
        body {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            font-family: Arial, sans-serif;
            text-align: center;
            color: white;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container {
            background: rgba(0,0,0,0.3);
            padding: 40px;
            border-radius: 20px;
        }

        button {
            padding: 15px 25px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            margin: 10px;
        }

        .yes { background: #00e676; color: white; }
        .no  { background: #ff1744; color: white; position: relative; }
    </style>
</head>
<body>

<div class="container">
    <h1>Hey ❤️</h1>
    <p>From the moment I met you, my world became beautiful 🌹</p>
    <h2>Will you be mine forever?</h2>

    <button class="yes" onclick="sendAnswer('YES')">YES 💖</button>
    <button class="no" onclick="moveNo()">NO 😢</button>

    <p id="result"></p>
</div>

<script>
function sendAnswer(answer) {
    fetch("/answer", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({response: answer})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            "Yay!!! ❤️ I love you forever 💍";
    });
}

function moveNo() {
    let btn = document.querySelector(".no");
    let x = Math.random() * 300 - 150;
    let y = Math.random() * 200 - 100;
    btn.style.transform = `translate(${x}px, ${y}px)`;
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_page)

@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    response = data.get("response")

    with open("responses.txt", "a") as f:
        f.write(response + "\\n")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)