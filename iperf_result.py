import iperf3

client = iperf3.Client()
client.duration = 5
client.server_hostname = 'speedtest.serverius.net'
client.port = 5002
result = client.run()

print("%.2f" % result.sent_Mbps)
