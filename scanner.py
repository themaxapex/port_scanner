import sys
import socket
import threading
from datetime import datetime
# create tcp connection base on ipv4, set timeout for spped up the scanning, error handling  
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"port {port} is open.")
            s.close()
    except socket.error as e:
        print(f"there is an error on {port}: {e}.")
    except Exception as e:
        print(f"there is exception error {port} {e}.")
# check command line arguments
def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("print invalid number of argument.")
        print("usage: python.exe scanner.py <target>")
        sys.exit(1)

    # resolve hostname
    try:
        target_ip = socket.gethostbyname(target)
        print(f"this is your {target_ip}")
    except socket.gaierror:
        print(f"Error: unable to reolve hostname {target}")
        sys.exit(1)

#print banner/info
    print("_" * 50)
    print(f"Scanning Target {target_ip}")
    print(f"time started {datetime}")
    print("_" * 50)

#start scanning using mutlithreading
    try:
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\nexiting program")
        sys.exit(0)
    except socket.error as e:
        print(f"socket error {e}")
    print("scan completed")

if __name__ == "__main__":
    main()








