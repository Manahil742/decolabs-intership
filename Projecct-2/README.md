## Project Overview
The **Expense Tracker** is a simple command-line program that helps a user
record their daily expenses and instantly see how much they have spent in
total. It was built to practice and demonstrate core Python fundamentals
taught early in the DecodeLabs training program.

This project focuses on **understanding**, not complexity — every part of
the code uses only basic Python building blocks.

## Concepts Practiced
| Concept | Where it's used |
|---|---|
| Variables | `total`, `expense_count`, `expense` |
| Loops (`while`) | Keeps the menu running until the user exits |
| Conditional statements (`if / elif / else`) | Menu choice handling, input validation |
| Accumulator pattern | `total = total + expense` |
| Functions | `add_expense()`, `view_total()`, `show_menu()`, `main()` |
| Mathematical operations | Addition (total), Division (average expense) |
| Error handling | `try / except` for invalid (non-numeric) input |
| Lists | Storing every entered expense in `expense_list` |

##  Features

1. **Add Expense** – Enter any number of expenses, one at a time.
2. **View Total Spent** – See the total amount, number of expenses, and
   average expense.
3. **Exit** – Cleanly ends the program.
4. Basic input validation (rejects negative amounts and non-numeric text).
