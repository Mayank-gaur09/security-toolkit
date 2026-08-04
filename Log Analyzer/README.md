# Tool 4: Log Analyzer

**File:**

**Description:** This tool reads through a log file line by line and counts any failed login attempts as well as the IP address it came from and also flags hem with 3 or more failures. It is helpful to spot brute force attacks.

## How it works:

- The user provides the file path to the log file.
- The script then reads the file line by line looking for the keyword "Failed password"
- It extracts the IP address and counts how many failed login attempts it has.
- Any IP address with more than 3 failed login attempts is flagged as suspicious activity.

## What I learned:

- Why brute-force login attempts are detected by looking for repeated failures from the same source, and how real tools like fail2ban use a similar concept.
- Looping through a dictionary's keys and using that key to look upits value (`counts[ip]`)

## Expected Outcome:




## How to run:

1. Clone the repo in terminal

   `git clone https://github.com/Mayank-gaur09/security-toolkit.git`

   `cd "security-toolkit/Log Analyzer"`

2. Run the script

   `python3 log-analyzer.py`

3. Enter the log file path when prompted 