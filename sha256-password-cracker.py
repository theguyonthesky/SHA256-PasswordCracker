from pwn import *
import sys
#import time

#check whether the script got exactly 1 arg (the hash)
if len(sys.argv) != 2:
	print("Invalid arguments!")
	print(f">>> {sys.argv[0]} <sha256sum>")
	exit()

target_hash = sys.argv[1]
password_file = "rockyou.txt"
attemtps = 0

with log.progress(f"Attempting to crack {target_hash}\n") as progress: # Show a progress/status message while attempting the crack
	with open (password_file, 'r', encoding='latin-1') as file:
		for password in file: #the password variable holds one password at a time
			password = password.strip("\n").encode('latin-1') #all passwords in the file get encoded one by one in the loop
			password_hash = sha256sumhex(password) #note that sha256sum function in pwntools returns raw bytes; which cant be compared, use sha256sumhex to get hex string for comparison
			progress.status(f"{attemtps}, {password.decode('latin-1')}=={password_hash}")
			#time.sleep(1)
			if password_hash == target_hash:
				progress.success(f"Password hash found after {attemtps} attemtps! {password.decode('latin-1')} hashes to {password_hash}")
				#break
				exit()
			attemtps+=1
		progress.failure("Password hash not found!")
		#print(f"Total attemtps made: {attemtps}")


#.status, .success, .failure
#These are methods of the progress object to show different message types:
#.status = ongoing status update
#.success = success message (usually ends the progress)
#.failure = failure message (ends progress)
