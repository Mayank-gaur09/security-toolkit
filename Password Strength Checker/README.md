# Tool 3: Password Strength Checker

**File:**

**Description:** This tool evaluates the strength of a password against five common strength criteria; The minimum length and whether it contains uppercase letters, lowercase letters, numbers and symbols. Depending on how many criteria are met, the script rates the password as Weak, Mediocre or Strong.

## How it works:

- The user enters a password to check it's strength.
- The script checks the password against 5 rules using Pythons string methods.
- Each Rule that passes adds to an overall score.
- The script then displays the overall strength rating and a checklist showing what rules were met.

## What I learned:

- Using python string methods to check what type of characters a string contains.
- Using a dictionary to pair each rule's description with its pass/fail result, and looping through both at once with `.items()`
- The limits to this password checker since it can't detect weak password like "Password1!" which is very weak but will pass all 5 criterions.

## Expected Outcome:






## How to run:

1. Clone the repo in terminal
   `git clone https://github.com/Mayank-gaur09/security-toolkit.git`
   `cd "security-toolkit/Password Strength Checker"`

2. Run the script
   `python3 password-checker.py`

3. Enter a password to check













##