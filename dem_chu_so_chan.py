def dem_chu_so_chan(so):
    if so == 0:
        return 1
    so = abs(so)   
    dem = 0
    while so > 0:
        chu_so_cuoi = so % 10
        if chu_so_cuoi % 2 == 0:
            dem += 1
        so //= 10
    return dem

def tong(a,b):
    return a+b