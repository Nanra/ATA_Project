import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    print "\nManunggu Koneksi..."
    c, addr = s.accept()
    print ("Terhubung dengan : ") + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "\nDari User : " + str(data)
        data = str(data).upper()
        print "Mengirim :"+str(data)
        c.send(data)

    c.close()
if __name__ == '__main__':
    main()

