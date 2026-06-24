# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it looked like a normal number guessing game, but multiple core systems were inconsistent or broken.

Two major bugs I noticed were:
- The hint system sometimes gave inconsistent or incorrect feedback (Too High / Too Low did not always match the secret logic).
- The attempt counter was off, which caused incorrect scoring and sometimes early game ending behavior.
- The "New Game" button did not fully reset state correctly in some runs, causing leftover state issues.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|------|------------------|----------------|------------------------|
| Guess: 50 (secret = 30) | "Too High" | Sometimes incorrect or inconsistent hint feedback | None |
| Guess: 20 (secret = 45) | "Too Low" | Sometimes incorrect or inconsistent hint feedback | None |
| Click "New Game" multiple times | Secret resets cleanly and attempts reset properly | Secret sometimes persists or state behaves inconsistently | None |
| Multiple guesses in a row | Attempt counter increases by 1 each time | Attempt count off by 1 leading to scoring mismatch | None |
| Correct guess (19) | Game ends and displays win state with correct score | Score sometimes inconsistent due to attempt mismatch | None |

---

## 2. How did you use AI as a teammate?

I used ChatGPT and the Streamlit documentation while debugging this project. I also used AI inside my coding workflow to help explain why Streamlit session state was behaving unexpectedly.

One correct AI suggestion was about Streamlit reruns and session_state. The AI explained that every button click reruns the entire script, and that variables must be stored in `st.session_state` to persist correctly. I verified this by observing that moving values into session_state stopped the secret number from resetting.

One incorrect or misleading suggestion was assuming the attempt counter logic was correct and only needed UI adjustment. In reality, the issue was that attempts were being incremented before validation, which caused off-by-one scoring errors. I confirmed this by printing debug values and observing incorrect scoring behavior during gameplay.

---

## 3. Debugging and testing your fixes

I verified each bug fix by running the Streamlit app manually and checking the Developer Debug Info panel after each guess. I also tested edge cases like repeated guesses, invalid inputs, and rapid button clicks.

For automated testing, I used pytest to ensure that core logic functions like `check_guess`, `parse_guess`, and `update_score` returned correct outputs. These tests helped confirm that the logic layer worked independently of the UI.

AI helped me design test cases by suggesting edge cases like invalid input strings, boundary values (1 and 100), and repeated guesses, which improved test coverage.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the entire script every time a user interacts with a widget like a button or input field. Because of this, normal variables do not persist between interactions.

To maintain game state, I had to use `st.session_state`, which acts like persistent memory across reruns. Without it, variables like the secret number and attempts would reset every time the user clicked a button.

---

## 5. Looking ahead: your developer habits

One habit I will reuse is using debug printouts (like the Developer Debug Info panel) to track state changes in real time. This made it much easier to identify state and scoring issues.

Next time I work with AI, I would ask more targeted questions instead of accepting full code suggestions immediately. I would also validate logic step-by-step instead of assuming correctness.

This project changed how I think about AI-generated code because I now see that AI can produce working-looking applications that still contain subtle logic bugs. Careful testing and debugging are still required even when code runs successfully.