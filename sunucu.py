import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # burda socket.AF_INET sebebi ipv4 adresi yazmamız socket.SOCK_STREAM ise portun tipini tcp seçmemeiz socket.DGRAM ise udp
server.bind(("localhost", 4444))#0.0.0.0 yerel ağdır aynı zamanda localhost ve 127.0.0.1 gibi 12345 ise portu
server.listen(1)#burda sadece bir kişi bağlanabilir

print("Server dinliyor.")

client_socket, client_address = server.accept() #burda client_socket istemci ile nesne arasında kurulan iletişimi sağlayan bir nesne olarak tanımlayabiliriz
print(f"bağlandı {client_address}")

while True:
    message = client_socket.recv(1024).decode("utf-8")#burda clienttan gelicek olan verileri decode yapıyoruz
    print(f"Client: {message}")
    response = input("sen: ")
    client_socket.send(response.encode("utf-8")) #burda paketi encode edip karşıya yüklüyoruz.Utf-8 aşağıda tanımladım


#port nedir: portu dış ağa açılan bir kapıdır 
#utf-8 farklı dillerdeki harfleri rakamları ve diğer karakterleri destekler
#tcp ile udp arasındaki fark: tcp gelen paketlerin gidip gitmesini kontrol ederken udp gönderir paketi arkasına bakmaz

#not: eğer bunu public yapmak isterseniz ordaki locahost açtığınız öyle kalıcak portta öyle kalıcak ama clientta statik ipsini ve portunu yazıcaz