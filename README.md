# Robust Contact Manager — Module 5

## Project overview

This is a simple command-line contact manager built for my Python course. It lets a user add, find, and delete contacts. I updated the original starter program so that common mistakes do not cause it to crash.

## What I fixed

- **Invalid menu input:** The original menu did not convert input into an integer. I now use `int()` inside `try/except ValueError`, so entering a letter shows a helpful message and returns to the menu.
- **Missing contact when searching:** A name that is not in the dictionary used to raise `KeyError`. The updated `find_contact()` catches the error, displays **Contact not found.**, and returns `None`.
- **Missing contact when deleting:** The updated `delete_contact()` catches `KeyError` instead of crashing.
- **Duplicate contacts:** I added a custom `DuplicateContactError`. `add_contact()` raises it when the name already exists, and `main()` catches it and prints a message.
- **Empty fields:** The menu also checks that names and phone numbers are not blank when adding contacts.
- **Missing tests:** The project now includes six automated unit tests using `unittest`.

## Project files

- `buggy_contacts.py` — original starter script, kept for comparison
- `contact_manager.py` — corrected contact manager
- `test_contact_manager.py` — six unit tests
- `README.md` — project explanation and instructions

## How to run

You need Python 3. No extra packages are required.

1. Open this folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Run the contact manager:

   ```bash
   python contact_manager.py
   ```

   If your computer uses `python3`, run `python3 contact_manager.py` instead.

4. Choose **1** to add, **2** to find, **3** to delete, or **4** to exit.

## How to test

Run the following command from the project folder:

```bash
python -m unittest test_contact_manager.py
```

The six tests cover adding, finding, and deleting contacts, missing contacts, and duplicate names. `setUp()` clears the contact dictionary before every test so that each test starts fresh. The tests check both successful operations and error situations.

## Test-driven development approach

The intended workflow for each change is to write a test for the behavior, run it to see it fail with the old code, implement the improvement, and rerun the test to confirm the fix. The included tests document the expected behavior of the finished program.

## Screencast (3–5 minutes)

**Video link:** [Add the link to my recorded screencast here before submission]

In the video, I demonstrate the menu, invalid input, missing names, duplicate contacts, the exception-handling code, and the six passing unit tests.
