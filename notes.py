import speedtest

s=speedtest.Speedtest()

print("Testing...\n")

downloadSpeed = s.download() / 1048576
uploadSpeed = s.upload() / 1048576
pingResult = round(s.results.ping)


print(f"Download speed: {downloadSpeed:.2f} Mbps")
print(f"Upload speed: {uploadSpeed:.2f} Mbps")
print(f"Ping: {pingResult} ms")