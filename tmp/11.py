def remove_Occ(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    
    if first_occurrence == -1 or first_occurrence == last_occurrence:
        return s.replace(char, '', 1)  # Remove only if there's one occurrence
    
    return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[last_occurrence + 1:]
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("abcda","a") == "bcd"
assert remove_Occ("PHP","P") == "H"