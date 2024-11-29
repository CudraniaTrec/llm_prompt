def move_num(s):
    letters = []
    numbers = []
    
    for char in s:
        if char.isdigit():
            numbers.append(char)
        else:
            letters.append(char)
    
    return ''.join(letters) + ''.join(numbers)
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'