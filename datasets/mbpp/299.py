#Write a function to calculate the maximum aggregate from the list of tuples.
from collections import defaultdict
def max_aggregate(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])