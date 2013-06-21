fibo_list = [1, 2]
total = 0

while fibo_list[-1] < 4000000:
	fibo_list.append(fibo_list[-1]+ fibo_list[-2])






for num in fibo_list:

	# fibo_list[len(fibo_list):] = [num]
	# fibo_list[-1] = fibo_list[i - 1] + fibo_list [ - 2]

	# if fibo_list[i]%2 == 0:
	# 	total = total + fibo_list[i]

	if num % 2 == 0:
		total += num

print total