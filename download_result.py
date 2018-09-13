import speedtest

# Perform speedtest on download to Telstra server(s) (ID: 2225)
servers = [2225]

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.results.share()

# Convert to a dict 
result_dict = s.results.dict()

# Grab result and convert from bit/s to megabit/s
result = result_dict["download"] / 1048576

# Print resulting to the precision of 2 decimal places
print("%.2f" % result)
