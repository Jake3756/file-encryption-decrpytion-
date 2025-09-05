from  cryptography.fernet import Fernet
import os

key="b7p4GZ-ulmL7xFz0GeBk_8jlf3o5l0Y49mSfnq3VrfE="
cipher=Fernet(key)

file=input("enter your file name:")
mode=int(input("choose your mode 1 for encryption 0 for decryption :"))


if os.path.isfile(file) == True:

	if mode == 1:
		with open(file,'rb') as f:
			content=f.read()

		encrypted=cipher.encrypt(content)
		with open(file,'wb') as f:
			f.write(encrypted)
	elif mode == 0:
		with open(file,'rb') as f:
			content=f.read()

		try:
			decrypted=cipher.decrypt(content)
			with open(file,'wb') as f:
				f.write(decrypted)
		except Exception as e:
			print("decryption failed.Error :",str(e))
	else:
		print("invalid operation.")
else:
	print("sorry but this file does not exist ")
