import socket
import os
HOST = "0.0.0.0"
PORT = 5000

def response(res):
    rules = res.split("&&")
    response = ""
    for rule in rules:
        response += "<h1>"+rule+"</h1>"
    return "<html><body>"+response+"</html></body>"

def worker(sck,res):
    t = response(res)
    sck.send(bytes("HTTP/1.1 200 OK\r\n", "UTF-8"))
    sck.send(bytes("Content-Type: text/html\r\n", "UTF-8" ) )
    sck.send(bytes("Content-Length: " + str(len(t)) + "\r\n","UTF-8"))
    sck.send(bytes("\r\n", "UTF-8"))
    sck.send(bytes(str(t), "UTF-8"))
    sck.close()

if __name__ == "__main__":
    # set the iptables rule
    print("set the iptables rule!")
    resetIptables = "iptables -F && iptables -t nat -F"
    os.system(resetIptables)
    rule1 = "iptables -A INPUT -p tcp --dport 8888 -j DROP" # reject the port
    rules = rule1
    os.system(rules)
    ssck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ssck.bind((HOST, PORT))
    ssck.listen(1)
    print("server start!")
    while True:
        sck,addr = ssck.accept()
        worker(sck, rules)