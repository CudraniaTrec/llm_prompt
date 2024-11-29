def loss_amount(selling_price, cost_price):
    if selling_price < cost_price:
        return cost_price - selling_price
    return 0
assert loss_amount(1500,1200)==0
assert loss_amount(100,200)==100
assert loss_amount(2000,5000)==3000