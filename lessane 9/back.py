inf = 46

def function():
    global inf
    inf = 45
    return inf
print(inf)
function()
print(inf)