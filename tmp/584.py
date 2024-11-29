def find_adverbs(sentence):
    words = sentence.split()
    for index, word in enumerate(words):
        if word.endswith('ly'):
            return f"{index}-{len(word)+sum(len(w)+1 for w in words[:index])}: {word}"
    return None
def find_adverbs(sentence):
    words = sentence.split()
    for index, word in enumerate(words):
        if word.lower().endswith('ly'):
            return f"{index}-{len(word)+sum(len(w)+1 for w in words[:index])}: {word}"
    return None
def find_adverbs(sentence):
    words = sentence.split()
    for index, word in enumerate(words):
        if word.lower().endswith('ly'):
            start_index = sentence.index(word)
            return f"{start_index}-{start_index + len(word)}: {word}"
    return None
assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
assert find_adverbs("Complete the task quickly") == '18-25: quickly'