#Write a function to sort a given matrix in ascending order according to the sum of its rows.
def sort_matrix(M):
    result = sorted(M, key=sum)
    return result