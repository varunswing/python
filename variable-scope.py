a = 342

def local_scope():
    a = 23
    print(a)

def global_scope():
    print(a)

local_scope()
global_scope()