# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and the game initially had multiple bugs.

- The hints were inconsistent
- The attempt counter was incorrect
- The secret number reset unexpectedly
- Scoring behaved unpredictably
- New Game did not reliably reset state

---

## 🛠️ Setup

1. Install dependencies:
```bash
pip install -r requirements.txt

2. Run the app:
python -m streamlit run app.py

---

## 🕵️‍♂️ Bugs Found

During testing, I identified and fixed the following issues:

- Inconsistent hints ("Too High" / "Too Low")
- Attempt counter bug causing early or incorrect game ending
- New Game not fully resetting state
- Score inconsistencies across guesses and games
- Difficulty levels not properly balanced
- Number range inconsistently applied across code

---

## 🛠️ Fixes Applied

I fixed the game by:

- Standardizing number range to 1–100 everywhere
- Fixing check_guess() so hints always match correct logic:
   guess > secret → "Too High"
   guess < secret → "Too Low"
- Fixing attempt tracking to prevent off-by-one errors
- Ensuring New Game resets all state correctly:
   secret number
   attempts
   score
   history
   status
- Updating scoring logic:
   Wrong guess → -2 points
   Correct guess → bonus score based on attempts used
   Fixing difficulty system:
   Easy → most attempts (12)
   Normal → medium attempts (8)
   Hard → few attempts (5)
- Refactoring logic into logic_utils.py for cleaner structure

---

## 📸 Demo Walkthrough
- User selects difficulty (Normal)
- Game generates a secret number between 1–100
- User enters guesses and receives correct hints ("Too High" / "Too Low")
- Score updates correctly after each guess (-2 for wrong guesses, bonus on win)
- When correct number is guessed, game ends and displays final score

1. User selects Normal difficulty
2. Game generates a secret number between 1 and 100 (e.g., 19)
3. User enters guess 50
4. Game responds: "Too High 📈"
5. Score decreases by -2
6. User enters guess 10
7. Game responds: "Too Low 📉"
8. Score decreases by -2
9. User enters guess 25
10. Game responds: "Too High 📈"
11. Score decreases by -2
12. User enters guess 19
13. Game responds: "🎉 Correct!"
14. Bonus score is added based on attempts used
15. Game ends and displays final score (e.g., Final Score: 54)
16. User clicks New Game 🔁
17. Secret number resets
18. Attempts reset
19. Score and history reset correctly

---

## 🧪 Test Results

All automated tests passed successfully:

pytest tests/
=========================== test session starts ===========================
collected 6 items

tests/test_game_logic.py ......                                     [100%]

============================ 6 passed in 0.11s ============================

---

## 🚀 Stretch Features
- Added enhanced scoring system (penalty + bonus logic)
- Improved UI debugging panel (Developer Debug Info)
- Clean separation of logic into logic_utils.py
- Improved game stability across reruns in Streamlit

---

## 📚 What I Learned
- How Streamlit session_state controls persistent variables
- How small logic bugs can break game consistency
- Why separating logic from UI improves debugging
- How AI tools help refactor and fix multi-file projects faster

---

## 🧠 Reflection Summary (Short)

This project helped me understand how AI-generated code can contain subtle logic bugs. I learned how to debug state issues in Streamlit, improve modular design by separating logic into logic_utils.py, and validate fixes using both manual testing and automated pytest cases.

I also learned that AI tools are helpful for debugging, but human verification is required to confirm correctness.
