def encrypt_caesar_cipher(text, key_shift):
    output = ""
    for char in text:
        if char.isupper():
            output = output + chr((ord(char) + key_shift - 65) % 26 + 65)
        elif char.islower():
            output = output + chr((ord(char)+ key_shift - 97) % 26 +97)
        else:
            output = output + char
    return output

# decrypting is just encrypting backwards, so we use a negative key shift
def decrypt_caesar_cipher(text, key_shift):
    return encrypt_caesar_cipher(text, -key_shift)

def main():
    print("---CAESAR CIPHER TOOL---")
    choice = input("Would you like to encrypt or decrypt a message? (Input 'encrypt' or 'decrypt'):").strip().lower()
    text = input("Enter your message: ")
    key_shift = int(input("Enter the key shift amount: ").strip())
    if choice == "encrypt":
        output = encrypt_caesar_cipher(text, key_shift)
        print(f"The encrypted message is: {output}")
    elif choice == "decrypt":
        output = decrypt_caesar_cipher(text, key_shift)
        print(f"The decrypted message is: {output}")
    else:
        print("Invalid choice, enter 'encrypt' or 'decrypt'.")



if __name__ == "__main__":
    main()

