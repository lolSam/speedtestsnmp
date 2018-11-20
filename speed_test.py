import speedtest
import pathlib
import os
import time

def download_test():

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
	result = "{:.2f}\n".format(result_dict["download"] / 1048576)

	# save result to file
	path = os.path.join(str(pathlib.Path.home()),"speedtestsnmp/download_result")

	file = open(path, 'w')
	file.write(result)
	file.close()

def upload_test():

	# Perform speedtest on upload to Telstra server(s) (ID: 2225)
	servers = [2225]

	s = speedtest.Speedtest()
	s.get_servers(servers)
	s.get_best_server()
	s.upload()
	s.results.share()

	# Convert to a dict
	result_dict = s.results.dict()

	# Grab result and convert from bit/s to megabit/s to the precision of 2s
	result = "{:.2f}\n".format(result_dict["upload"] / 1048576)

	# save result to file
	path = os.path.join(str(pathlib.Path.home()),"speedtestsnmp/upload_result")

	file = open(path, 'w')
	file.write(result)
	file.close()


def run_loop(interval):
	while True:
		download_test()
		upload_test()
		print("Speed test ran")
		time.sleep(interval)

run_loop(300)
