

def ADD(x, y):
    for i in range(y):
        x = x + 1
    return(x)

def MULT(x, y):
    z = 0
    for i in range(y):
        z = ADD(z,x)
    return(z)

def SUB(x,y):
    for i in range(y):
        if(x != 0):
            x = x - 1
    return(x)

def DIV(x, y): # x / y # substract y from x x times # should always be enough afaik
    
    time = x
    z = 0
    for i in range(time):
        if(x == 0):
            x = 0 # an empty statement since I want !=
        else:
            f = y - 1
            n = SUB(x, f)
            if(n == 0):
                x = 0
            else:
                x = SUB(x, y)
                z = z + 1
    return(z)

def MOD(x,y): # x mod y # 
    return (SUB(x, (MULT(DIV(x,y), y))))

def MVALUE(x):
    time = x
    z = 0
    r = 10
    for i in range(time):
        x = DIV(x,10)
        if(x == 0):
            x = x
        else:
            z = z + 1
    for i in range(z):
        r = MULT(r, 10)
    return(r)

def EMPTY(stack):
    stack = stack - 1
    if(stack == 0):
        return(0)
    else:
        return(1)

def POP(stack, mv):
    return(MOD(stack, mv))

def UPDATE(stack, mv):
    return(DIV(stack, mv))