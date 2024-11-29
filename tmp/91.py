def find_substring(string_list, substring):
    for string in string_list:
        if substring in string:
            return True
    return False
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True