# Hide the message
secret = input("Enter a secret message: ")
with open("hidden.txt", "w") as file:
    file.write(secret)
print("✅ Message hidden successfully!")

# Ask if the user wants to reveal it
if input("Do you want to reveal the message? (yes/no): ").lower() == "yes":
    with open("hidden.txt", "r") as file:
        print("🔍 Hidden message:", file.read())
else:
    print("🔒 Message remains hidden.")
