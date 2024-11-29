#Write a function to check whether the given amount has no profit and no loss
def noprofit_noloss(actual_cost,sale_amount): 
  if(sale_amount == actual_cost):
    return True
  else:
    return False