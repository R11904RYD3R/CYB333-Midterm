import socket
import time

allowed_targets = ["127.0.0.1", "localhost", "scanme.nmap.org"]

target = input("Enter target: ")

if target not in allowed_targets:
    print("Error: You can only scan 127.0.0.1, localhost, or scanme.nmap.org")
    exit()

try:
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Error: Ports must be between 1 and 65535.")
        exit()

    print(f"\nScanning {target} from port {start_port} to {end_port}\n")

    for port in range(start_port, end_port + 1):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)

        result = scanner.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

        scanner.close()
        time.sleep(0.2)

    print("\nScan complete.")

except ValueError:
    print("Error: Please enter numbers only for ports.")

except Exception as error:
    print("Scanner error:", error)