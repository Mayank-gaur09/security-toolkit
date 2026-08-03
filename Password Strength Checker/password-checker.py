def password_strength(password):
    length = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower()for char in password)
    number = any(char.isdigit()for char in password)
    symbol = any(not char.isalnum() for char in password)

    points = sum([length, uppercase, lowercase, number, symbol])

    if points == 5:
        strength = "Strong"
    elif points >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"


    return strength, {

        "Does the password have atleast 8 characters:": length,
        "Does the password have atleast 1 uppercase letter:": uppercase,
        "Does the password have atleast 1 lowercase letter:": lowercase,
        "Does the password have atleast 1 number:": number,
        "Does the password have atleast 1 symbol:": symbol,
    }


def main():
    print("---PASSWORD STRENGTH CHECKER---")
    password = input("Enter the password to evaluate its strength:").strip()
    strength, criteria = password_strength(password)

    print(f"The password strength is: {strength}")
    print("Password Strength Criteria:")
    for rules, met in criteria.items():
        result = "Met" if met else "Not Met"
        print(f"{rules} {result}")



if __name__ == "__main__":
    main()

