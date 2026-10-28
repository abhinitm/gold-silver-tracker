import requests

URL = "https://www.amfiindia.com/spages/NAVAll.txt"

response = requests.get(URL, timeout=30)
print("Status:", response.status_code)

lines = response.text.splitlines()
print("Total lines:", len(lines))

print("\n--- First 12 lines ---")
for line in lines[:12]:
       print(line)

print("\n--- Nippon India gold/silver lines ---")
for line in lines:
       low = line.lower()
       if "nippon india" in low and ("gold" in low or "silver" in low):
           print(line)