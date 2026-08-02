import hashlib

def hash_checker(file_path, hash_algorithm):
    # opens the file in binary and reads its contents
    with open(file_path, 'rb') as myfile:
        file_data = myfile.read()
        # Creates a hash object using the given hash algorithm and updates it with file data
    hash_obj = hashlib.new(hash_algorithm)
    hash_obj.update(file_data)
    return hash_obj.hexdigest() # returns into a readable hex string


def main():
    print("FILE HASH CHECKER:")
    file_path = input("Enter the path to the file: ").strip() # Asks user for the file path
    hash_algorithm = input("Enter the hash algorithm: ").strip().lower() # Asks user for hash algorithm

    if hash_algorithm == "":
        hash_algorithm = "sha256"

    # checks if the user input is valid
    try:
        result = hash_checker(file_path, hash_algorithm)
    except FileNotFoundError:
        print("Error: The file was not found, try again with the correct file path.")
        return
    except ValueError:
        print("Error: Hash algorithm is not valid, try again with a valid hash algorithm.")
        return

    # displays the hash to the user
    print(f"The {hash_algorithm.upper()} hash of the file is: {result}")

    # Asks user if they want to compare the hash with another hash
    hash_comparision = input("Do you want to compare the hash with another hash? (yes/no):").strip().lower()
    if hash_comparision == "yes":
        user_hash = input("Enter the hash to compare:").strip().lower()
        if user_hash == result:
            print("The hashes match, the file is intact.")
        else:
            print("The hashes do not match, the file could have been altered or tampered with.")



if __name__ == "__main__":
    main()

