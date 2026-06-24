# logic_utils.py

def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📈 Your guess is too high. Try LOWER."
    else:
        return "Too Low", "📉 Your guess is too low. Try HIGHER."


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        # reward faster wins
        points = max(10, 100 - (attempt_number * 10))
        return current_score + points

    if outcome in ["Too High", "Too Low"]:
        # small penalty for wrong guesses
        return current_score - 2

    return current_score