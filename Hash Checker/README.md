# Tool 2: Hash Checker 

File: [Python Hash Checker](./hash-checker.py)

**Description:** The hash checker reads a file and generates a specific cryptographic hash which is a unique value for the file's contents. If even a byte of the file changes then the hash changes completely. Hash checkers are used in the real world to check if a downloaded file has not been corrupted or tampered with by comparing it against a known hash given by the user.


## How it works:

- The script asks the user for the file path and the hash alogirthim (sha1, sha256, md5).
- The script calculates the hash of the file through python's in built hash library and reads the file in binary. 
- 

