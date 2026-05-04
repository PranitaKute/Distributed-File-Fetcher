# Distributed File Fetcher
This is a simple distributed systems project where a client retrieves files from multiple servers.

## Features
- Multiple server nodes
- Client-server communication using HTTP
- Basic fault tolerance
- File retrieval from distributed nodes

## Tech Stack
- Python
- Flask
- Requests

## Project Structure
```text
Distributed_File_Fetcher/
│
├── server1/
│ └── server.py
│
├── server2/
│ └── server.py
│
├── client.py
├── README.md
└── requirements.txt
```

## How It Works
- The client asks the user to enter a file name.
- It sends a request to Server 1.
- If the file is not found, it tries Server 2.
- Once found, the file is downloaded to the client system.
- If no server has the file, an error message is shown.

## Setup Instructions
### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Create test files (IMPORTANT)

#### Inside server1/, create a file:

**file1.txt**

Add content: *"Hello from Server 1"* 

#### Inside server2/, create a file:

**file2.txt**

Add content: *"Hello from Server 2"*

### 3. Run servers

**Terminal 1:**
```
cd server1
python server.py 5001
```

**Terminal 2:**
```
cd server2
python server.py 5002
```

### 4. Run client
```
python client.py
```

Enter file name when prompted (example: file1.txt or file2.txt)

## Concepts Demonstrated
- Client-Server Architecture
- Distributed File Retrieval
- Fault Tolerance (Basic)
- Network Communication using REST APIs
