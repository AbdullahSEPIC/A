import openvpn_api
import webbrowser

# Connect to the OpenVPN server
vpn = openvpn_api.connect('server1.freevpn.me', 'freevpn.me', 'k2YbR6Ve2JBe')

# Start the VPN connection
vpn.start()

# Get the VPN IP address
vpn_ip = vpn.get_vpn_ip()

# Display the VPN IP address
print("Connected to VPN. IP Address:", vpn_ip)

# Open Yahoo page in a web browser
webbrowser.open('https://www.yahoo.com')

# Disconnect from the VPN
vpn.stop()
