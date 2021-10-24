import time
import socketserver


class DemoTcpRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print("Sending Data Package: ASELS:26.70|")
            self.request.sendall(b"ASELS:26.70|")
            time.sleep(1)


if __name__ == '__main__':
    with socketserver.TCPServer(("localhost", 8081), DemoTcpRequestHandler) as demo_tcp_server:
        print("Demo Tcp Server Started!")
        demo_tcp_server.serve_forever()
