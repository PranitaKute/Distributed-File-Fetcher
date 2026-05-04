import requests

servers = [
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002"
]

filename = input("Enter file name: ")

for server in servers:
    try:
        print(f"Trying {server}...")
        r = requests.get(f"{server}/get/{filename}")
        
        if r.status_code == 200:
            with open(filename, "wb") as f:
                f.write(r.content)
            print(f"Downloaded from {server}")
            break
    except:
        print(f"{server} not reachable")

else:
    print("File not found on any server")