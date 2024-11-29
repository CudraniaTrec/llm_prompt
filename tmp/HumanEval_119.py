def match_parens(lst):
    open_count1 = lst[0].count('(')
    close_count1 = lst[0].count(')')
    open_count2 = lst[1].count('(')
    close_count2 = lst[1].count(')')

    # Check both concatenation orders
    first_concat = open_count1 + open_count2
    second_concat = close_count1 + close_count2

    if first_concat == second_concat and abs(open_count1 - close_count1) <= close_count2 and abs(open_count2 - close_count2) <= open_count1:
        return 'Yes'
    
    first_concat = close_count1 + close_count2
    second_concat = open_count1 + open_count2

    if first_concat == second_concat and abs(close_count1 - open_count1) <= open_count2 and abs(close_count2 - open_count2) <= close_count1:
        return 'Yes'

    return 'No'
  open_count1 = lst[0].count('(')
  close_count1 = lst[0].count(')')
  open_count2 = lst[1].count('(')
  close_count2 = lst[1].count(')')

  first_concat = open_count1 + open_count2
  second_concat = close_count1 + close_count2

  if first_concat == second_concat and abs(open_count1 - close_count1) <= close_count2 and abs(open_count2 - close_count2) <= open_count1:
      return 'Yes'
  return 'No'
def check(candidate):

    # Check some simple cases
    assert candidate(['()(', ')']) == 'Yes'
    assert candidate([')', ')']) == 'No'
    assert candidate(['(()(())', '())())']) == 'No'
    assert candidate([')())', '(()()(']) == 'Yes'
    assert candidate(['(())))', '(()())((']) == 'Yes'
    

    # Check some edge cases that are easy to work out by hand.


check(match_parens)