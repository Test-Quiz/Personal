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