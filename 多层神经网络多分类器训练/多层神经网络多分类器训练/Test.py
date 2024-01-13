g=2
def f():
    global g
    g=3
    return
f()
print(g)