# Tool 5: Caesar Cipher Tool

**File:** [Caesar Cipher Tool](./caesar-cipher.py)

**Descryption:** It is a python tool that encrypts and decrypts text using the caesar cipher which is one of the oldest encryption methods named after Julius Caesar, it shifts each letter by a fixed number of positions in the alphabet.

## How it works:

- The user chooses whether to encrypt or decrypt, enters a message and choose the number to shift it by.
- Each alphabet is converted into it's ASCII character code and is then shifted by the chosen amount and converted back into a letter (However, symbols and numbers are left unchanged.).

## What I learned:

- Use caesar cipher works as a basic encryption technique
- Using `ord()` and `chr()` to convert between letters and their ASCII character codes.
- Using the same function for both encryption and decryption by just reversing the sign of the shift amount.
- That this encryption technique is weak by mordern standards since it only has 25 key shifts.

## Expected Outcomes:

<img width="1000" height="230" alt="image" src="https://github.com/user-attachments/assets/520e95a6-f11f-44cc-bc44-27957a9c3af6" />


## How to run:

1. Clone the repo in terminal

`git clone https://github.com/Mayank-gaur09/security-toolkit.git`

`cd "security-toolkit/Caesar Cipher Tool"`

2. Run the Script

`python3 caesar-cipher.py`

3. Choose encrypt or decrypt, enter your message and the shift amount.
