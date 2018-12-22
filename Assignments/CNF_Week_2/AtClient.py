
import socket


def client_program():
    host = '10.2.136.106'  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input("Secret Question")
	print(printp)
	soc.send(message.encode())
	data_information = soc.received().decode()
	print("Received Secret Question" + str(data_information))
	file.close()
	

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()