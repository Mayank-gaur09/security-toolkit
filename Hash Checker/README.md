# Tool 2: Hash Checker 

**File:** [Python Hash Checker](./hash-checker.py)

**Description:** The hash checker reads a file and generates a specific cryptographic hash which is a unique value for the file's contents. If even a byte of the file changes then the hash changes completely. Hash checkers are used in the real world to check if a downloaded file has not been corrupted or tampered with by comparing it against a known hash given by the user.


## How it works:

- The script asks the user for the file path and the hash alogirthim (sha1, sha256, md5).
- The script calculates the hash of the file through python's in built hash library and reads the file in binary. 
- The hash is then displayed.
- The user can also compare the hash with a hash of their own to check if the file has been altered.


## What I learned:

- How cryptographic hash functions work and how they're used to verify file integrity.
- Using pythons hash library and hash objects to support multiple hash algorithms at once.
- Basic error handling using try/except.
- The use of "if __name__ == "__main__": main()" to make sure the script is ran directly and not when it is an import.

## Expected Outcome:
*using hash-checker.py as the target file*










## How to run the program

1. Clone the repo in terminal

`git clone https://github.com/Mayank-gaur09/security-toolkit.git`

`cd "security-toolkit/Hash Checker"`

2. Run the script

`python3 hash-checker.py`

3. Enter your file path and hash algorithm of choice.

4. Optionally enter the hash to compare against.



