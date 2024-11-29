def remove_length(s, k):
    words = s.split()  # Split the string into a list of words
    filtered_words = [word for word in words if len(word) != k]  # Filter out words with length k
    return ' '.join(filtered_words)  # Join the filtered words back into a string
assert remove_length('The person is most value tet', 3) == 'person is most value'
assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'