from sys import argv

script, filename = argv

txt = open(filename)
letter = txt.read()

alph_list =[0] * 26

for char in letter:
	lower_letter = char.lower()
	if 97 <=  ord(lower_letter) <=122:
		alph_list[ord(lower_letter) - 97] += 1

for value in alph_list:
	print value

#Another way to solve question is using a dictionary BUT the dictionary is not ordered


# dictionary = {}

# for char in letter:
# 	lower_letter = char.lower()
# 	# if char in {}:
# 	# 	continue
# 	# else:
# 	if 97 <= ord(lower_letter) <= 122:
# 		if lower_letter in dictionary:
# 			dictionary[lower_letter] += 1
# 		else:
# 			dictionary[lower_letter] = 1

# 		# if convert_letter in dictionary:
			
# # print dictionary

# for key in dictionary:
# 	print dictionary[key]







txt.close()