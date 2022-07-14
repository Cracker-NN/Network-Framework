import socket



class HoneyPot:
    def honeypot(self, ip, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((ip, 80))
        sock.listen(5)
        try:
            while 1:
                newSocket, addresss = sock.accept()
                ip = addresss[0]
                portS = addresss[1]
                print ("\nHost IP Found:", ip)
                print("Host Port Found:", portS)
                receivedData = newSocket.recv(1024)
                if not receivedData:
                    break
                print("\a\a\a")
                print(receivedData.decode('utf-8').replace('User-Agent', 'Victim System Info'))
                newSocket.send( bytes(data, 'utf-8') )
                break
            newSocket.close()
        finally:
            sock.close()
    
