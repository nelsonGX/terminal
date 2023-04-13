import os

print("\n  _                      _             _ ")
print(" | |                    (_)           | |")
print(" | |_ ___ _ __ _ __ ___  _ _ __   __ _| |")
print(" | __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |")
print(" | ||  __/ |  | | | | | | | | | | (_| | |")
print("  \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|")
print("                                                 v0.1\n")


while True:
	command = str(input("Python@terminal:~$ "))
	if command == "stop":
		print("Leaving terminal...")
		exit()
	os.system(command)