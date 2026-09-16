##  Project Objective

The **Random Password Generator** is a console-based program that creates
strong, random passwords based on a length chosen by the user. It was
built to practice string manipulation, the `random` module, input
validation, and function-based program design — all core skills from
the early stages of the DecodeLabs training program.

---

##  Concepts Practiced

| Concept | Where it's used |
|---|---|
| Variables | `length`, `password`, `CHARACTER_POOL` |
| Loops (`for`, `while`) | Building the password character by character; repeating the program |
| Conditional statements (`if`) | Validating length input, deciding whether to generate another password |
| Functions | `get_valid_length()`, `generate_password()`, `show_header()`, `main()` |
| String manipulation | Combining character sets, `"".join()` |
| `random` module | `random.choice()` for random character selection |
| `string` module | `string.ascii_uppercase`, `string.ascii_lowercase`, `string.digits` |
| Input validation | Rejecting non-numeric input and out-of-range lengths |

---

##  Technologies Used

- **Python 3** (no external libraries required)
- Built-in `random` module — for random selection
- Built-in `string` module — for ready-made character sets

---

##  Features

1. Asks the user for their desired password length.
2. Validates the input so only a whole number between **4 and 32** is
   accepted.
3. Generates a random password using a mix of:
   - Uppercase letters (A–Z)
   - Lowercase letters (a–z)
   - Numbers (0–9)
4. Displays the generated password clearly.
5. Lets the user generate multiple passwords in one session without
   restarting the program
