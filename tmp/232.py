def larg_nnum(lst, n):
    if n <= 0:
        return []
    return sorted(lst, reverse=True)[:n]
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])