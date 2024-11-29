def insert_element(lst, elem):
    result = []
    for item in lst:
        result.append(elem)
        result.append(item)
    return result
assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java']
assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']