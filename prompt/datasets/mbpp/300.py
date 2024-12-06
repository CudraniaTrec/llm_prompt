#Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
def count_binary_seq(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 