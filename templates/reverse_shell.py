import socket

# Safe Test Payload for YARA / Signature Validation
IP = "{{IP}}"
PORT = {{PORT}}

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(b"TEST_BENIGN_CONNECTION\n")
    s.close()
except Exception as e:
    print(f"Connection test complete: {e}")
