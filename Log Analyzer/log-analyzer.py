def log_analyzer(logfilepath):
    ip_address_failed = {}
    with open(logfilepath, 'r') as log_file:
        for line in log_file:
            if "Failed password" in line:
                parts = line.split("from")
                ip_address = parts[1].strip()
                if ip_address in ip_address_failed:
                    ip_address_failed[ip_address] = ip_address_failed[ip_address] + 1
                else:
                    ip_address_failed[ip_address] = 1
    return ip_address_failed


def main():
    print("---LOG ANALYZER---")
    logfilepath = input("Enter the path to the log file:").strip()
    count_failed = log_analyzer(logfilepath)

    print("IP addresses with failed login attempts:")
    for ip_address in count_failed:
        print(f"{ip_address} has {count_failed[ip_address]} failed login attemps.")

    print("Suspicious IP addresses that have more than 3 failed login attempts:")
    suspicious_found = False
    for ip_address in count_failed:
        if count_failed[ip_address] >= 3:
            print(f"{ip_address} has {count_failed[ip_address]} failed login attemps and is flagged for suspicious activity")
            suspicious_found = True
    if suspicious_found == False:
        print("No IP addresses were flagged for suspicious activity ")


if __name__ == "__main__":
    main()


