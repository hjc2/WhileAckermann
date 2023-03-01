
X, Y -> ADD

DO Y TIMES [ INCR(X) ]
ADD := X



X, Y -> MULT

Z := 0
DO Y TIMES [ Z := ADD(Z, X) ]



X, Y -> SUB

DO Y TIMES [ DECR(X) ]
SUB := X


X, Y -> DIV

T := X
Z := 0

DO T TIMES [
    IF X = 0 THEN
        [ X := 0 ]
    ELSE
        [
            F := Y - 1
            N := SUB(X,F)
        ]
        IF N == 0 THEN
            [ X == 0 ]
]
