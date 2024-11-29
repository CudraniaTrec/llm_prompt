#Write a function to find number of lists present in the given tuple.
def find_lists(Input): 
	if isinstance(Input, list): 
		return 1
	else: 
		return len(Input) 