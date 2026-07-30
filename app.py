import random
import os


from flask import Flask, request, render_template_string, session
import random

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "local-practice-key")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Number Guessing Game</title>

    <style>
    body {
        background-color: black;
        color: white;
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 80px;
        font-size: 26px;
    }

    h1 {
        font-size: 56px;
    }

    input {
        padding: 18px;
        font-size: 28px;
        border: 2px solid white;
        border-radius: 10px;
        width: 180px;
    }

    button {
        padding: 18px 28px;
        font-size: 28px;
        background-color: white;
        color: black;
        border: none;
        border-radius: 10px;
        cursor: pointer;
    }

    strong {
        color: red;
        font-size: 32px;
    }

    a {
        color: white;
        font-weight: bold;
        font-size: 24px;
    }
    .creator {
    position: fixed;
    bottom: 20px;
    left: 20px;
    color: pink;
    font-size: 18px;
    margin: 0;
}

</style>
</head>
<body>
    <h1>Number Guessing Game</h1>
    <p>I am thinking of a number from 1 to 100.</p>

    <p><strong>{{ message }}</strong></p>
    <p>Attempts: {{ attempts }}</p>

    <form method="post">
        <input type="number" name="guess" min="1" max="100" required>
        <button type="submit">Guess</button>
    </form>

    <br>
    <a href="/restart">Play again</a>
    <p class="creator">Created by Saishaaa.</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def game():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0

    message = "Make your first guess!"

    if request.method == "POST":
        guess = int(request.form["guess"])
        session["attempts"] += 1

        if guess < session["number"]:
            message = "Too low!"
        elif guess > session["number"]:
            message = "Too high!"
        else:
            message = f"You won! The number was {session['number']}."

    return render_template_string(
        HTML,
        message=message,
        attempts=session["attempts"]
    )

@app.route("/restart")
def restart():
    session.clear()
    return '<script>window.location.href="/"</script>'

if __name__ == "__main__":
    app.run(debug=True)
    
