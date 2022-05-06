alphabets = "abcdefghijklmnopqrstuvwxyz"

## ciphertext
m = input("enter message : ")
key = int(input("enter key : "))

## encryption

ciphertext = ""
for alp in m:
	if alp in alphabets:
		pos = alphabets.find(alp)		#gives index of the found element from the string named "alphabets"
		ciphertext += alphabets[(pos+key)%26]	#right shift + rotating the values if the value exceeds 26 i.e eg 24 + 6 = 30 % 26 = 4
	else:
		ciphertext +=alp			

print("ciphertext : ",ciphertext)

## decryption
deciphertext = ""
for alp in ciphertext:
	if alp in alphabets:
		pos = alphabets.find(alp)
		#if pos-key < 0:
		#	deciphertext += alphabets[26 + pos -key]
		#else: 
		deciphertext += alphabets[(pos-key)%26]
	else:
		deciphertext +=alp

print("deciphertext : ",deciphertext)


		  

