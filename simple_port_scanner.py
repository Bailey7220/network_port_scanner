import socket
import threading

def scan_port(host, port, results):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        results[port] = True
    except:
        results[port] = False
    finally:
        s.close()

def main():
    host = input("Enter target IP address (e.g., 127.0.0.1): ")
    start_port = int(input("Enter start port (e.g., 1): "))
    end_port = int(input("Enter end port (e.g., 1024): "))

    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")
    results = {}
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    open_ports = [port for port, is_open in results.items() if is_open]
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"  - {port}")
    else:
        print("No open ports found in the specified range.")

if __name__ == "__main__":
    main()
