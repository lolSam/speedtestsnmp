import subprocess

p = subprocess.Popen('ping mel1.speedtest.telstra.net')
p.wait()

print(p)
