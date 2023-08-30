import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 4444))#burda sunucuya bağlanıyor

while True:
    message = input("sen: ")
    client_socket.send(message.encode("utf-8"))#mesaj gönderiyor encode edip
    response = client_socket.recv(1024).decode("utf-8") # burda gelen paketleri utf-8 ile encode edilmiş paketi utf-8 ile decode ediyor
    print(f"server: {response}")#serverdan gelen cevapı console yazdırıyor