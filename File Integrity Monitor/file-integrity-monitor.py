#£ File Intregity Monitor


import hashlib
import json

# function to calculate the hash of the file
def calculate_file_hash(file_path):

    sha256_hash = hashlib.sha256()
    # opens the file in binary mode in order to read the file as bytes
    with open(file_path, "rb") as f:
        while True:
            # reads the file in 8192 byte chunks instead of all at once
            data = f.read(8192)

            if not data:
                break
            sha256_hash.update(data)
            # returns final hash as readable string
    return sha256_hash.hexdigest()

# function to create a baseline of the files
def baseline_creation():

    files = input("Enter the file paths to monitor (separated by commas): ").split(",")
    baseline_data = {}

    for file_path in files:
        file_path = file_path.strip()

        try:
            file_hash = calculate_file_hash(file_path)
            baseline_data[file_path] = file_hash
            print(f"File added: {file_path} with hash: {file_hash}")

        except FileNotFoundError:
            print(f"File not found: {file_path}")

    with open("baseline.json", "w") as baseline_file:
        json.dump(baseline_data, baseline_file, indent=4)

    print("Baseline created successfully and saved to baseline.json")

# function to check the intregrity of the files against the baselin
def integrity_check():

    try:
        with open("baseline.json", "r") as baseline_file:
            baseline_data = json.load(baseline_file)
    except FileNotFoundError:
        print("Baseline file cannot be found. Please create a baseline first.")
        return
# loops through the files in the baseline in order 
    for file_path, baseline_hash in baseline_data.items():
        try:
            current_hash = calculate_file_hash(file_path)
            if current_hash != baseline_hash:
                print(f"File integrity has been compromised for {file_path}.")
                print(f"Check the file for any malicious changes ASAP.")
            else:
                print(f"File integrity is intact for {file_path}.")
        except FileNotFoundError:
            print(f"File has not been found. {file_path} may have been deleted or moved.")

# main function to run the file integrity monitor
def main():

    print("---- FILE INTEGRITY MONITOR ----")
    print("1. CREATE BASELINE")
    print("2. CHECK INTEGRITY")
    mainchoice = input("Enter your preferred choice (1 or 2): ")

    if mainchoice == "1":
        baseline_creation()
    elif mainchoice == "2":
        integrity_check()
    else:
        print("Invalid selection. Please choose either 1 or 2.")



if __name__ == "__main__":
    main()