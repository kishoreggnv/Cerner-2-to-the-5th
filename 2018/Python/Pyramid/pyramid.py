# cerner_2^5_2018
# Print pyramid based on the specified height

height = int(input('Enter the height of pyramid :'))
 
for i in range(1,height+1):
	print ((height-i)*' '+i*'^ ')
