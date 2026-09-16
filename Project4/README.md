##  Project Objective

The **Project-4** is a simple console program that asks the
user 3 general knowledge questions, checks each answer against the
correct one, and calculates a final score out of 3. It was built to
practice `if-else` decision-making and score accumulation using
variables — the two concepts this project specifically focuses on.

---

##  Concepts Practiced

| Concept | Where it's used |
|---|---|
| Variables | `score = 0`, `answer1`, `answer2`, `answer3` |
| Input | `input("Your answer: ")` for each question |
| If-Else logic | Comparing each answer to the correct answer |
| String normalization | `.strip().lower()` to handle spacing and case |
| Score accumulation | `score = score + 1` for every correct answer |
| f-strings | `f"Your final score: {score}/3"` for the result |

---

##  Technologies Used

- **Python 3** (no external libraries required — built-in functions only)

---

##  Features

1. Asks exactly **3 general knowledge questions**.
2. Accepts the user's answer for each question.
3. Normalizes answers with `.strip().lower()` so that `Paris`, `paris`,
   and `PARIS ` are all accepted as correct.
4. Displays **"Correct! +1 point"** or **"Wrong answer!"** immediately
   after each question.
5. Tracks the score using a simple accumulator variable.
6. Displays the final score out of 3 at the end, using an f-string.

---
