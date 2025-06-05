# Simple Network Port Scanner

## Description

This port scanner allows you to specify a target IP address and a range of TCP ports to scan. It reports which ports are open, helping you understand which services are exposed on a networked device. Port scanning is a foundational skill for penetration testing, vulnerability assessment, and network defense.

---

## Features

- Scans a range of TCP ports on a target host
- Reports open ports
- Fast scanning using threading
- Handles unreachable hosts gracefully
- Simple command-line interface

---

## Installation

1. Ensure you have Python 3 installed.
2. Download or clone this repository.

---

## Usage

Run the script in your terminal:

python simple_port_scanner.py


You will be prompted to enter:
- The target IP address (e.g., 127.0.0.1)
- The start port (e.g., 1)
- The end port (e.g., 1024)



---

## Security Concepts Demonstrated

- TCP/IP networking fundamentals
- Network enumeration and reconnaissance
- Python socket programming
- Threading for faster scans

---

## Improvement Ideas

- Add UDP scanning
- Identify common services on open ports
- Export results to a file
- Add banner grabbing for service detection

---

## What I Learned

- How to use Python’s socket and threading modules
- The basics of port scanning and network enumeration
- The importance of identifying exposed services in cybersecurity

---

## References

- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [Port scanning (Wikipedia)](https://en.wikipedia.org/wiki/Port_scanner)
- [Nmap: the Network Mapper](https://nmap.org/)

---

**For educational and authorized use only. Never scan networks without permission.**
