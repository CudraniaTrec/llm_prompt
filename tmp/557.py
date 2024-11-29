def toggle_string(s):
    return s.swapcase()
assert toggle_string("Python")==("pYTHON")
assert toggle_string("Pangram")==("pANGRAM")
assert toggle_string("LIttLE")==("liTTle")