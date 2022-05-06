# input
message = "Exam"
message = message.upper()

# matrix key input
key = [[9,4],[5,7]]

# message matrix declaration and generation
msg_mat = [[0]*2 for i in range(0,2)]

l = 0
for i in range(0,2):
	for j in range(0,2):
		msg_mat[j][i] = ord(message[l])%65	# ord convets char to ascii equivalent
		l = l+1

print("message matrix : ",msg_mat)

# encripted matrix generation using key*msg_matrix multiplication
enc_mat = [[0]*2 for i in range(0,2)]
for i in range(0,2):
	for j in range(0,2):
		for k in range(0,2):
			enc_mat[i][j] += key[i][k]*msg_mat[k][j]
			
#mod 26 for rounding off ot matrix message
for i in range(0,2):
	for j in range(0,2):
		enc_mat[i][j] = enc_mat[i][j]% 26

print("encripted matrix : ",enc_mat)

enc_msg = ""
for i in range(0,2):
	for j in range(0,2):
		enc_msg += chr((enc_mat[j][i]) + 65)	#chr converts ascii to character equivalent

print("encriptd message : ",enc_msg)
		
