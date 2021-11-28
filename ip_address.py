import socket
import ipget

# インターフェイスを指定して ip_address を取得
target_ip = ipget.ipget()
print(target_ip.ipaddr("eth0"))

# ローカルのループバックのアドレスを取得
ip = socket.gethostbyname(socket.gethostname())
print(ip)

# ネットワークに接続するために使用されるインターフェイスのIPアドレスを取得する
connect_interface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect_interface.connect(("8.8.8.8", 80))
print(connect_interface.getsockname()[0])
