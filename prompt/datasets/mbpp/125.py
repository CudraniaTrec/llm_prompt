#Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
def find_length(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0