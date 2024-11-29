def start_withp(words):
    result = []
    for word in words:
        for w in word.split():
            if w.startswith('P') or w.startswith('p'):
                result.append(w)
                if len(result) == 2:
                    return tuple(result)
    return tuple(result)  # In case there are less than 2 words starting with 'p'
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')