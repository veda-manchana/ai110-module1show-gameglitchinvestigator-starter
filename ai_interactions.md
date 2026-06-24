# AI Interactions Log

> This file documents how AI tools (Cursor Agent / Copilot) were used to debug, refactor, test, and improve the Game Glitch Investigator project.

---

## Agent Workflow (SF8)

**What task did you give the agent?**

I used Cursor Agent to fix multiple bugs in the Streamlit guessing game. The main issues were inconsistent scoring logic, incorrect hint behavior ("Too High" / "Too Low"), attempt counter errors, difficulty balance problems, and the "New Game" button not resetting the game properly. I also asked it to standardize the game rules so the number range stayed consistent (1–100) across all components.

**What did the agent do?**

- Refactored core logic into `logic_utils.py`
- Fixed `check_guess()` so hint outputs correctly match the secret number
- Fixed attempt tracking so attempts only update correctly per valid guess
- Fixed scoring system:
  - Wrong guess → -2 points
  - Correct guess → bonus score based on number of attempts used
- Fixed "New Game" functionality:
  - resets secret number
  - resets attempts
  - resets history
  - resets game status
- Standardized difficulty settings:
  - Easy → more attempts
  - Normal → medium attempts
  - Hard → fewer attempts
- Ensured consistent game range (1–100) everywhere

**What did you have to verify or fix manually?**

- Verified Streamlit session_state was not persisting old values after reset
- Checked attempt counter off-by-one behavior (fixed by adjusting increment timing)
- Tested scoring manually to ensure it didn’t accumulate incorrectly across games
- Ran multiple game sessions to confirm stability instead of trusting only code changes

---

## Test Generation (SF7)

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Correct guess | "Generate pytest for winning condition in number guessing game" | check_guess(50, 50) returns "Win" | Yes | Confirms win condition works correctly |
| Too high guess | "Test high guess vs secret number" | check_guess(60, 50) returns "Too High" | Yes | Ensures hint logic is correct |
| Too low guess | "Test low guess vs secret number" | check_guess(40, 50) returns "Too Low" | Yes | Ensures comparison logic works correctly |

---

## Linting & Style (SF9)

**Prompt used:**
Fix this Streamlit guessing game to follow PEP 8 style guidelines. Do not change gameplay logic. Improve readability, naming consistency, spacing, and structure. Identify any style issues.


**Linting output before:**
- Inconsistent variable naming in early versions (attempt counter vs attempt_limit confusion)
- Mixed UI and logic inside `app.py`
- Some long inline expressions in session_state updates
- Repeated logic blocks instead of reusable functions

**Changes applied:**
- Moved core logic into `logic_utils.py`
- Standardized naming conventions (snake_case throughout)
- Improved spacing and readability across functions
- Clean separation between UI (Streamlit) and logic layer
- Fixed attempt counting logic to avoid off-by-one errors
- Ensured consistent structure across all difficulty levels

---

## Model Comparison (SF11)

**Task given to both models:**

Fix scoring system, hint logic, attempt tracking, and reset behavior in a Streamlit number guessing game.

|  | Cursor Agent | Copilot |
|--|--------------|----------|
| **Model name** | Cursor Agent | Copilot |
| **Response summary** | Direct multi-file edits and working fixes | Step-by-step explanations and debugging guidance |
| **More Pythonic?** | Yes | Medium |
| **Clearer explanation?** | Medium | Yes |

**Which did you prefer and why?**

I preferred Cursor Agent because it directly applied changes across multiple files and quickly fixed real bugs in the working code. Copilot was more helpful for understanding why the bugs were happening and how the logic should work.

---

## Summary

Using AI helped me:
- Identify logic bugs faster
- Refactor code into cleaner structure
- Fix scoring and attempt tracking issues
- Improve overall game stability
- Learn how Streamlit state behaves during reruns