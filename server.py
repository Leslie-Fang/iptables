import socket
HOST = "0.0.0.0"
PORT = 8888

def response():
    return "<html><body><h1>Hello World</h1></html></body>"

def worker(sck):
    t = response()
    sck.send(bytes("HTTP/1.1 200 OK\r\n", "UTF-8"))
    sck.send(bytes("Content-Type: text/html\r\n", "UTF-8" ) )
    sck.send(bytes("Content-Length: " + str(len(t)) + "\r\n","UTF-8"))
    sck.send(bytes("\r\n", "UTF-8"))
    sck.send(bytes(str(t), "UTF-8"))
    sck.close()

if __name__ == "__main__":
    ssck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ssck.bind((HOST, PORT))
    ssck.listen(1)
    print("server start!")
    while True:
        sck,addr = ssck.accept()
        worker(sck)