# Hide the message in a file with logs:
import datetime
import requests

# Get current time and public IPv4 address
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ip_address = requests.get('https://api.ipify.org').text

# Save secret message
secret = input("Enter a secret message: ")
with open("hidden.txt", "w") as file:
    file.write(f"Time: {time_stamp}\nIP: {ip_address}\nSecret: {secret}\n")

print("✅ Message hidden!")

# Reveal message
if input("Reveal message? (yes/no): ").lower() == "yes":
    print(open("hidden.txt").read())
else:
    print("🔒 Message remains hidden.")
