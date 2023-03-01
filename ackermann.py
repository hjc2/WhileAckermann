
#adds two numbers
def ADD(x, y):
    for i in range(y):
        x = x + 1
    return(x)

#multiplies two numbers
def MULT(x, y):
    z = 0
    for i in range(y):
        z = ADD(z,x)
    return(z)

#floored subtraction
def SUB(x,y):
    for i in range(y):
        if(x != 0):
            x = x - 1
    return(x)

#integer division 
def DIV(x, y):
    
    time = x
    z = 0
    for i in range(time):
        if(x == 0):
            x = 0
        else:
            f = y - 1
            n = SUB(x, f)
            if(n == 0):
                x = 0
            else:
                x = SUB(x, y)
                z = z + 1
    return(z)

def MOD(x,y): # modulus
    return (SUB(x, (MULT(DIV(x,y), y))))

#returns the power of 10 bigger than x.
# 99->100
# 8 -> 10
# 4885 -> 10000
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

# determines if a stack is empty
# a stack is empty when stack == 1
def EMPTY(stack):
    stack = SUB(stack, 1)
    if(stack == 0):
        return(0)
    else:
        return(1)

#pushes data onto the stack
def PUSH(stack, data, mv):
    stack = stack * mv
    return(stack + data)

#returns the value on the top of the stack
def POP(stack, mv):
    return(MOD(stack, mv))

#returns the stack with the top popped off
def UPDATE(stack, mv):
    return(DIV(stack, mv))

#computes ackermann function
#https://mathworld.wolfram.com/AckermannFunction.html

def ACK(m, n):

    mv = MVALUE(m)

    stack = 1
    stack = PUSH(stack, m, mv)

    empty = EMPTY(stack)

    while empty > 0:
        lst = [int(x) for x in str(stack)]

        print("stack " + str(lst[1:]))
        # print("value " + str(n))
        
        m = POP(stack, mv)
        stack = UPDATE(stack, mv)
        if m == 0:
            n += 1
        elif n == 0:
            n = 1
            stack = PUSH(stack, m - 1, mv)
        else:
            n = n - 1
            stack = PUSH(stack, m - 1, mv)
            stack = PUSH(stack, m, mv)
        
        empty = EMPTY(stack)

    return n

print(ACK(1,6))