
import socket

file_name = "data.csv"

# fields = []
rows = []


def server_program():
    # get the hostname
    host = '10.2.136.106'
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
       server_socket.bind((host, port))  # bind host address and port together

   
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:


        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        connection.send(data_information.encode())


    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()