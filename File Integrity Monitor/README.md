# Tool 6: File Integrity Monitor

**File**: [file-integrity-monitor.py

**Description:** The file integrity monitor checks whether a file has been modified by comparing it's hash against a hash taken earlier. The user inputs a set of file or files they want to check, the tool saves their hashes into the baseline file and later you can run a check to see if there has been any changes to your file when compared against the baselin. It helps detect malicious changes to the file that were not done by you.


## How it Works:

- The script gives the user an option whether to check the file integrity or create a baseline.
- When creating the baseline, the user types in the file path's they want to monitor, and the tool hashes each one wih SHA256 and saves the results to the `baseline.json`
- When checking the integrity, the tool loads the saved baseline, hashes the files again and compares the hashes, if the hashes don't match then there has been changes to the file. If a file is missing entirely, its been deleted or moved.
- Files are read in 8192 byte chunks instead of all at once to reduce memory usage.


## What I learned

- I reused the hashing logic from my Hash Checker tool but for a different purpose, checking files over time to detect changes instead of just once.
- Reading files in smaller byte chunks instead of loading the whole file into memory at once.
- Using JSON to save data so it's still there the next time you run the script.
- Debugging real bugs in my code, including a type mismatch from comparing an integer against a string and etc.


## Expected Outcome

*created a baseline for the included sample file, then edited the file and checked it again.* 



<img width="780" height="240" alt="image" src="https://github.com/user-attachments/assets/b6a37444-0699-49e9-a08a-e47bf20b52f6" />




*after editing the file*
<img width="660" height="135" alt="image" src="https://github.com/user-attachments/assets/e569dbb8-c636-4db0-be13-acd75903ca05" />



## How to run the program:

1. Clone the repo in terminal

`git clone https://github.com/Mayank-gaur09/security-toolkit.git`

`cd security-toolkit/File Integrity Monitor`

2. Run the script

`python3 file-security-monitor.py`

3. Pick option 1 to create the baseline and save the hash/hashes. Use the included "sample_file.txt" for the file path so you can try it straight away.

4. Edit the sample_file.txt

5. Run the script again and pick option 2, the file should come up as compromised.









