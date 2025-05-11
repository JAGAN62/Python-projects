from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "jagan"  # Required for using session

# Function to determine the winner
def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        session['user_count'] += 1
        return "You win!"
    else:
        session['bot_count'] += 1
        return "Computer wins!"

@app.route("/", methods=["GET", "POST"])
def index():
    if "user_count" not in session:
        session["user_count"] = 0
    if "bot_count" not in session:
        session["bot_count"] = 0

    result = None
    user_choice = None
    computer_choice = None

    if request.method == "POST":
        user_choice = request.form.get("choice")
        if user_choice == "reset":
            session["user_count"] = 0
            session["bot_count"] = 0
            return redirect(url_for("index"))
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = get_winner(user_choice, computer_choice)

    return render_template("index.html",
                           result=result,
                           user=user_choice,
                           computer=computer_choice,
                           c1=session["user_count"],
                           c2=session["bot_count"])


if __name__ == "__main__":
    app.run(debug=True)
