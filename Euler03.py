def factors(value):
	#factors =[]
	range_list = value

	number = 2

	while number <= range_list:
		if value % number == 0 and is_prime(number)== True:
			largest_factor = number
			range_list = range_list/number
		number = number + 1
	# 		continue
	# 	elif is_prime(number)== True:
	# 		factors.append(number)

	# #print factors
	# return factors[-1]

	return largest_factor


def is_prime(num):

	result= True

	for digit in range (2, num):
		if digit < (num/2) and (num%digit) == 0:
			result = False
			break

	return result 

# print is_prime(17)
# print is_prime(9)
# print is_prime(13)

print factors(13195)
print factors(600851475143)