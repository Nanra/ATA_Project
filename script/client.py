import socket


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))


    pesan = raw_input("\n->")

    if len(pesan) == 0:
        pesan = raw_input("\n->")
        while len(pesan) == 0:
            pesan = raw_input("\n->")
            while (pesan != 'q'):
                if len(pesan) == 0:
                    pesan = raw_input("\n->")

                else:
                    s.send(pesan)
                    data = s.recv(10214)
                    print 'Diterima oleh server :' + str(data)
                    pesan = raw_input("\n->")
                    if len(pesan) == 0:
                        pesan = raw_input("\n->")
            s.close()
    else:
        while pesan !='q':
            s.send(pesan)
            data = s.recv(10214)
            print 'Diterima oleh server :' + str(data)
            pesan = raw_input("\n->")
            if len(pesan) == 0:
                    pesan = raw_input("\n->")
        s.close()

if __name__ == '__main__':
    Main()

