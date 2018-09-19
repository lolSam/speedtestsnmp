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

# Grab result and convert from bit/s to megabit/s to the precision of 2s
result = "{:.2f}".format(result_dict["download"] / 1048576)

# save result to file
file = open('download_result', 'w')
file.write(result)
file.close()
