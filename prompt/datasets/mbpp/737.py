#Write a function to check whether the given string is starting with a vowel or not using regex.
import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	return re.search(regex, string)