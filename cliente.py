import socket


BROADCAST_PORT = 37020

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", BROADCAST_PORT))

print("Aguardando anúncio do servidor...")

data, addr = sock.recvfrom(1024)
msg = data.decode()
name, ip, port = msg.split(";")

print(f"Servidor encontrado: {name} em {ip}:{port}")



HOST = ip  # coloque aqui o IP da máquina do servidor
PORT = int(port)



# Exemplo de consulta
query = "SELECT nome FROM Usuario where id = 4;"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def requestBD():
    client.sendall(query.encode())

    data = client.recv(4096).decode()
    print("Resposta do servidor:", data)


requestBD()

client.close()