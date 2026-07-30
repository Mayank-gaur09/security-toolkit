# Security Toolkit

A collection of Python scripts built to practice core security concepts such as networking scanning, password analysis, log monitoring as well as file integrity checking. Built as a personal project to apply cyber security fundamentals in code to move beyond theory and build practical tools which are relevant for my future in cybersecurity.


## Tool 1: TCP Port Scanner

**File:** port-scanner.py

**Description:** It is a simple port scanner that scans a target's IP address across common network ports (22, 80, 443, 8080) to test if they are open or closed, whcih can indicate potential entry points into a system.


### How it Works:

- Uses python's built in socket library to estabilish TCP connections
- Converts the inputted host names to IP address (For example; *scanme.nmap.org*)
- Uses *s.connect_ex()* to attempt a TCP connection 
- Uses a for loop to iterate through the list of ports and check each one.


### What I learned:

- **Networking Fundamentals:** How TCP connections use ports such as 80 for HTTP and 22 for SSH to route network traffic.
- **Python Networking Programming:** Use of `socket.SOCK_STREAM` to test port states and that it estabilishes a reliable TCP connection.
- Ethical Hacking Principles such as only testing on authorized hostnames such as "localhost" , "scan.nmap.org" or my own network.
